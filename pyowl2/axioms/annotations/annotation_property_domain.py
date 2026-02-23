from __future__ import annotations

import typing

from rdflib import URIRef

from pyowl2.abstracts.annotation_axiom import OWLAnnotationAxiom
from pyowl2.base.annotation import OWLAnnotation
from pyowl2.base.annotation_property import OWLAnnotationProperty

if typing.TYPE_CHECKING:
    from pyowl2.base.iri import IRI


class OWLAnnotationPropertyDomain(OWLAnnotationAxiom):
    """
    This class represents an axiom that defines a domain restriction for an annotation property, asserting that the subject of any annotation using this property must be an instance of a specific class. It serves as a formal constraint within an ontology, linking an annotation property to a class identifier represented by a URI or IRI. To utilize this entity, one must provide the annotation property to be constrained and the domain class, along with optional metadata annotations that describe the axiom itself.

    :parm annotation_property: The annotation property for which the domain is being specified by this axiom.
    :type annotation_property: OWLAnnotationProperty
    :parm domain: The IRI representing the class of subjects to which the annotation property applies.
    :type domain: typing.Union[URIRef, IRI]
    """

    def __init__(
        self,
        property: OWLAnnotationProperty,
        iri: typing.Union[URIRef, IRI],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Initializes a new instance representing an OWL axiom that defines the domain of an annotation property. This constructor accepts the specific annotation property, the IRI representing the domain, and an optional list of annotations to be associated with the axiom itself. It delegates the storage of annotations to the parent class and sets the internal references for the property and its domain.

        :param property: The OWL annotation property that is the subject of this axiom.
        :type property: OWLAnnotationProperty
        :param iri: The Internationalized Resource Identifier representing the domain of the annotation property.
        :type iri: typing.Union[URIRef, IRI]
        :param annotations: Optional list of OWLAnnotation objects to be associated with this axiom.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        super().__init__(annotations)
        # super().__init__()
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = annotations
        self._annotation_property: OWLAnnotationProperty = property
        self._domain: typing.Union[URIRef, IRI] = iri

    # @property
    # def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
    #     """Getter for axiom_annotations."""
    #     return self._axiom_annotations

    # @axiom_annotations.setter
    # def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
    #     """Setter for axiom_annotations."""
    #     self._axiom_annotations = value

    @property
    def annotation_property(self) -> OWLAnnotationProperty:
        """
        Sets the annotation property for this domain axiom. This method updates the internal state of the object by assigning the provided `OWLAnnotationProperty` instance to the corresponding private attribute, effectively replacing any previously associated value.

        :param value: The OWL annotation property to assign to the instance.
        :type value: OWLAnnotationProperty
        """

        return self._annotation_property

    @annotation_property.setter
    def annotation_property(self, value: OWLAnnotationProperty) -> None:
        """Setter for annotation_property."""
        self._annotation_property = value

    @property
    def domain(self) -> typing.Union[URIRef, IRI]:
        """
        Sets the domain IRI for the OWL annotation property. This method accepts a value that is either a URIRef or an IRI object and updates the internal state of the instance by assigning this value to the `_domain` attribute. It effectively overwrites any existing domain definition stored in the object.

        :param value: The IRI or URI reference to set as the domain.
        :type value: typing.Union[URIRef, IRI]
        """

        return self._domain

    @domain.setter
    def domain(self, value: typing.Union[URIRef, IRI]) -> None:
        """Setter for iri."""
        self._domain = value

    def __str__(self) -> str:
        """
        Returns a string representation of the annotation property domain axiom, formatted in a functional syntax style. The representation always includes the annotation property and the domain, enclosed within an `AnnotationPropertyDomain(...)` structure. If the axiom contains annotations, they are listed at the beginning of the argument list; otherwise, an empty list `[]` is explicitly rendered. This method ensures that the string output accurately reflects the internal state of the axiom, specifically handling the presence or absence of metadata annotations.

        :return: A string representation of the axiom in the format "AnnotationPropertyDomain([annotations] property domain)".

        :rtype: str
        """

        if self.axiom_annotations:
            return f"AnnotationPropertyDomain({self.axiom_annotations} {self.annotation_property} {self.domain})"
        else:
            return (
                f"AnnotationPropertyDomain([] {self.annotation_property} {self.domain})"
            )
