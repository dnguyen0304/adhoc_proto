# -*- coding: utf-8 -*-

from nose.tools import assert_equals

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
