# Content jumbf box class

from c2py.jumbf_boxes.box import Box
from c2py.utils.content_types import jumbf_content_types


class ContentBox(Box):

    def __init__(self, box_type='jumb'.encode('utf-8').hex(), payload = b''):
        super().__init__(box_type=box_type, payload=payload)
    