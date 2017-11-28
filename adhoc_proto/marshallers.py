# -*- coding: utf-8 -*-

import abc

import suitcase.exceptions

from . import models


class BytesToStructure(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def marshall(self):

        """
        Marshall the bytes into a structure.

        Returns
        -------
        suitcase.structure.Structure
        """

        raise NotImplementedError


class BytesToStructures(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def marshall(self):

        """
        Marshall the bytes into a collection of structures.

        Returns
        -------
        typing.Sequence[suitcase.structure.Structure]
        """

        raise NotImplementedError


class BytesToHeader(BytesToStructure):

    def __init__(self, file):

        """
        Parameters
        ----------
        file : file
        """

        self._file = file

    def marshall(self):

        """
        The time complexity is O(n), where n is the number of bytes
        being read.

        Returns
        -------
        adhoc_proto.models.Header
        """

        data = self._file.read(models.Header.LENGTH_BYTES)
        if len(data) < models.Header.LENGTH_BYTES:
            header = None
        else:
            header = models.Header.from_data(data)
        return header

    def __repr__(self):
        repr_ = '{}(file={})'
        return repr_.format(self.__class__.__name__, self._file)


class BytesToRecord(BytesToStructure):

    def __init__(self, file):

        """
        Parameters
        ----------
        file : file
        """

        self._file = file

    def marshall(self):

        """
        The time complexity is O(n), where n is the number of bytes
        being read.

        Returns
        -------
        adhoc_proto.models.Record
        """

        data = self._file.read(models.Record.LENGTH_BYTES)
        if len(data) < models.Record.LENGTH_BYTES:
            return None
        try:
            record = models.Record.from_data(data)
        except suitcase.exceptions.SuitcaseParseError:
            record = models.Record.from_data(
                data + self._file.read(models.Record.CONDITIONAL_LENGTH_BYTES))
        return record

    def __repr__(self):
        repr_ = '{}(file={})'
        return repr_.format(self.__class__.__name__, self._file)


class BytesToLog(BytesToStructures):

    def __init__(self, file, header_marshaller, record_marshaller):

        """
        Parameters
        ----------
        file : file
        header_marshaller : adhoc_proto.marshallers.BytesToStructure
        record_marshaller : adhoc_proto.marshallers.BytesToStructure
        """

        self._file = file
        self._header_marshaller = header_marshaller
        self._record_marshaller = record_marshaller

    def marshall(self):

        """
        The time complexity is O(n), where n is the number of bytes
        being read.

        Returns
        -------
        typing.Sequence[suitcase.structure.Structure]
        """

        log = list()
        # Marshall the header.
        header = self._header_marshaller.marshall()
        log.append(header)
        # Marshall the records.
        for _ in xrange(header.record_count):
            record = self._record_marshaller.marshall()
            if record is None:
                break
            log.append(record)
        return log

    def __repr__(self):
        repr_ = '{}(file={}, header_marshaller={}, record_marshaller)'
        return repr_.format(self.__class__.__name__,
                            self._file,
                            self._header_marshaller,
                            self._record_marshaller)
