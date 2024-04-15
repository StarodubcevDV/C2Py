
from c2py.jumbf_boxes.super_box import SuperBox
from c2py.utils.assertion_schemas import get_assertion_content_type, get_assertion_label


class Assertion(SuperBox):

    def __init__(self, assertion_type, schema):
        self.type = assertion_type
        self.schema = schema

        super().__init__(content_type=get_assertion_content_type(assertion_type),
                         label=get_assertion_label(assertion_type))
