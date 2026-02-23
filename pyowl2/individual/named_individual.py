import typing

from rdflib import URIRef

from pyowl2.abstracts.individual import OWLIndividual
from pyowl2.base.iri import IRI


class OWLNamedIndividual(OWLIndividual):
    """
    This class represents a specific entity within an OWL ontology that is distinguished by a unique Internationalized Resource Identifier (IRI). Unlike anonymous individuals, this entity possesses a persistent, globally resolvable identifier that allows it to be unambiguously referenced in axioms and assertions. It is typically used to model concrete instances of classes, such as specific people, objects, or data points, and provides mechanisms to initialize, access, and modify its associated IRI.

    :parm iri: The unique Internationalized Resource Identifier (IRI) that identifies the named individual within the ontology, allowing for unambiguous reference in axioms and assertions.
    :type iri: typing.Union[URIRef, IRI]
    """

    def __init__(self, iri: typing.Union[URIRef, IRI]) -> None:
        """
        Constructs an OWLNamedIndividual object, representing a specific, identifiable instance within an OWL ontology. The method requires an Internationalized Resource Identifier (IRI) or URI reference as a mandatory argument, which serves as the unique identity for the individual. This identifier is stored internally for subsequent access, and the constructor ensures that any initialization logic defined by the parent class is also executed.

        :param iri: The Internationalized Resource Identifier (IRI) or URI reference representing the resource.
        :type iri: typing.Union[URIRef, IRI]
        """

        super().__init__()
        self._iri: typing.Union[URIRef, IRI] = iri

    @property
    def iri(self) -> typing.Union[URIRef, IRI]:
        """
        Assigns a new Internationalized Resource Identifier (IRI) to the named individual, effectively changing its identity within the ontology. The method accepts a value that is either a URIRef or an IRI object and updates the internal state accordingly. This operation directly mutates the instance, replacing any previously stored IRI.

        :param value: The IRI or URI reference to assign to the object.
        :type value: typing.Union[URIRef, IRI]
        """

        return self._iri

    @iri.setter
    def iri(self, value: typing.Union[URIRef, IRI]) -> None:
        """Setter for iri."""
        self._iri = value

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the current instance, formatted as "NamedIndividual({iri})" where {iri} is the value of the object's IRI attribute. This method is invoked implicitly by the `str()` built-in function and print statements, providing a concise summary useful for debugging and logging. The operation has no side effects and relies solely on the current state of the `iri` attribute; if the IRI is not set or is None, the string will reflect that state accordingly.

        :return: A string representation of the instance, formatted as 'NamedIndividual(<iri>)'.

        :rtype: str
        """

        return f"NamedIndividual({self.iri})"
