# Description jumbf box class

from c2py.jumbf_boxes.box import Box
from c2py.utils.content_types import jumbf_content_types


class DescriptionBox(Box):

    def __init__(self, content_type = jumbf_content_types["json"], label=''):
        self.label = label
        self.content_type = content_type
        self.toggle = 3

        payload = self.content_type + \
                        self.toggle.to_bytes(1, 'big') + \
                        self.label.encode('utf-8') + \
                        b'\x00'
        
        super().__init__('jumd'.encode('utf-8').hex(), payload=payload)

    
    def get_label(self):
        return self.label
    
    def get_content_type(self):
        return self.content_type
    