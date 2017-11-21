# -*- coding: utf-8 -*-

from nose.tools import assert_equals

from .. import parsers


def test_convert_hex_to_char():

    data = '41'
    expected = 'A'
    converted = parsers.convert_hex_to_char(data=data)
    assert_equals(expected, converted)
