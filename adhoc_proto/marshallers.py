# -*- coding: utf-8 -*-

import abc

import suitcase.exceptions

from . import models


class ByteToStructure(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def marshall(self):

        """
        Marshall the bytes into a structure.

        Returns
        -------
        suitcase.structure.Structure
        """

        raise NotImplementedError


class Header(ByteToStructure):

    def __init__(self, file):

        """
        Parameters
        ----------
        file : file
        """

        self._file = file

    def marshall(self):
        data = self._file.read(models.Header.LENGTH_BYTES)
        header = models.Header.from_data(data)
        return list(header)

    def __repr__(self):
        repr_ = '{}(file={})'
        return repr_.format(self.__class__.__name__, self._file)


class Record(ByteToStructure):

    def __init__(self, file):

        """
        Parameters
        ----------
        file : file
        """

        self._file = file

    def marshall(self):
        data = self._file.read(models.Record.LENGTH_BYTES)
        try:
            record = models.Record.from_data(data)
        except suitcase.exceptions.SuitcaseParseError:
            record = models.Record.from_data(
                data + self._file.read(models.Record.CONDITIONAL_LENGTH_BYTES))
        return record

    def __repr__(self):
        repr_ = '{}(file={})'
        return repr_.format(self.__class__.__name__, self._file)
