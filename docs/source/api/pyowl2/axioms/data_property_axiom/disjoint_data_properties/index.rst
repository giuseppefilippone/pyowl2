pyowl2.axioms.data_property_axiom.disjoint_data_properties
==========================================================

.. py:module:: pyowl2.axioms.data_property_axiom.disjoint_data_properties



.. ── LLM-GENERATED DESCRIPTION START ──

Models an OWL axiom asserting that a specific set of data properties are mutually disjoint, ensuring no individual shares the same literal value across them.


Description
-----------


The implementation enforces a strict requirement that at least two property expressions must be provided during initialization, and it automatically sorts these expressions to guarantee a canonical internal representation regardless of input order. By inheriting from the base axiom class, the logic supports the inclusion of optional annotations, enabling the attachment of metadata to the logical constraint. Additionally, a string representation is provided in functional syntax style, which explicitly formats the output to display annotations and the sorted list of properties for readability and serialization purposes.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.data_property_axiom.disjoint_data_properties.OWLDisjointDataProperties


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_axioms_data_property_axiom_disjoint_data_properties_OWLDisjointDataProperties.png
       :alt: UML Class Diagram for OWLDisjointDataProperties
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDisjointDataProperties**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_axioms_data_property_axiom_disjoint_data_properties_OWLDisjointDataProperties.pdf
       :alt: UML Class Diagram for OWLDisjointDataProperties
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDisjointDataProperties**

.. py:class:: OWLDisjointDataProperties(expressions: list[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.data_property_axiom.OWLDataPropertyAxiom`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.data_property_axiom.disjoint_data_properties.OWLDisjointDataProperties
      :parts: 1
      :private-bases:


   This class models an axiom within an OWL ontology that declares a set of data properties to be mutually disjoint. Semantically, this implies that no single individual can possess the same literal value for any two properties included in the set. To utilize this class, instantiate it with a list containing at least two `OWLDataPropertyExpression` objects; an optional list of annotations may be provided to attach metadata to the axiom. Note that the class enforces a minimum of two properties and automatically sorts the provided expressions to ensure consistent representation.

   :param data_property_expressions: The sorted list of two or more data properties involved in the axiom, representing properties that are mutually exclusive in their values for any individual.
   :type data_property_expressions: list[OWLDataPropertyExpression]


   .. py:method:: __str__() -> str

      Returns a string representation of the axiom formatted in a functional syntax style. The output always includes a list structure for annotations, displaying the actual annotations if present or an empty list otherwise. Following the annotations, the method appends the string representations of all associated data property expressions, joined by spaces.

      :return: A string representation of the object, formatted as a constructor-like call including any annotations and the list of data property expressions.

      :rtype: str



   .. py:attribute:: _data_property_expressions
      :type:  list[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression]


   .. py:property:: data_property_expressions
      :type: list[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression]


      Assigns a new collection of data property expressions to this disjointness axiom. The provided list is sorted before being stored to ensure a consistent internal representation, effectively discarding the original order of the input elements.

      :param value: The OWL data property expressions to assign. The provided list will be sorted before storage.
      :type value: list[OWLDataPropertyExpression]

