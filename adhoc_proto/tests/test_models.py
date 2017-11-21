# -*- coding: utf-8 -*-

from nose.tools import assert_equals

from .. import models


def test_header_from_hex():

    data = ['4D', '50', '53', '37', '01', '00', '00', '00', '47']
    expected = 'Header(protocol="MPS7", version=1, length=71)'
    header = models.Header.from_hex(data=data)
    assert_equals(expected, str(header))
