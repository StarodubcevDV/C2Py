import pytest

from c2py.c2pa.assertion import Assertion
from c2py.utils.content_types import jumbf_content_types
from c2py.utils.assertion_schemas import C2PA_AssertionTypes

def test_create_assertion():

    test_assertion = Assertion(C2PA_AssertionTypes.creative_work, {})

    assert test_assertion != None


def test_create_assertion_with_jumbf_type():

    test_assertion = Assertion(C2PA_AssertionTypes.creative_work, {})
    assert test_assertion.t_box == 'jumb'.encode('utf-8').hex()
    assert test_assertion.get_content_type() == jumbf_content_types["json"]
    


def test_create_assertion_with_correct_label():
    test_assertion = Assertion(C2PA_AssertionTypes.creative_work, {})
    assert test_assertion.get_label() == 'stds.schema-org.CreativeWork'


def test_create_assertion_with_true_type():

    test_assertion = Assertion(C2PA_AssertionTypes.creative_work, {})

    assert test_assertion.type == C2PA_AssertionTypes.creative_work


def test_create_assertion_with_correct_schema():

    creative_work_schema = {
        "@context": "https://schema.org",
        "@type": "CreativeWork",
        "author": [
            {
                "@type": "Person",
                "name": "Dmitriy Starodubtcev"
            }
        ],
        "copyrightYear": "2024",
        "copyrightHolder": "c2py"
    }

    test_assertion = Assertion(C2PA_AssertionTypes.creative_work, creative_work_schema)

    assert test_assertion.schema == creative_work_schema
