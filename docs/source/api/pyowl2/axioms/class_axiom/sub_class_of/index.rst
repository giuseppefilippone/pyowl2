pyowl2.axioms.class_axiom.sub_class_of
======================================

.. py:module:: pyowl2.axioms.class_axiom.sub_class_of



.. ── LLM-GENERATED DESCRIPTION START ──

Implements the OWL SubClassOf axiom to model hierarchical relationships between ontology classes by asserting that all instances of a subclass are also instances of a superclass.


Description
-----------


The software models a fundamental logical construct from the Web Ontology Language that establishes a taxonomic hierarchy by asserting that every instance of a specific subclass expression must also be an instance of a more general superclass expression. By inheriting from a base class axiom, it integrates into a broader ontology framework, allowing for the attachment of optional annotations such as provenance or confidence scores to the logical statement. The implementation manages the relationship through properties that expose and modify the subclass and superclass expressions, ensuring that the internal state reflects the defined logical constraints. A string representation method generates a functional syntax output, which aids in debugging and serialization by clearly displaying the axiom type, associated annotations, and the linked class expressions.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.class_axiom.sub_class_of.OWLSubClassOf


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_axioms_class_axiom_sub_class_of_OWLSubClassOf.png
       :alt: UML Class Diagram for OWLSubClassOf
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLSubClassOf**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_axioms_class_axiom_sub_class_of_OWLSubClassOf.pdf
       :alt: UML Class Diagram for OWLSubClassOf
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLSubClassOf**

.. py:class:: OWLSubClassOf(sub_class: pyowl2.abstracts.class_expression.OWLClassExpression, super_class: pyowl2.abstracts.class_expression.OWLClassExpression, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.class_axiom.OWLClassAxiom`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.class_axiom.sub_class_of.OWLSubClassOf
      :parts: 1
      :private-bases:


   Represents a fundamental axiom in the Web Ontology Language that defines a hierarchical relationship between two class expressions, asserting that all instances of the subclass are necessarily instances of the superclass. This construct allows for the creation of taxonomies and logical constraints by linking either simple named classes or complex, anonymous class expressions. To use this entity, instantiate it with the specific subclass and superclass expressions, optionally providing a list of annotations to attach metadata such as provenance or confidence levels to the logical statement.

   :parm sub_class_expression: The class expression that is declared to be a subclass of the superclass expression.
   :type sub_class_expression: OWLClassExpression
   :parm super_class_expression: The superclass expression in the axiom, representing the more general concept that the subclass is a subset of.
   :type super_class_expression: OWLClassExpression


   .. py:method:: __str__() -> str

      Returns a string representation of the SubClassOf axiom, formatted according to a functional syntax style. The output string includes the axiom annotations, the sub-class expression, and the super-class expression. If the axiom contains annotations, they are included in the string; otherwise, an empty list is explicitly rendered to ensure the structure remains consistent. This method has no side effects and is primarily used for debugging or logging purposes.

      :return: A string representation of the SubClassOf axiom, formatted as 'SubClassOf([annotations] sub_class_expression super_class_expression)'.

      :rtype: str



   .. py:attribute:: _sub_class_expression
      :type:  pyowl2.abstracts.class_expression.OWLClassExpression


   .. py:attribute:: _super_class_expression
      :type:  pyowl2.abstracts.class_expression.OWLClassExpression


   .. py:property:: sub_class_expression
      :type: pyowl2.abstracts.class_expression.OWLClassExpression


      Updates the subclass expression component of the OWL SubClassOf axiom by assigning the provided `OWLClassExpression` to the internal attribute. This method modifies the object's state in place, overwriting any previously stored subclass expression with the new value.

      :param value: The OWL class expression to be set as the subclass.
      :type value: OWLClassExpression


   .. py:property:: super_class_expression
      :type: pyowl2.abstracts.class_expression.OWLClassExpression


      Sets the superclass expression for this `OWLSubClassOf` axiom to the provided value. This method updates the internal state of the object, replacing the existing superclass definition with the new `OWLClassExpression`. As a property setter, it directly modifies the axiom's structure to reflect that the subclass is a sub-class of the specified expression.

      :param value: The expression representing the superclass to be set.
      :type value: OWLClassExpression

