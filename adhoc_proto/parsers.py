# -*- coding: utf-8 -*-

import abc


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
