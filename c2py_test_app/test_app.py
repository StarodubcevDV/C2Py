import hashlib

from c2py.interface import C2Py_GenerateAssertion, C2Py_GenerateManifest, C2Py_EmplaceManifest, C2PA_AssertionTypes, C2PA_ContentTypes


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

cai_offset = 2

with open("tests/fixtures/test_image.jpg", "rb") as binary_image:
    raw_bytes = binary_image.read()

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
creative_work_assertion = C2Py_GenerateAssertion(C2PA_AssertionTypes.creative_work, creative_work_schema)

hash_data_schema = {
    "exclusions": [{"start": cai_offset, "length": 65535}], # set length to 65535, library will calculate length by itself
    "name": "jumbf manifest",
    "alg": "sha256",
    "hash": hashlib.sha256(raw_bytes).digest(),
    "pad": []
}
hash_data_assertion = C2Py_GenerateAssertion(C2PA_AssertionTypes.data_hash, hash_data_schema)

assertions = [creative_work_assertion, hash_data_assertion]

manifest = C2Py_GenerateManifest(assertions=assertions, private_key=key, certificate_chain=certificate)

raw_bytes = C2Py_EmplaceManifest(C2PA_ContentTypes.jpg, raw_bytes, cai_offset, manifest)

with open("c2py_test_app/test_injected_image.jpg", "wb") as binary_file:
    binary_file.write(raw_bytes)
