import typing

from rdflib import OWL, Namespace, URIRef

from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.entity import OWLEntity
from pyowl2.base.iri import IRI


class OWLClass(OWLClassExpression, OWLEntity):
    """
    Represents a named class within an OWL ontology, functioning as a conceptual grouping for individuals that share specific characteristics or properties. It is uniquely identified by an Internationalized Resource Identifier (IRI), which serves as the definitive reference for the class in axioms and assertions. To define a specific concept, instances are created by providing an IRI, such as a URI representing "Person" or "Vehicle." The class also provides static methods to access the universal class (`owl:Thing`) and the empty class (`owl:Nothing`), enabling the representation of the top and bottom elements of the class hierarchy. As a subclass of both `OWLClassExpression` and `OWLEntity`, it serves as a fundamental building block for constructing complex logical descriptions and defining relationships within the ontology.

    :param iri: Stores the Internationalized Resource Identifier (IRI) that uniquely identifies the class within the ontology, used for referencing the class in axioms and assertions.
    :type iri: typing.Union[URIRef, IRI]
    """

    def __init__(self, iri: typing.Union[URIRef, IRI]) -> None:
        """
        Constructs an `OWLClass` instance identified by a specific Internationalized Resource Identifier (IRI). The method accepts an IRI argument, which may be either a `URIRef` or an `IRI` object, and stores it within the private `_iri` attribute to establish the entity's unique identity. This initialization is a prerequisite for any further interaction with the class, as the internal IRI is used to distinguish this specific ontology class from others.

        :param iri: The Internationalized Resource Identifier (IRI) or URI Reference (URIRef) identifying the resource.
        :type iri: typing.Union[URIRef, IRI]
        """

        self._iri: typing.Union[URIRef, IRI] = iri

    @staticmethod
    def thing() -> typing.Self:
        """
        Retrieves the `OWLClass` instance representing `owl:Thing`, which is the universal class in the OWL ontology and the root of the class hierarchy. This static method constructs the class using the standard OWL namespace IRI, ensuring the returned object corresponds to the official top-level concept defined by the specification. It does not depend on instance state and returns a new representation of the class each time it is called.

        :return: Returns the OWL class representing the universal class (owl:Thing).

        :rtype: typing.Self
        """

        return OWLClass(IRI(Namespace(OWL._NS), OWL.Thing))

    @staticmethod
    def nothing() -> typing.Self:
        """
        Returns the OWL class representing the empty set, formally known as `owl:Nothing`. This static method constructs an instance of `OWLClass` initialized with the specific IRI corresponding to the bottom element of the OWL class hierarchy. It is used to denote a contradiction or a class that cannot have any instances. The function has no side effects and does not accept any arguments.

        :return: Returns the OWL class representing the empty set (owl:Nothing).

        :rtype: typing.Self
        """

        return OWLClass(IRI(Namespace(OWL._NS), OWL.Nothing))

    def is_thing(self) -> bool:
        """
        Checks if the current instance represents the universal class 'owl:Thing', which serves as the root of the class hierarchy in OWL ontologies. This method compares the instance against the canonical 'Thing' class to determine equivalence. It returns True if the instance is the top-level class, and False otherwise.

        :return: True if this object is the OWL Thing class, otherwise False.

        :rtype: bool
        """

        return self == OWLClass.thing()

    def is_nothing(self) -> bool:
        """
        Checks if the current instance represents the empty class, often denoted as 'owl:Nothing' in the Web Ontology Language. This method returns True if the object is equivalent to the canonical bottom class, which signifies a class with no instances. It performs a direct equality comparison against the static nothing() instance to determine this status.

        :return: True if the object represents the OWL Nothing class, otherwise False.

        :rtype: bool
        """

        return self == OWLClass.nothing()

    @property
    def iri(self) -> typing.Union[URIRef, IRI]:
        """
        Sets the Internationalized Resource Identifier (IRI) for the OWL class instance. This method accepts a value that is either a URIRef or an IRI object and assigns it to the internal `_iri` attribute, thereby updating the unique identifier of the class. This operation modifies the state of the object in place.

        :param value: The IRI or URI reference to assign to the object.
        :type value: typing.Union[URIRef, IRI]
        """

        return self._iri

    @iri.setter
    def iri(self, value: typing.Union[URIRef, IRI]) -> None:
        self._iri = value

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the OWL class, formatted as "Class({iri})" where {iri} corresponds to the class's Internationalized Resource Identifier. This method is primarily intended for debugging and logging purposes and is automatically invoked by the built-in `str()` function and print statements. It does not modify the object's state and relies on the current value of the `iri` attribute for the output content.

        :return: Returns a string representation of the object, formatted as 'Class({iri})'.

        :rtype: str
        """

        return f"Class({self.iri})"
