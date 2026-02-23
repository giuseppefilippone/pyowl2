import typing

from rdflib import OWL, Namespace, URIRef

from pyowl2.abstracts.data_property_expression import OWLDataPropertyExpression
from pyowl2.abstracts.entity import OWLEntity
from pyowl2.base.iri import IRI


class OWLDataProperty(OWLEntity, OWLDataPropertyExpression):
    """
    This class represents a property within an ontology that associates an individual entity with a literal data value, such as a string, integer, or date, rather than linking to another individual. It is uniquely identified by an Internationalized Resource Identifier (IRI), which acts as its canonical name and allows it to be referenced in axioms and assertions. Instances can be created by specifying an IRI, or users can retrieve the universal and empty data properties using the static `top` and `bottom` methods. The class also includes functionality to determine if a specific instance corresponds to these special system properties, which is useful for logical reasoning and ontology validation.

    :parm iri: The Internationalized Resource Identifier that uniquely identifies this data property within the ontology. It serves as the primary identifier for the entity, enabling its use in axioms, assertions, and logical comparisons.
    :type iri: typing.Union[URIRef, IRI]
    """

    def __init__(self, iri: typing.Union[URIRef, IRI]) -> None:
        """
        Constructs a new instance representing an OWL data property, a specific type of property in the Web Ontology Language that associates individuals with literal data values like integers or strings. The method requires a unique identifier, provided as either a URIRef or an IRI object, which is assigned to an internal attribute to distinguish this property from others. No validation is performed on the structure of the IRI beyond type checking, and the operation has no side effects outside of initializing the instance's state.

        :param iri: The Internationalized Resource Identifier (IRI) or URI reference representing the resource.
        :type iri: typing.Union[URIRef, IRI]
        """

        self._iri: typing.Union[URIRef, IRI] = iri

    @staticmethod
    def top() -> typing.Self:
        """
        Returns the instance representing the universal data property defined in the OWL 2 specification. This static method constructs an entity using the specific IRI for `owl:topDataProperty` within the standard OWL namespace. Semantically, this property serves as the most general data property, being a super-property of every other data property in the ontology.

        :return: Returns the OWL top data property instance, representing the universal super-property of all data properties.

        :rtype: typing.Self
        """

        return OWLDataProperty(IRI(Namespace(OWL._NS), OWL.topDataProperty))

    @staticmethod
    def bottom() -> typing.Self:
        """
        Returns the standard OWL entity representing the bottom data property, which is the data property that has no instances. This static method constructs an instance using the specific IRI `owl:bottomDataProperty` from the OWL namespace. It serves as a factory for accessing this built-in vocabulary term, creating a new object instance on each invocation without side effects.

        :return: Returns the OWL bottom data property.

        :rtype: typing.Self
        """

        return OWLDataProperty(IRI(Namespace(OWL._NS), OWL.bottomDataProperty))

    @property
    def iri(self) -> typing.Union[URIRef, IRI]:
        """
        Sets the Internationalized Resource Identifier (IRI) for the OWL data property instance. This method accepts a value of type `URIRef` or `IRI` and assigns it to the internal `_iri` attribute, effectively updating the unique identifier of the property. Changing the IRI modifies the core identity of the entity, which may impact its resolution and relationships within an ontology graph.

        :param value: The IRI or URI reference to assign to the object.
        :type value: typing.Union[URIRef, IRI]
        """

        return self._iri

    @iri.setter
    def iri(self, value: typing.Union[URIRef, IRI]) -> None:
        self._iri = value

    def is_top_data_property(self) -> bool:
        """
        Determines whether this data property instance represents the top data property, which is the universal property encompassing all data properties in the ontology. The method returns `True` if the instance is identical to the class-level definition of the top property, and `False` otherwise. This check is performed without modifying the state of the object.

        :return: True if this data property is the top data property, False otherwise.

        :rtype: bool
        """

        return self == OWLDataProperty.top()

    def is_bottom_data_property(self) -> bool:
        """
        Determines whether the current data property instance represents the bottom data property within the OWL ontology hierarchy. The bottom data property is the most specific concept in the hierarchy, often corresponding to the empty set or a property that no individual possesses. This method performs a direct equality comparison against the canonical bottom data property instance and returns True if they match, otherwise False.

        :return: True if this data property is the bottom data property, False otherwise.

        :rtype: bool
        """

        return self == OWLDataProperty.bottom()

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the data property, formatted to include the class name and the associated Internationalized Resource Identifier (IRI). The output follows the pattern "DataProperty({iri})", making it suitable for debugging and logging purposes. This method does not modify the object's state and relies on the internal `_iri` attribute being defined and convertible to a string.

        :return: A string representation of the object, formatted as 'DataProperty({iri})' where {iri} is the object's IRI.

        :rtype: str
        """

        return f"DataProperty({self._iri})"
