
from c2py.jumbf_boxes.super_box import SuperBox
from c2py.jumbf_boxes.content_box import ContentBox
from c2py.utils.assertion_schemas import get_assertion_content_type, get_assertion_label, json_to_bytes, cbor_to_bytes
from c2py.utils.content_types import jumbf_content_types


class Assertion(SuperBox):

    def __init__(self, assertion_type, schema):
        self.type = assertion_type
        self.schema = schema
        self.payload = self.get_payload_from_schema()
        content_box = ContentBox(payload=self.payload)

        super().__init__(content_type=get_assertion_content_type(assertion_type),
                         label=get_assertion_label(assertion_type),
                         content_boxes=[content_box])


    def get_payload_from_schema(self):
        if get_assertion_content_type(self.type) == jumbf_content_types['json']:
            return json_to_bytes(self.schema)
        elif get_assertion_content_type(self.type) == jumbf_content_types['cbor']:
            return cbor_to_bytes(self.schema)
        elif get_assertion_content_type(self.type) == jumbf_content_types['codestream']:
            return self.schema['payload']
        else:
            return b''
        
        
    def get_data_for_signing(self):
        return self.description_box.serialize() + self.serialize_content_boxes()
