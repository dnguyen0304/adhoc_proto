# -*- coding: utf-8 -*-

from nose.tools import assert_equals

from .. import converters


class TestBuiltIn(object):

    def __init__(self):
        self.converter = None

    def setup(self):
        self.converter = converters.BuiltIn()

    def test_convert_hex_to_int_single_byte(self):
        data = ['00']
        expected = 0
        converted = self.converter.convert_hex_to_int(data=data)
        assert_equals(expected, converted)

    def test_convert_hex_to_int_multiple_bytes(self):
        data = ['00', '00', '00', '47']
        expected = 71
        converted = self.converter.convert_hex_to_int(data=data)
        assert_equals(expected, converted)
