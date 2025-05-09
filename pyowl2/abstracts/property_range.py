import abc

from pyowl2.abstracts.object import OWLObject


class OWLPropertyRange(OWLObject, abc.ABC, metaclass=abc.ABCMeta):

    __slots__ = ()
