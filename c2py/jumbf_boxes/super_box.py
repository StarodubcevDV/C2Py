# Jumbf super box class

from c2py.jumbf_boxes.box import Box
from c2py.jumbf_boxes.description_box import DescriptionBox
from c2py.utils.content_types import jumbf_content_types


class SuperBox(Box):

    def __init__(self, content_type=jumbf_content_types["json"], label='', content_boxes=None):
        self.description_box = DescriptionBox(content_type=content_type, label=label)
        self.content_boxes = [] if content_boxes == None else content_boxes

        payload = self.description_box.serialize() + self.serialize_content_boxes()
        super().__init__('jumb'.encode('utf-8').hex(), payload=payload)

    
    def add_content_box(self, content_box):
        self.content_boxes.append(content_box)
        self.sync_payload()


    def serialize_content_boxes(self):
        serialized_content_boxes = b''
        
        for content_box in self.content_boxes:
            if content_box != None:
                serialized_content_boxes += content_box.serialize()

        return serialized_content_boxes
    

    def sync_payload(self):
        self.payload = self.description_box.serialize() + self.serialize_content_boxes()
        super().__init__('jumb'.encode('utf-8').hex(), payload=self.payload)

    
    def get_label(self):
        return self.description_box.get_label()
    
    
    def get_content_type(self):
        return self.description_box.get_content_type()

