import pytest

import hashlib

from c2py.c2pa.manifest import Manifest
from c2py.c2pa.manifest_store import ManifestStore
from c2py.c2pa.assertion import Assertion
from c2py.c2pa.assertion_store import AssertionStore
from c2py.c2pa.claim import Claim
from c2py.c2pa.claim_signature import ClaimSignature
from c2py.utils.assertion_schemas import C2PA_AssertionTypes
from c2py.c2pa_injection.jpeg_injection import JpgSegmentApp11Storage


key_filepath = 'tests/fixtures/crypto/ps256.pem'
cert_filepath = 'tests/fixtures/crypto/ps256.pub'

if key_filepath != '':
    with open(key_filepath, 'rb') as f:
        key = f.read()
else:
    key = []

if cert_filepath != '':
    with open(cert_filepath, 'rb') as f:
        certificate = f.read()
else:
    key = []


def test_integration_c2pa():
    
    cai_offset = 2
    
    with open("tests/fixtures/test_image.jpg", "rb") as binary_image:
        raw_bytes = binary_image.read()

    manifest = Manifest()

    creative_work_schema = {
        "@context": "https://schema.org",
        "@type": "CreativeWork",
        "author": [
            {
                "@type": "Person",
                "name": "Dmitriy Starodubtcev"
            }
        ],
        "copyrightYear": "2024",
        "copyrightHolder": "c2py"
    }
    creative_work_assertion = Assertion(C2PA_AssertionTypes.creative_work, creative_work_schema)
    
    hash_data_schema = {
        "exclusions": [{"start": cai_offset, "length": 65535}], # set length to 65535, library will calculate length by itself
        "name": "jumbf manifest",
        "alg": "sha256",
        "hash": hashlib.sha256(raw_bytes).digest(),
        "pad": []
    }
    hash_data_assertion = Assertion(C2PA_AssertionTypes.data_hash, hash_data_schema)

    assertion_store = AssertionStore(assertions=[creative_work_assertion, hash_data_assertion])
    manifest.set_assertion_store(assertion_store)
    print("Assetion Store was created!")
    
    claim = Claim(claim_generator='C2Py', manifest_label=manifest.get_manifest_label(), assertion_store=assertion_store)
    manifest.set_claim(claim)
    print("Claim was created!")
    
    claim_signature = ClaimSignature(claim, private_key=key, certificate=certificate)
    manifest.set_claim_signature(claim_signature)
    print("Claim Signature was created!")
    
    manifest_store = ManifestStore([manifest])
    print(f'Manifest l_box: {manifest_store.get_serialized_length()}')
    
    manifest_store.set_hash_data_length()

    c2pa_jpg_app11_storage = JpgSegmentApp11Storage(app11_segment_box_length=manifest_store.get_length(),
                                                    app11_segment_box_type=manifest_store.get_type(),
                                                    payload=manifest_store.serialize())
    
    raw_bytes = raw_bytes[:cai_offset] + c2pa_jpg_app11_storage.serialize() + raw_bytes[cai_offset:]
    
    print(f'Serialized length: {c2pa_jpg_app11_storage.get_serialized_length()}')
    
    # raw_bytes = insert_xmp_key(raw_bytes, manifest.get_manifest_label())
    
    with open("tests/fixtures/test_injected_image.jpg", "wb") as binary_file:
        binary_file.write(raw_bytes)


    assert 1 != 1