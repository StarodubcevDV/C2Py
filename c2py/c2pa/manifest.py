
import uuid

from c2py.jumbf_boxes.super_box import SuperBox
from c2py.utils.content_types import c2pa_content_types


class Manifest(SuperBox):

    def __init__(self, claim = None, claim_signature = None, assertion_store = None):
        self.claim = claim
        self.claim_signature = claim_signature
        self.assertion_store = assertion_store
        self.manifest_label = '{}:urn:uuid:{}'.format("c2py", uuid.uuid4())

        super().__init__(content_type=c2pa_content_types["default_manifest"], label=self.manifest_label)

    
    def set_claim(self, claim):
        self.claim = claim
        self.add_content_box(self.claim)
        self.sync_payload()


    def set_claim_signature(self, claim_signature):
        self.claim_signature = claim_signature
        self.add_content_box(self.claim_signature)
        self.sync_payload()


    def set_assertion_store(self, assertion_store):
        self.assertion_store = assertion_store
        self.add_content_box(self.assertion_store)
        self.sync_payload()
        

    def get_manifest_label(self):
        return self.manifest_label


    def set_claim_signature(self, claim_signature):
        self.claim_signature = claim_signature
        self.add_content_box(self.claim_signature)


    def get_assertions(self):
        return self.assertion_store.get_assertions()
    
