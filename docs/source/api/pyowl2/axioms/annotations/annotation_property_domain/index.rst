pyowl2.axioms.annotations.annotation_property_domain
====================================================

.. py:module:: pyowl2.axioms.annotations.annotation_property_domain



.. ── LLM-GENERATED DESCRIPTION START ──

Defines an OWL axiom that restricts the domain of an annotation property to a specific class identified by an IRI.


Description
-----------


The implementation models a semantic constraint within an ontology by asserting that the subject of any annotation utilizing a specific property must be an instance of a designated class. It encapsulates the relationship between an annotation property and a domain identifier, which can be represented as either a URI reference or an Internationalized Resource Identifier. By inheriting from a base annotation axiom class, it supports the attachment of optional metadata annotations that describe the axiom itself, separating the logical constraint from descriptive information. The logic includes a string representation mechanism that renders the structure in functional syntax, explicitly handling the presence or absence of these metadata annotations to ensure accurate serialization.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.annotations.annotation_property_domain.OWLAnnotationPropertyDomain


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_axioms_annotations_annotation_property_domain_OWLAnnotationPropertyDomain.png
       :alt: UML Class Diagram for OWLAnnotationPropertyDomain
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLAnnotationPropertyDomain**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_axioms_annotations_annotation_property_domain_OWLAnnotationPropertyDomain.pdf
       :alt: UML Class Diagram for OWLAnnotationPropertyDomain
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLAnnotationPropertyDomain**

.. py:class:: OWLAnnotationPropertyDomain(property: pyowl2.base.annotation_property.OWLAnnotationProperty, iri: Union[rdflib.URIRef, pyowl2.base.iri.IRI], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.annotation_axiom.OWLAnnotationAxiom`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.annotations.annotation_property_domain.OWLAnnotationPropertyDomain
      :parts: 1
      :private-bases:


   This class represents an axiom that defines a domain restriction for an annotation property, asserting that the subject of any annotation using this property must be an instance of a specific class. It serves as a formal constraint within an ontology, linking an annotation property to a class identifier represented by a URI or IRI. To utilize this entity, one must provide the annotation property to be constrained and the domain class, along with optional metadata annotations that describe the axiom itself.

   :param annotation_property: The annotation property for which the domain is being specified by this axiom.
   :type annotation_property: OWLAnnotationProperty
   :param domain: The IRI representing the class of subjects to which the annotation property applies.
   :type domain: typing.Union[URIRef, IRI]


   .. py:method:: __str__() -> str

      Returns a string representation of the annotation property domain axiom, formatted in a functional syntax style. The representation always includes the annotation property and the domain, enclosed within an `AnnotationPropertyDomain(...)` structure. If the axiom contains annotations, they are listed at the beginning of the argument list; otherwise, an empty list `[]` is explicitly rendered. This method ensures that the string output accurately reflects the internal state of the axiom, specifically handling the presence or absence of metadata annotations.

      :return: A string representation of the axiom in the format "AnnotationPropertyDomain([annotations] property domain)".

      :rtype: str



   .. py:attribute:: _annotation_property
      :type:  pyowl2.base.annotation_property.OWLAnnotationProperty


   .. py:attribute:: _domain
      :type:  Union[rdflib.URIRef, pyowl2.base.iri.IRI]


   .. py:property:: annotation_property
      :type: pyowl2.base.annotation_property.OWLAnnotationProperty


      Sets the annotation property for this domain axiom. This method updates the internal state of the object by assigning the provided `OWLAnnotationProperty` instance to the corresponding private attribute, effectively replacing any previously associated value.

      :param value: The OWL annotation property to assign to the instance.
      :type value: OWLAnnotationProperty


   .. py:property:: domain
      :type: Union[rdflib.URIRef, pyowl2.base.iri.IRI]


      Sets the domain IRI for the OWL annotation property. This method accepts a value that is either a URIRef or an IRI object and updates the internal state of the instance by assigning this value to the `_domain` attribute. It effectively overwrites any existing domain definition stored in the object.

      :param value: The IRI or URI reference to set as the domain.
      :type value: typing.Union[URIRef, IRI]

