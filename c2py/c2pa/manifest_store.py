
from c2py.jumbf_boxes.super_box import SuperBox
from c2py.utils.assertion_schemas import C2PA_AssertionTypes
from c2py.utils.content_types import c2pa_content_types

JPEG_SEGMENT_MAX_PAYLOAD_LENGTH = 65517


class ManifestStore(SuperBox):

    def __init__(self, manifests=None):
        self.manifests = [] if manifests == None else manifests
        super().__init__(content_type=c2pa_content_types['manifest_store'], label='c2pa', content_boxes=manifests)
    
    
    def get_serialized_length(self):
        return self.get_length() + 2 + (10 * (self.get_length() // JPEG_SEGMENT_MAX_PAYLOAD_LENGTH + 1))
    
    
    def set_hash_data_length(self):
        for manifest_id in range(len(self.manifests)):
            print(f'OLOLO manifest id: {manifest_id}')
            self.manifests[manifest_id].set_hash_data_length(self.get_serialized_length())
            # print(f'changed length: {self.manifests[manifest_id].assertion_store.assertions[1].schema['exclusions'][0]['length']}')                   
        self.sync_payload()
        
    
    def serialize(self):
        self.set_hash_data_length()
        return super().serialize()
    