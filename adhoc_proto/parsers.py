# -*- coding: utf-8 -*-

import abc

HEXADECIMAL = 16


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
    Convert the data to string.

    Parameters
    ----------
    data : typing.Iterable[str]
        Sequence of bytes each encoded in base 16 (hexadecimal).

    Returns
    -------
    str
    """

    return ''.join(convert_hex_to_char(x) for x in data)


class HexToType(object):

    def __init__(self, _convert_hex_to_str=convert_hex_to_str):
        self._convert_hex_to_str = _convert_hex_to_str

    def parse(self, data):

        """
        Parse the data.

        Parameters
        ----------
        data : typing.Iterable[str]
            Sequence of bytes each encoded in base 16 (hexadecimal).

        Returns
        -------
        str
        """

        return self._convert_hex_to_str(data=data)

    def __repr__(self):
        repr_ = '{}()'
        return repr_.format(self.__class__.__name__)
