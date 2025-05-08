import abc

from pyowl.abstracts.object import OWLObject


class OWLDataPropertyExpression(OWLObject, abc.ABC, metaclass=abc.ABCMeta):
    """
    An expression involving data properties, which represent relationships between an individual and a literal.
    """

    __slots__ = ()

    @abc.abstractmethod
    def is_top_data_property(self) -> bool:
        pass

    @abc.abstractmethod
    def is_bottom_data_property(self) -> bool:
        pass
