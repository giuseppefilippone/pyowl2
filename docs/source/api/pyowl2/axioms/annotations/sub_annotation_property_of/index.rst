pyowl2.axioms.annotations.sub_annotation_property_of
====================================================

.. py:module:: pyowl2.axioms.annotations.sub_annotation_property_of



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a data structure representing the OWL SubAnnotationPropertyOf axiom, which establishes a hierarchical relationship where one annotation property is a sub-property of another.


Description
-----------


By storing references to both the specific sub-property and the broader super-property, the logic enables semantic inference, ensuring that annotations applied using the sub-property are implicitly understood to apply to the super-property as well. The design leverages inheritance to manage optional metadata about the axiom itself, allowing users to attach additional context or source information. Access to the core properties is provided through mutable attributes, and the structure includes a string representation method that outputs the relationship in standard functional syntax for interoperability.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.annotations.sub_annotation_property_of.OWLSubAnnotationPropertyOf


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_axioms_annotations_sub_annotation_property_of_OWLSubAnnotationPropertyOf.png
       :alt: UML Class Diagram for OWLSubAnnotationPropertyOf
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLSubAnnotationPropertyOf**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_axioms_annotations_sub_annotation_property_of_OWLSubAnnotationPropertyOf.pdf
       :alt: UML Class Diagram for OWLSubAnnotationPropertyOf
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLSubAnnotationPropertyOf**

.. py:class:: OWLSubAnnotationPropertyOf(sub_property: pyowl2.base.annotation_property.OWLAnnotationProperty, super_property: pyowl2.base.annotation_property.OWLAnnotationProperty, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.annotation_axiom.OWLAnnotationAxiom`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.annotations.sub_annotation_property_of.OWLSubAnnotationPropertyOf
      :parts: 1
      :private-bases:


   This class represents an axiom within the Web Ontology Language (OWL) that defines a hierarchical relationship between two annotation properties, asserting that one is a subproperty of the other. By establishing this relationship, it enables semantic inference where any annotation applied using the subproperty is implicitly understood to also apply to the superproperty. To use this class, instantiate it with the specific sub-property and super-property instances, optionally including a list of annotations to provide metadata about the axiom itself, such as its source or context. The properties of the axiom can be accessed and modified directly via the provided attributes, allowing for dynamic updates to the ontology structure.

   :parm sub_annotation_property: The annotation property asserted to be a subproperty of the super annotation property.
   :type sub_annotation_property: OWLAnnotationProperty
   :parm super_annotation_property: The annotation property asserted to be the superproperty in the subproperty relationship, representing the parent property that the sub-property implies.
   :type super_annotation_property: OWLAnnotationProperty


   .. py:method:: __str__() -> str

      Returns a string representation of the sub-annotation property axiom in a functional syntax format. The string begins with "SubAnnotationPropertyOf" followed by the axiom annotations; if no annotations are present, an empty list is explicitly displayed. The representation concludes with the sub-annotation property and the super-annotation property identifiers.

      :return: A string representation of the axiom, formatted as `SubAnnotationPropertyOf([annotations] sub_property super_property)`.

      :rtype: str



   .. py:attribute:: _sub_annotation_property
      :type:  pyowl2.base.annotation_property.OWLAnnotationProperty


   .. py:attribute:: _super_annotation_property
      :type:  pyowl2.base.annotation_property.OWLAnnotationProperty


   .. py:property:: sub_annotation_property
      :type: pyowl2.base.annotation_property.OWLAnnotationProperty


      Sets the specific annotation property that serves as the sub-property within this `OWLSubAnnotationPropertyOf` axiom. This method accepts an `OWLAnnotationProperty` instance and updates the internal state, replacing any previously stored value for this property.

      :param value: The OWL annotation property to be set as the sub-annotation property.
      :type value: OWLAnnotationProperty


   .. py:property:: super_annotation_property
      :type: pyowl2.base.annotation_property.OWLAnnotationProperty


      Sets the super annotation property that defines the parent of the relationship represented by this `OWLSubAnnotationPropertyOf` axiom. It accepts an `OWLAnnotationProperty` instance and assigns it to the internal `_super_annotation_property` attribute, overwriting any existing value. This operation directly modifies the object's state to reflect the new hierarchy.

      :param value: The annotation property to set as the super property.
      :type value: OWLAnnotationProperty

