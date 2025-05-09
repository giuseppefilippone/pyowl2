import abc

from pyowl2.abstracts.object import OWLObject


class OWLObjectPropertyExpression(OWLObject, abc.ABC, metaclass=abc.ABCMeta):
    """
    An expression involving object properties, such as an object property or its inverse.
    """

    __slots__ = ()

    @abc.abstractmethod
    def is_top_object_property(self) -> bool:
        pass

    @abc.abstractmethod
    def is_bottom_object_property(self) -> bool:
        pass
