# -*- coding: utf-8 -*-

import math

from . import common


def calculate_debit_total(log):

    """
    Calculate the total amount of debits.

    The units are in dollars. The time complexity is O(n), where n
    is the number of records in the log.

    Parameters
    ----------
    log : typing.Sequence[adhoc_proto.models.Record]

    Returns
    -------
    float
    """

    return math.fsum(record.amount
                     for record
                     in log
                     if record.type == common.RecordType.DEBIT)


def calculate_credit_total(log):

    """
    Calculate the total amount of credit.

    The units are in dollars. The time complexity is O(n), where n
    is the number of records in the log.

    Parameters
    ----------
    log : typing.Sequence[adhoc_proto.models.Record]

    Returns
    -------
    float
    """

    return math.fsum(record.amount
                     for record
                     in log
                     if record.type == common.RecordType.CREDIT)
