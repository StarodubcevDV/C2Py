
from c2py.utils.assertion_schemas import C2PA_AssertionTypes
from c2py.utils.content_types import C2PA_ContentTypes
from c2py.c2pa.assertion import Assertion
from c2py.c2pa.assertion_store import AssertionStore
from c2py.c2pa.claim import Claim
from c2py.c2pa.claim_signature import ClaimSignature
from c2py.c2pa.manifest import Manifest
from c2py.c2pa.manifest_store import ManifestStore
from c2py.c2pa_injection.jpeg_injection import JpgSegmentApp11Storage


# Function for asserion creation.
def C2Py_GenerateAssertion(assertion_type: C2PA_AssertionTypes, assertion_schema) -> Assertion:
    return Assertion(assertion_type, assertion_schema)


# Function for manifest store generation.
def C2Py_GenerateManifest(assertions: list, private_key: str, certificate_chain: str) -> ManifestStore:
    manifest = Manifest()
    
    assertion_store = AssertionStore(assertions=assertions)
    manifest.set_assertion_store(assertion_store)
    
    claim = Claim(claim_generator='C2Py', manifest_label=manifest.get_manifest_label(), assertion_store=assertion_store)
    manifest.set_claim(claim)
    
    claim_signature = ClaimSignature(claim, private_key=private_key, certificate=certificate_chain)
    manifest.set_claim_signature(claim_signature)
    
    return ManifestStore([manifest])

 
# Function for emplacing manifest to source data
def C2Py_EmplaceManifest(format_type: C2PA_ContentTypes, content_bytes: bytes, c2pa_offset: int, manifest: ManifestStore) -> bytes:
    
    manifest.set_hash_data_length()
    
    if format_type == C2PA_ContentTypes.jpg:
        c2pa_jpg_app11_storage = JpgSegmentApp11Storage(app11_segment_box_length=manifest.get_length(),
                                                    app11_segment_box_type=manifest.get_type(),
                                                    payload=manifest.serialize())
        
        return content_bytes[:c2pa_offset] + c2pa_jpg_app11_storage.serialize() + content_bytes[c2pa_offset:]
    else:
        print(f'Unsupported content type {format_type}!')
        return b''
    
