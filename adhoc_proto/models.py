# -*- coding: utf-8 -*-

import suitcase.structure
from suitcase.fields import (ConditionalField,
                             FieldProperty,
                             Magic,
                             UBInt8,
                             UBInt32,
                             UBInt64)

from . import common
from . import fields

PROTOCOL_NAME = 'MPS7'


class Header(suitcase.structure.Structure):

    LENGTH_BYTES = 9

    protocol = Magic(expected_sequence=PROTOCOL_NAME)
    version = UBInt8()
    record_count = UBInt32()


def _is_debit_record(record):

    """
    Assert the record is a debit record.

    Parameters
    ----------
    record : adhoc_proto.models.Record

    Returns
    -------
    bool
    """

    return record.type == common.RecordType.DEBIT


def _is_credit_record(record):

    """
    Assert the record is a credit record.

    Parameters
    ----------
    record : adhoc_proto.models.Record

    Returns
    -------
    bool
    """

    return record.type == common.RecordType.CREDIT


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
    # suitcase.fields.ConditionalField requires a condition argument,
    # which is a callable that accepts a suitcase.structure.Structure
    # (adhoc_proto.models.Record in this case) and returns a boolean.
    amount = ConditionalField(
        field=fields.SBFloat64(),
        condition=lambda x: _is_debit_record(x) or _is_credit_record(x))

    type = FieldProperty(field=_type,
                         onget=lambda x: Record._RECORD_TYPE_MAPPING[x])
