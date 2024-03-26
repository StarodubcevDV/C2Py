import pytest

from c2py.jumbf_boxes.box import Box

def test_create_box():

    test_box = Box("jumb")

    assert test_box.t_box == "jumb"

def test_get_some_box_length():

    test_box = Box("jumb")

    assert test_box.get_length() != None

def test_get_true_box_length():

    test_box = Box("jumb")

    assert test_box.get_length() == 8

