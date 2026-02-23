pyowl2.axioms.data_property_axiom.equivalent_data_properties
============================================================

.. py:module:: pyowl2.axioms.data_property_axiom.equivalent_data_properties



.. ── LLM-GENERATED DESCRIPTION START ──

Implements an OWL axiom structure to declare that a set of data properties share the same extension and are therefore interchangeable.


Description
-----------


The software models a specific type of Web Ontology Language (OWL) axiom used to define that multiple data properties are semantically equivalent, meaning they refer to the same set of data assertions. By requiring a minimum of two property expressions upon initialization, the implementation ensures logical validity, while automatically sorting these expressions to maintain a canonical internal state regardless of the input order. This design allows for the attachment of optional metadata annotations, facilitating the enrichment of the axiom with additional context or information. The internal logic normalizes the representation of equivalent properties, which aids in comparison operations and ensures consistent structural output when the object is converted to a string.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.data_property_axiom.equivalent_data_properties.OWLEquivalentDataProperties


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_axioms_data_property_axiom_equivalent_data_properties_OWLEquivalentDataProperties.png
       :alt: UML Class Diagram for OWLEquivalentDataProperties
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLEquivalentDataProperties**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_axioms_data_property_axiom_equivalent_data_properties_OWLEquivalentDataProperties.pdf
       :alt: UML Class Diagram for OWLEquivalentDataProperties
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLEquivalentDataProperties**

.. py:class:: OWLEquivalentDataProperties(expressions: list[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.data_property_axiom.OWLDataPropertyAxiom`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.data_property_axiom.equivalent_data_properties.OWLEquivalentDataProperties
      :parts: 1
      :private-bases:


   This class represents an OWL axiom asserting that two or more data properties share the same property extension, effectively treating them as synonyms for the purpose of data assertions. To utilize this class, instantiate it with a list of `OWLDataPropertyExpression` objects containing at least two members, optionally accompanied by a list of `OWLAnnotation` objects for metadata. It is important to note that the class enforces a minimum of two properties and automatically sorts the provided expressions upon initialization and assignment to maintain a consistent internal state.

   :parm data_property_expressions: Internal list of data property expressions declared to be equivalent, maintained in sorted order.
   :type data_property_expressions: list[OWLDataPropertyExpression]


   .. py:method:: __str__() -> str

      Generates a human-readable string representation of the OWL equivalent data properties axiom. The output formats the axiom as a pseudo-function call containing the list of annotations, displaying an empty list if none are present, followed by the space-separated string representations of the data property expressions. This method is primarily used for debugging or logging purposes to visualize the structure of the axiom.

      :return: A string representation of the object, displaying the axiom annotations and the list of data property expressions.

      :rtype: str



   .. py:attribute:: _data_property_expressions
      :type:  list[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression]


   .. py:property:: data_property_expressions
      :type: list[pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression]


      Updates the set of data property expressions that constitute this equivalence axiom. The provided list is sorted before being assigned to the internal attribute, ensuring a consistent canonical order. This operation overwrites the previously stored collection of expressions.

      :param value: A list of OWL data property expressions to assign to the object.
      :type value: list[OWLDataPropertyExpression]

