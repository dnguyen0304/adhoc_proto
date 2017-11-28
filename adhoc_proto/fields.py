# -*- coding: utf-8 -*-

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
