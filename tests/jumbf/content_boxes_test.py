import pytest

from c2py.jumbf_boxes.content_box import ContentBox
from c2py.jumbf_boxes.jumbf_content_types import jumbf_content_types

def test_create_box():

    test_content_box = ContentBox()

    assert test_content_box.t_box == 'jumb'.encode('utf-8').hex()


def test_create_box_with_payload():

    test_content_box = ContentBox(payload=b'0000')

    assert test_content_box.payload == b'0000'
