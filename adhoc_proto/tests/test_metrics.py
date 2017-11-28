# -*- coding: utf-8 -*-

from nose.tools import assert_equals

from .. import common
from .. import metrics
from .. import models


class TestCalculateDebitSum(object):

    def __init__(self):
        self.log = None
        self.expected = None

    def setup(self):
        self.log = list()
        self.expected = 4.0

        record_1 = models.Record()
        record_2 = models.Record()
        record_1.type = common.RecordType.DEBIT
        record_2.type = common.RecordType.DEBIT
        record_1.amount = 2.0
        record_2.amount = 2.0

        self.log.append(record_1)
        self.log.append(record_2)

    def test_sum(self):
        debit_sum = metrics.calculate_debit_sum(log=self.log)
        assert_equals(self.expected, debit_sum)

    def test_filter(self):
        record_3 = models.Record()
        record_3.type = common.RecordType.START_AUTO_PAY
        record_3.amount = 2.0

        self.log.append(record_3)

        debit_sum = metrics.calculate_debit_sum(log=self.log)
        assert_equals(self.expected, debit_sum)


class TestCalculateCreditSum(object):

    def __init__(self):
        self.log = None
        self.expected = None

    def setup(self):
        self.log = list()
        self.expected = 4.0

        record_1 = models.Record()
        record_2 = models.Record()
        record_1.type = common.RecordType.CREDIT
        record_2.type = common.RecordType.CREDIT
        record_1.amount = 2.0
        record_2.amount = 2.0

        self.log.append(record_1)
        self.log.append(record_2)

    def test_sum(self):
        credit_sum = metrics.calculate_credit_sum(log=self.log)
        assert_equals(self.expected, credit_sum)

    def test_filter(self):
        record_3 = models.Record()
        record_3.type = common.RecordType.START_AUTO_PAY
        record_3.amount = 2.0

        self.log.append(record_3)

        credit_sum = metrics.calculate_credit_sum(log=self.log)
        assert_equals(self.expected, credit_sum)


class TestCalculateAutoPayStartedCount(object):

    def __init__(self):
        self.log = None
        self.expected = None

    def setup(self):
        self.log = list()

        record_1 = models.Record()
        record_2 = models.Record()
        record_1.type = common.RecordType.START_AUTO_PAY
        record_2.type = common.RecordType.START_AUTO_PAY

        self.log.append(record_1)
        self.log.append(record_2)
        self.expected = len(self.log)

    def test_count(self):
        auto_pay_started_count = metrics.calculate_auto_pay_started_count(
            log=self.log)
        assert_equals(self.expected, auto_pay_started_count)

    def test_filter(self):
        record_3 = models.Record()
        record_3.type = common.RecordType.END_AUTO_PAY

        self.log.append(record_3)

        auto_pay_started_count = metrics.calculate_auto_pay_started_count(
            log=self.log)
        assert_equals(self.expected, auto_pay_started_count)


class TestCalculateAutoPayEndedCount(object):

    def __init__(self):
        self.log = None
        self.expected = None

    def setup(self):
        self.log = list()

        record_1 = models.Record()
        record_2 = models.Record()
        record_1.type = common.RecordType.END_AUTO_PAY
        record_2.type = common.RecordType.END_AUTO_PAY

        self.log.append(record_1)
        self.log.append(record_2)
        self.expected = len(self.log)

    def test_count(self):
        auto_pay_ended_count = metrics.calculate_auto_pay_ended_count(
            log=self.log)
        assert_equals(self.expected, auto_pay_ended_count)

    def test_filter(self):
        record_3 = models.Record()
        record_3.type = common.RecordType.START_AUTO_PAY

        self.log.append(record_3)

        auto_pay_ended_count = metrics.calculate_auto_pay_ended_count(
            log=self.log)
        assert_equals(self.expected, auto_pay_ended_count)


class TestCalculateBalanceSum(object):

    def __init__(self):
        self.log = None
        self.users_id = None
        self.expected = None

    def setup(self):
        self.log = list()
        self.users_id = 1

        record_1 = models.Record()
        record_2 = models.Record()
        record_1.type = common.RecordType.DEBIT
        record_2.type = common.RecordType.CREDIT
        record_1.users_id = self.users_id
        record_2.users_id = self.users_id
        record_1.amount = 4.0
        record_2.amount = 2.0

        self.log.append(record_1)
        self.log.append(record_2)
        self.expected = -record_1.amount + record_2.amount

    def test_sum(self):
        balance_sum = metrics.calculate_balance_sum(
            log=self.log,
            users_id=self.users_id)
        assert_equals(self.expected, balance_sum)

    def test_filter_users_id(self):
        record_3 = models.Record()
        record_3.type = common.RecordType.DEBIT
        record_3.users_id = self.users_id + 1
        record_3.amount = 2.0

        self.log.append(record_3)

        balance_sum = metrics.calculate_balance_sum(
            log=self.log,
            users_id=self.users_id)
        assert_equals(self.expected, balance_sum)

    def test_filter_record_type(self):
        record_3 = models.Record()
        record_3.type = common.RecordType.START_AUTO_PAY
        record_3.users_id = self.users_id
        record_3.amount = 2.0

        self.log.append(record_3)

        balance_sum = metrics.calculate_balance_sum(
            log=self.log,
            users_id=self.users_id)
        assert_equals(self.expected, balance_sum)
