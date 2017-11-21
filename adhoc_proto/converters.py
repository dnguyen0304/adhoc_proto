# -*- coding: utf-8 -*-


class BuiltIn(object):

    _HEXADECIMAL = 16

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

        return int(''.join(data), base=self._HEXADECIMAL)

    def __repr__(self):
        repr_ = '{}()'
        return repr_.format(self.__class__.__name__)
