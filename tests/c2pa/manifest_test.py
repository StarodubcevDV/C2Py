import pytest

from c2py.c2pa.manifest import Manifest
from c2py.jumbf_boxes.jumbf_content_types import jumbf_content_types

def test_create_manifest():

    test_manifest = Manifest()

    assert test_manifest != None
    assert test_manifest.claim == None
    assert test_manifest.claim_signature == None
    assert test_manifest.assertion_store == None


def test_create_manifest_with_jumb_base_type():

    test_manifest = Manifest()

    assert test_manifest.t_box == 'jumb'.encode('utf-8').hex()
    assert test_manifest.get_content_type() == jumbf_content_types["json"]
    assert test_manifest.description_box.label == ''

