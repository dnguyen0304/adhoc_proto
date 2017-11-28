# -*- coding: utf-8 -*-

import abc


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
