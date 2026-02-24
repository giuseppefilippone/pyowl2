import typing

from rdflib import OWL, Namespace, URIRef

from pyowl2.abstracts.entity import OWLEntity
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression
from pyowl2.base.iri import IRI


class OWLObjectProperty(OWLEntity, OWLObjectPropertyExpression):
    """
    This class models an OWL Object Property, which serves as a binary relation connecting two individuals within an ontology. Users can instantiate this class by providing an IRI (Internationalized Resource Identifier) that uniquely identifies the property, such as a URI representing "hasParent". Beyond standard instantiation, the class offers static methods to retrieve the universal top property and the empty bottom property, as well as instance methods to check if the current property corresponds to these specific OWL entities.

    :param iri: Backing field for the public `iri` property, holding the Internationalized Resource Identifier (IRI) that uniquely identifies this object property within the ontology.
    :type iri: typing.Union[URIRef, IRI]
    """

    def __init__(self, iri: typing.Union[URIRef, IRI]) -> None:
        """
        Initializes a new instance of the OWLObjectProperty class using the provided Internationalized Resource Identifier (IRI). The constructor accepts either a `URIRef` or an `IRI` object, which serves as the unique identifier for the object property. This identifier is stored internally in the `_iri` attribute, establishing the entity's identity without performing any external registration or validation beyond the assignment.

        :param iri: The Internationalized Resource Identifier (IRI) or URI reference identifying the resource.
        :type iri: typing.Union[URIRef, IRI]
        """

        self._iri: typing.Union[URIRef, IRI] = iri

    @staticmethod
    def top() -> typing.Self:
        """
        Returns an instance representing the universal object property from the OWL vocabulary, which is the property that relates every individual to every other individual. This static method creates a new object property identified by the standard IRI `http://www.w3.org/2002/07/owl#topObjectProperty`. As the top element of the object property hierarchy, it acts as a superclass for all other specific object properties.

        :return: Returns an instance representing the OWL top object property (owl:topObjectProperty), which is the universal property relating all individuals.

        :rtype: typing.Self
        """

        return OWLObjectProperty(IRI(Namespace(OWL._NS), OWL.topObjectProperty))

    @staticmethod
    def bottom() -> typing.Self:
        """
        Returns the OWL 2 bottom object property, which represents the property that no pair of individuals instantiate. This static method constructs an `OWLObjectProperty` instance using the specific IRI defined in the OWL namespace for `owl:bottomObjectProperty`. It acts as the universal lower bound within the object property hierarchy and has no side effects.

        :return: Returns the OWL bottom object property (owl:bottomObjectProperty).

        :rtype: typing.Self
        """

        return OWLObjectProperty(IRI(Namespace(OWL._NS), OWL.bottomObjectProperty))

    @property
    def iri(self) -> typing.Union[URIRef, IRI]:
        """
        Sets the Internationalized Resource Identifier (IRI) for this OWL object property. The method accepts a value of type URIRef or IRI and assigns it to the internal `_iri` attribute, thereby updating the unique identifier of the entity. This operation directly modifies the object's state, changing how it is referenced within the ontology.

        :param value: The IRI or URI reference to assign to the object.
        :type value: typing.Union[URIRef, IRI]
        """

        return self._iri

    @iri.setter
    def iri(self, value: typing.Union[URIRef, IRI]) -> None:
        self._iri = value

    def is_top_object_property(self) -> bool:
        """
        Determines whether the current object property instance is the universal top object property, which serves as the superclass of all object properties in OWL. This method performs a direct comparison against the specific entity representing the top property. It returns `True` if the instance is the top property, and `False` otherwise.

        :return: True if this property is the top object property, False otherwise.

        :rtype: bool
        """

        return self == OWLObjectProperty.top()

    def is_bottom_object_property(self) -> bool:
        """
        Checks if this object property instance is the bottom object property, which is the universal sub-property that relates no pairs of individuals. This method returns `True` if the current instance is identical to the static bottom property defined by the class, and `False` otherwise. It is a pure query method with no side effects.

        :return: True if this object property is the bottom object property, otherwise False.

        :rtype: bool
        """

        return self == OWLObjectProperty.bottom()

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the object property, formatted to display the entity type alongside its Internationalized Resource Identifier (IRI). This method is primarily used for debugging and logging, providing a concise summary that identifies the instance as an ObjectProperty and exposes its specific identifier. The operation has no side effects and relies on the internal `_iri` attribute to construct the output string.

        :return: A string representation of the object, formatted as 'ObjectProperty({iri})' where {iri} is the object's IRI.

        :rtype: str
        """

        return f"ObjectProperty({self._iri})"
