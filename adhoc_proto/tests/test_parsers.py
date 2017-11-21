# -*- coding: utf-8 -*-

from nose.tools import assert_equals

from .. import common
from .. import parsers


def test_convert_hex_to_int_single_byte():

    data = ['00']
    expected = 0
    converted = parsers.convert_hex_to_int(data=data)
    assert_equals(expected, converted)


def test_convert_hex_to_int_multiple_bytes():

    data = ['A', 'A']
    expected = 170
    converted = parsers.convert_hex_to_int(data=data)
    assert_equals(expected, converted)


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


def test_convert_hex_to_record_type():

    data = '00'
    expected = common.RecordType.DEBIT
    converted = parsers.convert_hex_to_record_type(data=data)
    assert_equals(expected, converted)
