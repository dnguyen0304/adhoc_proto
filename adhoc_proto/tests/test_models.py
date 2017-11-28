# -*- coding: utf-8 -*-

from nose.tools import assert_equals, assert_true

from .. import common
from .. import converters
from .. import models


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


def test_is_debit_record():

    record = models.Record()
    record.type = common.RecordType.DEBIT

    assert_true(models._is_debit_record(record))


def test_is_credit_record():

    record = models.Record()
    record.type = common.RecordType.CREDIT

    assert_true(models._is_credit_record(record))


def test_record_with_amount_from_data():

    converter = converters.BuiltIn()

    #         \x00\x53\x09\x27\xD1\x39\x67\x47\xC0\x45\xD9\x91\x21\x40\x82\xE2\x31\xD6\xD7\x2E\x8D
    data = """\x00S\t'\xd19gG\xc0E\xd9\x91!@\x82\xe21\xd6\xd7.\x8d"""
    expected = models.Record()
    expected.type = common.RecordType.DEBIT
    expected.timestamp = converter.convert_hex_to_int(data[1:5].encode('hex'))
    expected.users_id = converter.convert_hex_to_int(data[5:13].encode('hex'))
    expected.amount = converter.convert_hex_to_double(data[13:21].encode('hex'))

    record = models.Record.from_data(data=data)

    assert_equals(expected.type, record.type)
    assert_equals(expected.timestamp, record.timestamp)
    assert_equals(expected.users_id, record.users_id)
    assert_equals(expected.amount, record.amount)


def test_record_without_amount_from_data():

    converter = converters.BuiltIn()

    #         \x02\x53\x09\x27\xD1\x39\x67\x47\xC0\x45\xD9\x91\x21
    data = """\x02S\t'\xd19gG\xc0E\xd9\x91!"""
    expected = models.Record()
    expected.type = common.RecordType.START_AUTO_PAY
    expected.timestamp = converter.convert_hex_to_int(data[1:5].encode('hex'))
    expected.users_id = converter.convert_hex_to_int(data[5:13].encode('hex'))

    record = models.Record.from_data(data=data)

    assert_equals(expected.type, record.type)
    assert_equals(expected.timestamp, record.timestamp)
    assert_equals(expected.users_id, record.users_id)
    assert_equals(expected.amount, record.amount)
