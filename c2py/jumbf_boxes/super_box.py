# Jumbf super box class

from c2py.jumbf_boxes.box import Box
from c2py.jumbf_boxes.description_box import DescriptionBox
from c2py.jumbf_boxes.jumbf_content_types import jumbf_content_types


class SuperBox(Box):

    description_box = None
    content_boxes = []

    def __init__(self, content_type = jumbf_content_types["json"], label=''):
        super().__init__('jumb'.encode('utf-8').hex())
        self.description_box = DescriptionBox(content_type=content_type, label=label)
