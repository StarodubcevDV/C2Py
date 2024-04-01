import pytest

from c2py.c2pa.manifest import Manifest

def test_create_manifest():

    test_manifest = Manifest()

    assert test_manifest != None