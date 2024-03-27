import pytest

from c2py.jumbf_boxes.super_box import SuperBox
from c2py.jumbf_boxes.jumbf_content_types import jumbf_content_types


def test_create_super_box():

    test_super_box = SuperBox()

    assert test_super_box.t_box == 'jumb'.encode('utf-8').hex()

def test_create_super_box_with_description_box():

    test_super_box = SuperBox()

    assert test_super_box.description_box != None

def test_create_super_box_with_cbor_content_type():

    test_super_box = SuperBox(content_type=jumbf_content_types['cbor'])

    assert test_super_box.description_box.content_type == jumbf_content_types['cbor']

def test_create_super_box_with_label():

    test_super_box = SuperBox(label="c2pa.Test")

    assert test_super_box.description_box.label == "c2pa.Test"

def test_create_super_box_with_content_boxes():

    test_super_box = SuperBox()

    assert len(test_super_box.content_boxes) == 0 

