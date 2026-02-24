pyowl2.axioms.class_axiom.disjoint_classes
==========================================

.. py:module:: pyowl2.axioms.class_axiom.disjoint_classes



.. ── LLM-GENERATED DESCRIPTION START ──

Implements the OWL DisjointClasses axiom to enforce mutual exclusion among a set of class expressions within an ontology.


Description
-----------


The software models the semantic constraint that no individual can simultaneously belong to more than one class in a specified collection, a fundamental concept in ontology engineering known as the DisjointClasses axiom. By inheriting from a base class axiom, it integrates seamlessly into the broader ontology structure while enforcing strict validation rules, such as requiring a minimum of two class expressions to define a meaningful disjointness relationship. Internally, the implementation automatically sorts the provided class expressions to maintain a deterministic order, which aids in comparison and serialization processes. Optional metadata can be attached to the axiom through annotations, and the logic includes a string representation method that outputs the structure in standard OWL functional syntax.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.class_axiom.disjoint_classes.OWLDisjointClasses


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_axioms_class_axiom_disjoint_classes_OWLDisjointClasses.png
       :alt: UML Class Diagram for OWLDisjointClasses
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDisjointClasses**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_axioms_class_axiom_disjoint_classes_OWLDisjointClasses.pdf
       :alt: UML Class Diagram for OWLDisjointClasses
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDisjointClasses**

.. py:class:: OWLDisjointClasses(expressions: list[pyowl2.abstracts.class_expression.OWLClassExpression], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.class_axiom.OWLClassAxiom`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.class_axiom.disjoint_classes.OWLDisjointClasses
      :parts: 1
      :private-bases:


   This axiom defines a mutual exclusion relationship between two or more class expressions within an ontology, asserting that no individual can be an instance of more than one of the specified classes simultaneously. To utilize this entity, instantiate it with a list of `OWLClassExpression` objects, ensuring the list contains at least two elements; the implementation automatically sorts these expressions to maintain a consistent internal order. Optional annotations can be attached to provide metadata about the axiom itself, such as provenance or confidence scores.

   :param class_expressions: The sorted list of class expressions involved in the disjointness axiom.
   :type class_expressions: list[OWLClassExpression]


   .. py:method:: __str__() -> str

      Returns a string representation of the disjoint classes axiom formatted in a functional syntax style. The output begins with the keyword 'DisjointClasses' followed by the list of axiom annotations; if no annotations are present, an empty list is explicitly included. The string concludes with the space-separated string representations of all class expressions involved in the disjointness relationship.

      :return: A string representation of the DisjointClasses axiom in functional syntax, including the axiom annotations and the list of class expressions.

      :rtype: str



   .. py:attribute:: _class_expressions
      :type:  list[pyowl2.abstracts.class_expression.OWLClassExpression]


   .. py:property:: class_expressions
      :type: list[pyowl2.abstracts.class_expression.OWLClassExpression]


      Replaces the current collection of class expressions with the provided list of OWLClassExpression objects. This setter normalizes the input by sorting the elements before storing them in the private attribute, ensuring a deterministic internal order regardless of the input sequence. The operation modifies the object in place and returns None.

      :param value: A list of OWL class expressions to assign. The list will be sorted before being stored.
      :type value: list[OWLClassExpression]

