pyowl2.axioms.class_axiom.equivalent_classes
============================================

.. py:module:: pyowl2.axioms.class_axiom.equivalent_classes



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a logical axiom asserting that two or more OWL class expressions share the exact same set of instances.


Description
-----------


The implementation models the semantic identity between distinct concepts, enabling reasoners to infer that any individual belonging to one class must also belong to all others declared equivalent. To ensure consistency and logical validity, the construction process mandates that a minimum of two class expressions are provided, preventing the creation of trivial or incomplete equivalences. A key design choice involves the automatic sorting of these expressions upon initialization and modification, which guarantees a canonical representation where the order of input does not affect the identity of the axiom. Optional metadata can be attached via annotations, and the structure supports a functional-style string representation that explicitly renders the annotation state alongside the equivalent class expressions.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.class_axiom.equivalent_classes.OWLEquivalentClasses


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_axioms_class_axiom_equivalent_classes_OWLEquivalentClasses.png
       :alt: UML Class Diagram for OWLEquivalentClasses
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLEquivalentClasses**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_axioms_class_axiom_equivalent_classes_OWLEquivalentClasses.pdf
       :alt: UML Class Diagram for OWLEquivalentClasses
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLEquivalentClasses**

.. py:class:: OWLEquivalentClasses(expressions: list[pyowl2.abstracts.class_expression.OWLClassExpression], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.class_axiom.OWLClassAxiom`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.class_axiom.equivalent_classes.OWLEquivalentClasses
      :parts: 1
      :private-bases:


   This axiom defines a logical equivalence between two or more class expressions, asserting that they share the exact same set of instances within an ontology. It is utilized to model scenarios where distinct concepts are semantically identical, allowing reasoners to infer that any individual belonging to one class must also belong to all others declared equivalent. To construct this object, a user must provide a list containing at least two `OWLClassExpression` instances, along with an optional list of annotations for metadata. The implementation automatically sorts the provided expressions to maintain a canonical representation, ensuring that the order of input does not affect the identity of the axiom.

   :parm class_expressions: A sorted list of class expressions declared to be equivalent, containing at least two elements.
   :type class_expressions: list[OWLClassExpression]


   .. py:method:: __str__() -> str

      Returns a string representation of the OWL equivalent classes axiom using a functional-style syntax. The output string begins with 'EquivalentClasses' and includes the axiom annotations; if no annotations are present, an empty list '[]' is explicitly rendered. The class expressions defining the equivalence are converted to strings and concatenated with spaces to complete the representation.

      :return: A string representation of the equivalent classes axiom, including its annotations and class expressions.

      :rtype: str



   .. py:attribute:: _class_expressions
      :type:  list[pyowl2.abstracts.class_expression.OWLClassExpression]


   .. py:property:: class_expressions
      :type: list[pyowl2.abstracts.class_expression.OWLClassExpression]


      Sets the list of class expressions that are declared equivalent within this axiom. The provided list of OWLClassExpression objects is sorted prior to storage to maintain a consistent internal order. This method replaces any existing class expressions currently held by the object.

      :param value: The OWL class expressions to assign. The list will be sorted before being stored.
      :type value: list[OWLClassExpression]

