# -*- coding: utf-8 -*-

HEXADECIMAL = 16


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
    data : typing.Iterable[str]
        Sequence of bytes each encoded in base 16 (hexadecimal).

    Returns
    -------
    str
    """

    return ''.join(convert_hex_to_char(x) for x in data)
