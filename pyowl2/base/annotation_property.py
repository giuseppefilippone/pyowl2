from __future__ import annotations

import typing

from rdflib import URIRef

from pyowl2.abstracts.entity import OWLEntity

if typing.TYPE_CHECKING:
    from pyowl2.base.iri import IRI


class OWLAnnotationProperty(OWLEntity):
    """
    Represents an annotation property within the Web Ontology Language (OWL), serving as a mechanism to associate metadata or annotations with other entities such as IRIs, anonymous individuals, or literals. Unlike object or data properties, annotation properties do not influence the logical semantics of the ontology but are instead used for documentation, labeling, and management of metadata. To utilize this class, instantiate it with a specific Internationalized Resource Identifier (IRI) which acts as the unique identifier for the property; this IRI can be accessed or modified via the corresponding property attribute.

    :param iri: The Internationalized Resource Identifier (IRI) that uniquely identifies this annotation property.
    :type iri: typing.Union[URIRef, IRI]
    """

    def __init__(self, iri: typing.Union[URIRef, IRI]) -> None:
        """
        Initializes a new instance representing an OWL annotation property, which is used to attach metadata to ontology entities. The method requires an Internationalized Resource Identifier (IRI) or a URI reference as its sole argument, serving as the unique identifier for the property. Upon instantiation, this identifier is stored in a protected attribute, establishing the identity of the property within the ontology structure.

        :param iri: The Internationalized Resource Identifier (IRI) or URI Reference (URIRef) identifying the resource.
        :type iri: typing.Union[URIRef, IRI]
        """

        self._iri: typing.Union[URIRef, IRI] = iri

    @property
    def iri(self) -> typing.Union[URIRef, IRI]:
        """
        Sets the Internationalized Resource Identifier (IRI) for the OWL annotation property. This method accepts a value that is either a URIRef or an IRI object and assigns it to the internal attribute, thereby updating the property's identity. Modifying the IRI changes the fundamental identifier used to reference this property within the ontology.

        :param value: The IRI or URI reference to assign to the object.
        :type value: typing.Union[URIRef, IRI]
        """

        return self._iri

    @iri.setter
    def iri(self, value: typing.Union[URIRef, IRI]) -> None:
        self._iri = value

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the annotation property, formatted as "AnnotationProperty({iri})". The method retrieves the internal Internationalized Resource Identifier (IRI) associated with the object to construct this string. This representation is primarily intended for debugging and logging purposes, providing a concise summary of the entity's identity without exposing its full internal structure.

        :return: A string representation of the annotation property in the format 'AnnotationProperty(<iri>)'.

        :rtype: str
        """

        return f"AnnotationProperty({self._iri})"
