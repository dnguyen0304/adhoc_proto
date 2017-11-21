# -*- coding: utf-8 -*-

import abc

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
