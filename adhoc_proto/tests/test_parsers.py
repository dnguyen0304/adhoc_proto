# -*- coding: utf-8 -*-

from nose.tools import assert_equals

from .. import parsers


def test_convert_hex_to_char():

    data = '41'
    expected = 'A'
    converted = parsers.convert_hex_to_char(data=data)
    assert_equals(expected, converted)


def test_convert_hex_to_str():

    data = ['66', '6F', '6F']
    expected = 'foo'
    converted = parsers.convert_hex_to_str(data=data)
    assert_equals(expected, converted)


def test_hex_to_type_parse():

    data = ['4D', '50', '53', '37']
    expected = 'MPS7'
    parsed = parsers.HexToType().parse(data=data)
    assert_equals(expected, parsed)
