pyowl2.axioms.data_property_axiom.functional_data_property
==========================================================

.. py:module:: pyowl2.axioms.data_property_axiom.functional_data_property



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a class representing an OWL axiom that enforces a functional constraint on data properties, ensuring an individual has at most one value for a specific attribute.


Description
-----------


The implementation models a specific type of Web Ontology Language (OWL) axiom used to declare that a data property is functional, meaning any given individual can be associated with at most one distinct data value through that property. By extending the base axiom class, it integrates into the broader ontology structure while enforcing a uniqueness constraint where multiple values assigned to the same individual are inferred to be identical. The design allows for the attachment of optional metadata annotations and stores the target data property expression, providing mechanisms to access and modify this core component. Additionally, the logic includes a string representation method that outputs the axiom in standard functional syntax, facilitating debugging, logging, or serialization tasks.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.data_property_axiom.functional_data_property.OWLFunctionalDataProperty


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_axioms_data_property_axiom_functional_data_property_OWLFunctionalDataProperty.png
       :alt: UML Class Diagram for OWLFunctionalDataProperty
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLFunctionalDataProperty**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_axioms_data_property_axiom_functional_data_property_OWLFunctionalDataProperty.pdf
       :alt: UML Class Diagram for OWLFunctionalDataProperty
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLFunctionalDataProperty**

.. py:class:: OWLFunctionalDataProperty(property: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.data_property_axiom.OWLDataPropertyAxiom`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.data_property_axiom.functional_data_property.OWLFunctionalDataProperty
      :parts: 1
      :private-bases:


   This class models an axiom used to define a data property as functional, meaning that any individual in the ontology can be associated with at most one distinct data value through that specific property. It enforces a uniqueness constraint where, if an individual is linked to multiple values, those values are inferred to be identical. Users can instantiate this object by providing the target data property expression and, optionally, a list of annotations to attach metadata to the axiom itself. This construct is essential for representing attributes that must have a single value, such as a unique identifier or a specific measurement, within an OWL ontology.

   :param data_property_expression: The data property expression that is declared to be functional.
   :type data_property_expression: OWLDataPropertyExpression


   .. py:method:: __str__() -> str

      Returns a string representation of the functional data property axiom in a functional syntax format. The output string includes the keyword 'FunctionalDataProperty' followed by the axiom annotations and the data property expression. If the object contains no annotations, the representation explicitly includes an empty list placeholder. This method does not modify the object's state and is intended for display or logging purposes.

      :return: The functional syntax string representation of the axiom, including annotations and the data property expression.

      :rtype: str



   .. py:attribute:: _data_property_expression
      :type:  pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression


   .. py:property:: data_property_expression
      :type: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression


      Assigns the specified data property expression to this functional data property instance. This method updates the internal state by replacing the existing property expression with the provided value, effectively defining which data property is constrained by the functional characteristic.

      :param value: The data property expression to assign.
      :type value: OWLDataPropertyExpression

