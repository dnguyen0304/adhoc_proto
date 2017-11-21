# -*- coding: utf-8 -*-

import suitcase.structure
from suitcase.fields import (FieldProperty,
                             Magic,
                             UBInt8,
                             UBInt32,
                             UBInt64)

from . import common

PROTOCOL_NAME = 'MPS7'


class Header(suitcase.structure.Structure):

    protocol = Magic(expected_sequence=PROTOCOL_NAME)
    version = UBInt8()
    record_count = UBInt32()


class Record(suitcase.structure.Structure):

    _RECORD_TYPE_MAPPING = {
        0x00: common.RecordType.DEBIT,
        0x01: common.RecordType.CREDIT,
        0x02: common.RecordType.START_AUTO_PAY,
        0x03: common.RecordType.END_AUTO_PAY
    }

    _type = UBInt8()
    timestamp = UBInt32()
    users_id = UBInt64()

    type = FieldProperty(field=_type,
                         onget=lambda x: Record._RECORD_TYPE_MAPPING[x])
