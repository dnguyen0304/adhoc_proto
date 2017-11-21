# -*- coding: utf-8 -*-

from nose.tools import assert_equals

from .. import common
from .. import models
from .. import parsers


def test_header_from_data():

    #      'MPS7\x01\x00\x00\x00\x47'
    data = 'MPS7\x01\x00\x00\x00G'
    expected = models.Header()
    # expected.protocol is a magic string.
    expected.version = 1
    expected.record_count = 71

    header = models.Header.from_data(data=data)

    assert_equals(expected.protocol, header.protocol)
    assert_equals(expected.version, header.version)
    assert_equals(expected.record_count, header.record_count)


def test_record_from_data():

    #         \x00\x53\x09\x27\xD1\x39\x67\x47\xC0\x45\xD9\x91\x21
    data = """\x00S\t'\xd19gG\xc0E\xd9\x91!"""
    expected = models.Record()
    expected.type = common.RecordType.DEBIT
    expected.timestamp = parsers.convert_hex_to_int(data[1:5].encode('hex'))
    expected.users_id = parsers.convert_hex_to_int(data[5:13].encode('hex'))

    record = models.Record.from_data(data=data)

    assert_equals(expected.type, record.type)
    assert_equals(expected.timestamp, record.timestamp)
    assert_equals(expected.users_id, record.users_id)
