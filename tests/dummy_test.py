import pytest


def test_lower():
    assert 'FOO'.lower() == 'foo'


def test_upper():
    assert 'foo'.upper() == 'FOO'