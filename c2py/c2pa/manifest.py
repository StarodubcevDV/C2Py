
from c2py.jumbf_boxes.super_box import SuperBox
from c2py.utils.content_types import c2pa_content_types


class Manifest(SuperBox):

    def __init__(self, claim = None, claim_signature = None, assertion_store = None):
        self.claim = claim
        self.claim_signature = claim_signature
        self.assertion_store = assertion_store

        super().__init__(content_type=c2pa_content_types["default_manifest"])

    
    def set_claim(self, claim):
        self.claim = claim
        self.add_content_box(self.claim)


    def set_claim_signature(self, claim_signature):
        self.claim_signature = claim_signature
        self.add_content_box(self.claim_signature)


    def set_assertion_store(self, assertion_store):
        self.assertion_store = assertion_store
        self.add_content_box(self.assertion_store)

