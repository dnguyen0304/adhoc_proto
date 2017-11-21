# -*- coding: utf-8 -*-

import abc

from . import parsers


class Model(object):

    __metaclass__ = abc.ABCMeta


class Header(Model, parsers.HexToModel):

    def __init__(self, protocol, version, length):

        """
        Parameters
        ----------
        protocol : str
        version : int
        length : int
            Count of records.
        """

        self._protocol = protocol
        self._version = version
        self._length = length

    @classmethod
    def from_hex(cls, data):
        protocol = parsers.convert_hex_to_str(data=data[:4])
        version = parsers.convert_hex_to_int(data=data[4])
        length = parsers.convert_hex_to_int(data=data[5:9])
        return Header(protocol=protocol,
                      version=version,
                      length=length)

    def __repr__(self):
        repr_ = '{}(protocol="{}", version={}, length={})'
        return repr_.format(self.__class__.__name__,
                            self._protocol,
                            self._version,
                            self._length)
