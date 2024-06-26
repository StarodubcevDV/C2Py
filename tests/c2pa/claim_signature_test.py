import pytest

from c2py.c2pa.claim_signature import ClaimSignature
from c2py.c2pa.claim import Claim
from c2py.c2pa.assertion_store import AssertionStore
from c2py.c2pa.assertion import Assertion
from c2py.utils.content_types import c2pa_content_types
from c2py.utils.assertion_schemas import C2PA_AssertionTypes


def test_create_claim_signature():
    
    test_claim_signature = ClaimSignature(claim=None, private_key=None, certificate=None)

    assert test_claim_signature != None
    assert test_claim_signature.get_label() == 'c2pa.signature'
    assert test_claim_signature.get_content_type() == c2pa_content_types["claim_signature"]


def test_create_claim_signature_with_claim():

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
    test_assertion = Assertion(assertion_type=C2PA_AssertionTypes.creative_work, schema=creative_work_schema)
    test_assertions = [test_assertion, test_assertion]
    test_assertion_store = AssertionStore(assertions=test_assertions)
    test_claim = Claim(claim_generator='C2Py', manifest_label='valid_manifest_label', assertion_store=test_assertion_store)

    test_claim_signature = ClaimSignature(claim=test_claim, private_key=key, certificate=certificate)

    test_claim_signature.claim != None
    test_claim_signature.content_boxes[0].get_type() == 'cbor'.encode('utf-8').hex()
