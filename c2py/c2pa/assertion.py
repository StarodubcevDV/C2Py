
from c2py.jumbf_boxes.super_box import SuperBox
from c2py.jumbf_boxes.content_box import ContentBox
from c2py.utils.assertion_schemas import get_assertion_content_type, get_assertion_content_box_type, get_assertion_label, json_to_bytes, cbor_to_bytes
from c2py.utils.content_types import jumbf_content_types


class Assertion(SuperBox):

    def __init__(self, assertion_type, schema):
        self.type = assertion_type
        self.schema = schema
        self.payload = self.get_payload_from_schema()
        
        content_box = ContentBox(box_type=get_assertion_content_box_type(self.type), payload=self.payload)

        super().__init__(content_type=get_assertion_content_type(self.type),
                         label=get_assertion_label(self.type),
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

    
    def set_hash_data_length(self, length):
        if self.schema['name'] == 'jumbf manifest':
            for exclusion_id in range(len(self.schema['exclusions'])):
                if self.schema['exclusions'][exclusion_id]['length'] == 65535:
                    self.schema['exclusions'][exclusion_id]['length'] = length
        
        self.payload = self.get_payload_from_schema()
        content_box = ContentBox(box_type=get_assertion_content_box_type(self.type), payload=self.payload)

        super().__init__(content_type=get_assertion_content_type(self.type),
                         label=get_assertion_label(self.type),
                         content_boxes=[content_box])
                        
    