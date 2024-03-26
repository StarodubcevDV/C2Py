# Content jumbf box class

from c2py.jumbf_boxes.box import Box
from c2py.jumbf_boxes.jumbf_content_types import jumbf_content_types

class ContentBox(Box):

    payload = b''

    def __init__(self, payload = b''):
        super().__init__('jumb'.encode('utf-8').hex())
        self.payload = payload
    