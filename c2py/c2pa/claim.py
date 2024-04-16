
import hashlib

from c2py.jumbf_boxes.super_box import SuperBox
from c2py.jumbf_boxes.content_box import ContentBox
from c2py.utils.content_types import c2pa_content_types, jumbf_content_types
from c2py.utils.assertion_schemas import get_assertion_label, cbor_to_bytes


class Claim(SuperBox):

    def __init__(self, assertion_store, claim_generator='', manifest_label=''):
        self.claim_generator = claim_generator
        self.manifest_label = manifest_label
        self.claim_signature_label = f'self#jumbf=c2pa/{self.manifest_label}/c2pa.signature'

        content_boxes = []
        if assertion_store != None:
            self.assertion_store = assertion_store
            content_box = ContentBox(payload=self.generate_claim_schema())
            content_boxes.append(content_box)

        super().__init__(label='c2pa.claim', content_type=c2pa_content_types["claim"], content_boxes=content_boxes)

    
    def generate_claim_schema(self):
        claim_schema = {}
        claim_schema['alg'] = "sha256"
        claim_schema['claim_generator'] = self.claim_generator
        claim_schema['signature'] = f'self#jumbf=c2pa/{self.manifest_label}/c2pa.signature"'
        claim_schema['assertions'] = [
            {
                'url': f'self#jumbf=c2pa/{self.manifest_label}/c2pa.assertions/{get_assertion_label(assertion.type)}',
                'hash': (hashlib.sha256(assertion.serialize())).digest()
            } for assertion in self.assertion_store.assertions
        ]

        return cbor_to_bytes(claim_schema)

