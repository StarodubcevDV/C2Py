
from c2py.jumbf_boxes.super_box import SuperBox
from c2py.jumbf_boxes.jumbf_content_types import jumbf_content_types


class Manifest(SuperBox):

    claim = None
    claim_signature = None
    assertion_store = None


    def __init__(self, claim = None, claim_signature = None, assertion_store = None):
        self.claim = claim
        self.claim_signature = claim_signature
        self.assertion_store = assertion_store
        content_boxes = [self.claim, self.claim_signature, self.assertion_store]

        super().__init__(content_type=jumbf_content_types["json"], content_boxes=content_boxes)


    def get_content_type(self):
        return self.description_box.content_type