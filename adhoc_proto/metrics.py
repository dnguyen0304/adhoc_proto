# -*- coding: utf-8 -*-

import math

from . import common


def calculate_debit_sum(records):

    """
    Calculate the total amount of debits.

    The units are in dollars. The time complexity is O(n), where n
    is the number of records in the log.

    Parameters
    ----------
    records : typing.Sequence[adhoc_proto.models.Record]

    Returns
    -------
    float
    """

    return math.fsum(record.amount
                     for record
                     in records
                     if record.type == common.RecordType.DEBIT)


def calculate_credit_sum(records):

    """
    Calculate the total amount of credit.

    The units are in dollars. The time complexity is O(n), where n
    is the number of records in the log.

    Parameters
    ----------
    records : typing.Sequence[adhoc_proto.models.Record]

    Returns
    -------
    float
    """

    return math.fsum(record.amount
                     for record
                     in records
                     if record.type == common.RecordType.CREDIT)


def calculate_auto_pay_started_count(records):

    """
    Calculate the total number of auto pays started.

    The time complexity is O(n), where n is the number of records in the
    log.

    Parameters
    ----------
    records : typing.Sequence[adhoc_proto.models.Record]

    Returns
    -------
    int
    """

    return sum(1
               for record
               in records
               if record.type == common.RecordType.START_AUTO_PAY)


def calculate_auto_pay_ended_count(records):

    """
    Calculate the total number of auto pays ended.

    The time complexity is O(n), where n is the number of records in the
    log.

    Parameters
    ----------
    records : typing.Sequence[adhoc_proto.models.Record]

    Returns
    -------
    int
    """

    return sum(1
               for record
               in records
               if record.type == common.RecordType.END_AUTO_PAY)


def calculate_balance_sum(records, users_id):

    """
    Calculate the total balance for a user.

    The time complexity is O(n), where n is the number of records in
    the log.

    Parameters
    ----------
    records : typing.Sequence[adhoc_proto.models.Record]
    users_id : int

    Returns
    -------
    int
    """

    def helper():
        for record in records:
            if record.users_id != users_id:
                continue
            if record.type == common.RecordType.DEBIT:
                # Debits remove money from an account
                yield -record.amount
            if record.type == common.RecordType.CREDIT:
                # Credits add money to an account.
                yield record.amount

    return sum(helper())
