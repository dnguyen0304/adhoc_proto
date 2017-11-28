# -*- coding: utf-8 -*-

import struct

from suitcase.fields import BaseStructField


# As of November 27, 2017, this change has not been released yet.
#
# Links
# [1] https://github.com/digidotcom/python-suitcase/pull/46
class SBFloat32(BaseStructField):
    """Signed Big Endian 32-bit float field."""
    PACK_FORMAT = UNPACK_FORMAT = b">f"


class SBFloat64(BaseStructField):
    """Signed Big Endian 64-bit float field."""
    PACK_FORMAT = UNPACK_FORMAT = b">d"

    # As of November 27, 2017, the default implementation of unpack in
    # suitcase.fields.BaseStructField does not support floats.
    def unpack(self, data, **kwargs):
        self._value = struct.unpack(self.UNPACK_FORMAT, data)[0]
