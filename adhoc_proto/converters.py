# -*- coding: utf-8 -*-

import abc

HEXADECIMAL = 16


class Converter(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def convert_hex_to_int(self, data):

        """
        Convert the data to a int.

        Parameters
        ----------
        data : typing.Sequence[str]
            Sequence of bytes each encoded in base 16 (hexadecimal). Its
            length is used to infer the size of the integer.

        Returns
        -------
        int
        """

        raise NotImplementedError


class BuiltIn(Converter):

    def convert_hex_to_int(self, data):
        return int(''.join(data), base=HEXADECIMAL)

    def __repr__(self):
        repr_ = '{}()'
        return repr_.format(self.__class__.__name__)
