import abc

from pyowl2.abstracts.object import OWLObject


class OWLDataPropertyExpression(OWLObject, abc.ABC, metaclass=abc.ABCMeta):
    """
    This abstract base class represents expressions involving OWL data properties, which define relationships between an individual and a literal value, such as a string or integer. It serves as the root interface for data property constructs within the ontology model, distinguishing them from object properties that link individuals to other individuals. Users can utilize this class to check specific characteristics of a property expression, such as whether it represents the universal (top) data property or the empty (bottom) data property.
    """


    __slots__ = ()

    @abc.abstractmethod
    def is_top_data_property(self) -> bool:
        """
        Determines whether this specific data property expression represents the top data property, which is the universal property that relates every individual to every literal in the ontology. This check is essential for reasoning tasks and ontology normalization, as the top property acts as the identity element for certain property operations. The method returns a boolean value indicating if the expression is equivalent to the built-in top data property, without modifying the underlying expression.

        :return: True if the property is the top data property, False otherwise.

        :rtype: bool
        """

        pass

    @abc.abstractmethod
    def is_bottom_data_property(self) -> bool:
        """
        Determines whether this data property expression represents the bottom data property, which is the property that no individual can possess. In OWL semantics, the bottom data property corresponds to the empty set of data property assertions. This method returns `True` if the expression is equivalent to the built-in `owl:bottomDataProperty`, and `False` for any other data property expression.

        :return: True if the data property is the bottom-most one, False otherwise.

        :rtype: bool
        """

        pass
