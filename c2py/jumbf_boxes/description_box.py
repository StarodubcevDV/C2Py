# Description jumbf box class

from c2py.jumbf_boxes.box import Box
from c2py.jumbf_boxes.jumbf_content_types import jumbf_content_types

class DescriptionBox(Box):

    content_type = ''
    label = ''
    toggle = ''

    def __init__(self, content_type = jumbf_content_types["json"], label=''):
        self.label = label
        self.content_type = content_type
        self.toggle = 3

        self.payload = self.content_type + \
                        self.toggle.to_bytes(1, 'big') + \
                        bytes.fromhex(self.label.encode('utf-8').hex()) + \
                        b'\x00'
        
        super().__init__('jumd'.encode('utf-8').hex())
    