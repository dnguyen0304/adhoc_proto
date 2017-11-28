# -*- coding: utf-8 -*-

import StringIO

from nose.tools import assert_is_none

from .. import marshallers
from .. import models


def test_bytes_to_header_marshall_eof():

    buffer = ''.join(' ' for _ in xrange(models.Header.LENGTH_BYTES - 1))
    file = StringIO.StringIO(buffer)
    marshaller = marshallers.BytesToHeader(file=file)
    header = marshaller.marshall()

    assert_is_none(header)
