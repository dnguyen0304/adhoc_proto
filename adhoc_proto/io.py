# -*- coding: utf-8 -*-

import abc

from . import models


class Reader(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def read(self):

        """
        Read the source into a sequence.

        Returns
        -------
        typing.Sequence
        """

        raise NotImplementedError


class Header(Reader):

    def __init__(self, file):

        """
        Parameters
        ----------
        file : file
        """

        self._file = file

    def read(self):
        data = self._file.read(models.Header.LENGTH_BYTES)
        header = models.Header.from_data(data)
        return list(header)

    def __repr__(self):
        repr_ = '{}(file={})'
        return repr_.format(self.__class__.__name__, self._file)
