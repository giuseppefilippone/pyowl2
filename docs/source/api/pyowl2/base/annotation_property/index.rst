pyowl2.base.annotation_property
===============================

.. py:module:: pyowl2.base.annotation_property



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a representation of an OWL annotation property that facilitates the attachment of metadata to ontology entities without affecting logical semantics.


Description
-----------


The software defines a structure for handling annotation properties within the Web Ontology Language, specifically designed to manage metadata such as labels and comments without influencing the logical reasoning of the ontology. By extending a base entity class, the implementation ensures that these properties are treated as distinct components separate from data and object properties that drive semantic interpretation. Central to the design is the encapsulation of an Internationalized Resource Identifier (IRI), which acts as the unique identifier for the property and is managed through controlled accessors to maintain data integrity. Additionally, a string representation mechanism is included to provide a clear, human-readable format for debugging and logging purposes by explicitly exposing the associated identifier.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.base.annotation_property.OWLAnnotationProperty


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_base_annotation_property_OWLAnnotationProperty.png
       :alt: UML Class Diagram for OWLAnnotationProperty
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLAnnotationProperty**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_base_annotation_property_OWLAnnotationProperty.pdf
       :alt: UML Class Diagram for OWLAnnotationProperty
       :align: center
       :width: 9.4cm
       :class: uml-diagram

       UML Class Diagram for **OWLAnnotationProperty**

.. py:class:: OWLAnnotationProperty(iri: Union[rdflib.URIRef, pyowl2.base.iri.IRI])

   Bases: :py:obj:`pyowl2.abstracts.entity.OWLEntity`

   .. autoapi-inheritance-diagram:: pyowl2.base.annotation_property.OWLAnnotationProperty
      :parts: 1
      :private-bases:


   Represents an annotation property within the Web Ontology Language (OWL), serving as a mechanism to associate metadata or annotations with other entities such as IRIs, anonymous individuals, or literals. Unlike object or data properties, annotation properties do not influence the logical semantics of the ontology but are instead used for documentation, labeling, and management of metadata. To utilize this class, instantiate it with a specific Internationalized Resource Identifier (IRI) which acts as the unique identifier for the property; this IRI can be accessed or modified via the corresponding property attribute.

   :param iri: The Internationalized Resource Identifier (IRI) that uniquely identifies this annotation property.
   :type iri: typing.Union[URIRef, IRI]


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the annotation property, formatted as "AnnotationProperty({iri})". The method retrieves the internal Internationalized Resource Identifier (IRI) associated with the object to construct this string. This representation is primarily intended for debugging and logging purposes, providing a concise summary of the entity's identity without exposing its full internal structure.

      :return: A string representation of the annotation property in the format 'AnnotationProperty(<iri>)'.

      :rtype: str



   .. py:attribute:: _iri
      :type:  Union[rdflib.URIRef, pyowl2.base.iri.IRI]


   .. py:property:: iri
      :type: Union[rdflib.URIRef, pyowl2.base.iri.IRI]


      Sets the Internationalized Resource Identifier (IRI) for the OWL annotation property. This method accepts a value that is either a URIRef or an IRI object and assigns it to the internal attribute, thereby updating the property's identity. Modifying the IRI changes the fundamental identifier used to reference this property within the ontology.

      :param value: The IRI or URI reference to assign to the object.
      :type value: typing.Union[URIRef, IRI]

