import abc

from pyowl2.abstracts.object import OWLObject


class OWLObjectPropertyExpression(OWLObject, abc.ABC, metaclass=abc.ABCMeta):
    """
    This abstract base class defines the interface for expressions that represent relationships between individuals in an OWL ontology, covering both simple named properties and complex constructs such as inverse properties. It acts as a common type for any entity functioning as an object property, allowing the system to treat various property forms uniformly. Furthermore, it mandates the implementation of methods to identify if the expression corresponds to the universal (top) or empty (bottom) property, which are specific logical constants used in reasoning.
    """


    __slots__ = ()

    @abc.abstractmethod
    def is_top_object_property(self) -> bool:
        """
        Determines whether this object property expression corresponds to the universal top object property, which is the property that relates every possible pair of individuals in the ontology. This method returns True if the expression is the top property, and False for any other property, including named properties or complex expressions like inverse or property chains. The check is purely evaluative and does not produce any side effects or modifications to the ontology.

        :return: True if the property is the top object property in the hierarchy, otherwise False.

        :rtype: bool
        """

        pass

    @abc.abstractmethod
    def is_bottom_object_property(self) -> bool:
        """
        Determines whether this object property expression represents the bottom object property, which is the property that no pair of individuals can satisfy. In the context of the Web Ontology Language (OWL), this corresponds to `owl:bottomObjectProperty` and acts as the logical equivalent of "false" for property expressions. The method returns True if the expression is the bottom property and False otherwise, serving as a read-only check that does not alter the state of the object.

        :return: True if this property is the bottom object property (the property that relates no individuals), False otherwise.

        :rtype: bool
        """

        pass
