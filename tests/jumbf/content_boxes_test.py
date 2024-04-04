import pytest

from c2py.jumbf_boxes.content_box import ContentBox
from c2py.utils.content_types import jumbf_content_types


def test_create_content_box():

    test_content_box = ContentBox()

    assert test_content_box.t_box == 'jumb'.encode('utf-8').hex()


def test_create_content_box_with_payload():

    test_content_box = ContentBox(payload=b'0000')

    assert test_content_box.payload == b'0000'


def test_serialize_content_box():

    test_content_box = ContentBox(payload=b'\x00\x00')

    test_content_box_serialized_data = b'\x6a\x75\x6d\x62' + \
                                        b'\x00\x00\x00\x0A' + \
                                        b'\x00\x00'

    assert test_content_box.serialize() == test_content_box_serialized_data

