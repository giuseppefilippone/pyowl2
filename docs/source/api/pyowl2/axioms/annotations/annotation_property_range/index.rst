pyowl2.axioms.annotations.annotation_property_range
===================================================

.. py:module:: pyowl2.axioms.annotations.annotation_property_range



.. ── LLM-GENERATED DESCRIPTION START ──

Implements an OWL axiom that constrains the valid range of values for a specific annotation property.


Description
-----------


Defines the semantic constraint that values assigned to a specific annotation property must belong to a certain class or type. By extending the abstract ``OWLAnnotationAxiom`` base class, the implementation allows the constraint to carry metadata annotations about the axiom itself. The design encapsulates an ``OWLAnnotationProperty`` and a range identifier, which can be either an IRI or a URI reference, providing property accessors to manage these components. A string representation method facilitates debugging and logging by displaying the property, range, and associated annotations in a standardized format.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.annotations.annotation_property_range.OWLAnnotationPropertyRange


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_axioms_annotations_annotation_property_range_OWLAnnotationPropertyRange.png
       :alt: UML Class Diagram for OWLAnnotationPropertyRange
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLAnnotationPropertyRange**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_axioms_annotations_annotation_property_range_OWLAnnotationPropertyRange.pdf
       :alt: UML Class Diagram for OWLAnnotationPropertyRange
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLAnnotationPropertyRange**

.. py:class:: OWLAnnotationPropertyRange(property: pyowl2.base.annotation_property.OWLAnnotationProperty, iri: Union[rdflib.URIRef, pyowl2.base.iri.IRI], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.annotation_axiom.OWLAnnotationAxiom`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.annotations.annotation_property_range.OWLAnnotationPropertyRange
      :parts: 1
      :private-bases:


   This axiom represents a constraint that specifies the valid range of values for a given annotation property within an ontology. It asserts that any value associated with the property must be an instance of the class identified by the provided IRI. To use this entity, one must provide the annotation property to be constrained and the IRI representing the range class, along with optional annotations to attach metadata directly to the axiom.

   :parm annotation_property: The annotation property for which the range is being specified.
   :type annotation_property: OWLAnnotationProperty
   :parm range: The IRI or URI reference identifying the class to which the values of the annotation property must belong.
   :type range: typing.Union[URIRef, IRI]


   .. py:method:: __str__() -> str

      Returns a string representation of the annotation property range axiom, formatted to display the annotations, the annotation property, and the range. The output string follows the pattern "AnnotationPropertyRange([annotations] property range)", where the annotations section reflects the actual `axiom_annotations` if present, or an empty list "[]" if they are absent. This method is intended for debugging or display purposes and does not modify the state of the object.

      :return: A string representation of the annotation property range axiom, formatted as 'AnnotationPropertyRange([annotations] property range)'.

      :rtype: str



   .. py:attribute:: _annotation_property
      :type:  pyowl2.base.annotation_property.OWLAnnotationProperty


   .. py:attribute:: _range
      :type:  Union[rdflib.URIRef, pyowl2.base.iri.IRI]


   .. py:property:: annotation_property
      :type: pyowl2.base.annotation_property.OWLAnnotationProperty


      Updates the annotation property associated with this `OWLAnnotationPropertyRange` instance by assigning the provided value to the internal state. This method serves as the setter for the `annotation_property` attribute, replacing any existing reference with the new `OWLAnnotationProperty` object. The operation mutates the instance in place and does not return a value.

      :param value: The OWL annotation property to assign to the object.
      :type value: OWLAnnotationProperty


   .. py:property:: range
      :type: Union[rdflib.URIRef, pyowl2.base.iri.IRI]


      Sets the range restriction for the OWL annotation property represented by this object. The method accepts a value that must be a URI reference or an IRI, which identifies the specific type or class defining the range. Upon invocation, it updates the internal state of the instance by assigning the provided value to the private `_range` attribute.

      :param value: The URI or IRI to assign as the range.
      :type value: typing.Union[URIRef, IRI]

