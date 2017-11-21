# -*- coding: utf-8 -*-

import abc

from . import common

HEXADECIMAL = 16


# This implementation closely mirrors the one in the Python +3.2.
# abc.abstractclassmethod was not added until Python 3.2. It was then
# deprecated in Python 3.3 because being able to use classmethod and
# abc.abstractmethod together was added.
class abstractclassmethod(classmethod):

    __isabstractmethod__ = True

    def __init__(self, callable):
        callable.__isabstractmethod__ = True
        super(abstractclassmethod, self).__init__(callable)


class HexToModel(object):

    __metaclass__ = abc.ABCMeta

    @abstractclassmethod
    def from_hex(self, data):

        """
        Parse the data.

        Parameters
        ----------
        data : typing.Sequence[str]
            Sequence of bytes each encoded in base 16 (hexadecimal).

        Returns
        -------
        adhoc_proto.models.Model
        """

        raise NotImplementedError


def convert_hex_to_int(data):

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


def convert_hex_to_char(data):

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


def convert_hex_to_str(data):

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

    return ''.join(convert_hex_to_char(x) for x in data)


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
