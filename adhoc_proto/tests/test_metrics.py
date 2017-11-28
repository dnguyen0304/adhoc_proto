# -*- coding: utf-8 -*-

from nose.tools import assert_equals

from .. import common
from .. import metrics
from .. import models


class TestCalculateDebitTotal(object):

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
        debit_total = metrics.calculate_debit_total(log=self.log)
        assert_equals(self.expected, debit_total)

    def test_filter(self):
        record_3 = models.Record()
        record_3.type = common.RecordType.START_AUTO_PAY
        record_3.amount = 2.0

        self.log.append(record_3)

        debit_total = metrics.calculate_debit_total(log=self.log)
        assert_equals(self.expected, debit_total)


class TestCalculateCreditTotal(object):

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
        credit_total = metrics.calculate_credit_total(log=self.log)
        assert_equals(self.expected, credit_total)

    def test_filter(self):
        record_3 = models.Record()
        record_3.type = common.RecordType.START_AUTO_PAY
        record_3.amount = 2.0

        self.log.append(record_3)

        credit_total = metrics.calculate_credit_total(log=self.log)
        assert_equals(self.expected, credit_total)
