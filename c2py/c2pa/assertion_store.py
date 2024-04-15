
from c2py.jumbf_boxes.super_box import SuperBox
from c2py.utils.content_types import c2pa_content_types


class AssertionStore(SuperBox):

    def __init__(self, assertions=None):
        self.assertions = [] if assertions == None else assertions
        super().__init__(content_type=c2pa_content_types['assertions'], label='c2pa.assertions', content_boxes=assertions)

