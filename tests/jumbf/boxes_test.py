import pytest

from c2py.jumbf_boxes.box import Box

def test_create_box():

    test_box = Box('jumb'.encode('utf-8').hex())

    assert test_box.t_box == 'jumb'.encode('utf-8').hex()

def test_get_some_box_length():

    test_box = Box('jumb'.encode('utf-8').hex())

    assert test_box.get_length() != None

def test_get_true_box_length():

    test_box = Box('jumb'.encode('utf-8').hex())

    assert test_box.get_length() == 8

