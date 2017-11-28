# -*- coding: utf-8 -*-

import struct

from . import common

HEXADECIMAL = 16

BIG_ENDIAN = '>'
DOUBLE = 'd'


class BuiltIn(object):

    @classmethod
    def convert_hex_to_int(cls, data):

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

        return int(''.join(data), base=HEXADECIMAL)

    @classmethod
    def convert_hex_to_char(cls, data):

        """
        Convert the data to a character.

        Parameters
        ----------
        data : str
            Byte encoded in base 16 (hexadecimal).

        Returns
        -------
        str
        """

        return chr(int(data, base=HEXADECIMAL))

    def convert_hex_to_str(self, data):

        """
        Convert the data to a string.

        Parameters
        ----------
        data : typing.Sequence[str]
            Sequence of bytes each encoded in base 16 (hexadecimal).

        Returns
        -------
        str
        """

        return ''.join(self.convert_hex_to_char(x) for x in data)

    @staticmethod
    def convert_hex_to_double(data):
        return struct.unpack(BIG_ENDIAN + DOUBLE, data)[0]

    @staticmethod
    def convert_hex_to_record_type(data):

        """
        Convert the data to a RecordType.

        The time complexity is O(1).

        Parameters
        ----------
        data : str
            Byte encoded in base 16 (hexadecimal).

        Returns
        -------
        adhoc_proto.common.RecordType
        """

        mapping = {
            '': common.RecordType.DEBIT,
            '1': common.RecordType.CREDIT,
            '2': common.RecordType.START_AUTO_PAY,
            '3': common.RecordType.END_AUTO_PAY
        }
        return mapping[data.lstrip('0')]

    def __repr__(self):
        repr_ = '{}()'
        return repr_.format(self.__class__.__name__)
