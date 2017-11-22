# -*- coding: utf-8 -*-

from nose.tools import assert_equals

from .. import common
from .. import converters


class TestBuiltIn(object):

    def __init__(self):
        self.converter = None

    def setup(self):
        self.converter = converters.BuiltIn()

    def test_convert_hex_to_int_single_byte(self):
        expected = 0
        data = '0'
        converted = self.converter.convert_hex_to_int(data=data)
        assert_equals(expected, converted)

    def test_convert_hex_to_int_multiple_bytes(self):
        expected = 71
        data = hex(expected).lstrip('0x')
        converted = self.converter.convert_hex_to_int(data=data)
        assert_equals(expected, converted)

    def test_convert_hex_to_char(self):
        expected = 'A'
        data = hex(ord(expected)).lstrip('0x')
        converted = self.converter.convert_hex_to_char(data=data)
        assert_equals(expected, converted)

    def test_convert_hex_to_str(self):
        expected = 'foo'
        data = (hex(ord(char)).lstrip('0x') for char in expected)
        converted = self.converter.convert_hex_to_str(data=data)
        assert_equals(expected, converted)

    def test_convert_hex_to_record_type(self):
        data = '00'
        expected = common.RecordType.DEBIT
        converted = self.converter.convert_hex_to_record_type(data=data)
        assert_equals(expected, converted)
