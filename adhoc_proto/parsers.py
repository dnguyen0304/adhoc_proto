# -*- coding: utf-8 -*-

import abc


class HexToModel(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def parse(self, data):

        """
        Parse the data.

        Parameters
        ----------
        data : typing.Iterable[str]
            Sequence of bytes each encoded in base 16 (hexadecimal).

        Returns
        -------
        adhoc_proto.models.Model
        """

        pass
