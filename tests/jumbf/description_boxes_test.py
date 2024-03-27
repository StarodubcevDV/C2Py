import pytest

from c2py.jumbf_boxes.description_box import DescriptionBox
from c2py.jumbf_boxes.jumbf_content_types import jumbf_content_types

def test_create_box():

    test_description_box = DescriptionBox()

    assert test_description_box.t_box == 'jumd'.encode('utf-8').hex()

def test_create_box_with_label():

    test_description_box = DescriptionBox(label="test")

    assert test_description_box.label == "test"

def test_create_box_with_content_type():

    test_description_box = DescriptionBox(content_type=jumbf_content_types["json"])

    assert test_description_box.content_type == jumbf_content_types["json"]

def test_create_box_with_toggle():

    test_description_box = DescriptionBox()

    assert test_description_box.toggle == 3

def test_check_length():

    test_description_box = DescriptionBox()

    assert test_description_box.get_length() == 8