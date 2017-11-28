# -*- coding: utf-8 -*-

from __future__ import print_function

from adhoc_proto import marshallers
from adhoc_proto import metrics


class Application(object):

    def __init__(self, log_marshaller, users_id):

        """
        Parameters
        ----------
        log_marshaller : adhoc_proto.marshallers.BytesToLog
        users_id : int
        """

        self._log_marshaller = log_marshaller
        self._users_id = users_id

    def start(self):

        """
        Start the application.
        """

        log = self._log_marshaller.marshall()
        records = log[1:]

        print('The total amount of debits is {} dollars.'.format(
            metrics.calculate_debit_sum(records=records)))
        print('The total amount of credits is {} dollars.'.format(
            metrics.calculate_credit_sum(records=records)))
        print('The total number of auto pays started is {}.'.format(
            metrics.calculate_auto_pay_started_count(records=records)))
        print('The total number of auto pays ended is {}.'.format(
            metrics.calculate_auto_pay_ended_count(records=records)))
        print('The total balance for user {} is {} dollars.'.format(
            self._users_id,
            metrics.calculate_balance_sum(records=records,
                                          users_id=self._users_id)))

    def __repr__(self):
        repr_ = '{}(log_marshaller={}, users_id={})'
        return repr_.format(self.__class__.__name__,
                            self._log_marshaller,
                            self._users_id)


def main():

    # Set the configuration.
    path = './data/txnlog.dat'
    users_id = 2456938384156277127

    # Create the file.
    file = open(path, 'rb')

    # Create the log marshaller.
    log_marshaller = marshallers.BytesToLog(
        header_marshaller=marshallers.BytesToHeader(file=file),
        record_marshaller=marshallers.BytesToRecord(file=file))

    # Create the application.
    application = Application(log_marshaller=log_marshaller, users_id=users_id)

    try:
        application.start()
    finally:
        # Dispose of the file.
        file.close()


if __name__ == '__main__':
    main()
