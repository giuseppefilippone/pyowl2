pyowl2.axioms.object_property_axiom.functional_object_property
==============================================================

.. py:module:: pyowl2.axioms.object_property_axiom.functional_object_property



.. ── LLM-GENERATED DESCRIPTION START ──

Represents an OWL axiom asserting that a specific object property is functional, meaning it relates an individual to at most one other individual.


Description
-----------


The implementation enforces the semantic constraint that any given subject entity can be associated with a maximum of one distinct object entity through the specified property. By inheriting from the base object property axiom class, it integrates seamlessly into the broader ontology structure while allowing for the attachment of metadata via annotations. The internal state manages the specific property expression, which can be a named property or an inverse property, ensuring that reasoners can infer uniqueness or identity based on these relationships. A string representation method generates the axiom in functional syntax, facilitating debugging or serialization by explicitly listing annotations and the constrained property.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.object_property_axiom.functional_object_property.OWLFunctionalObjectProperty


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_axioms_object_property_axiom_functional_object_property_OWLFunctionalObjectProperty.png
       :alt: UML Class Diagram for OWLFunctionalObjectProperty
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLFunctionalObjectProperty**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_axioms_object_property_axiom_functional_object_property_OWLFunctionalObjectProperty.pdf
       :alt: UML Class Diagram for OWLFunctionalObjectProperty
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLFunctionalObjectProperty**

.. py:class:: OWLFunctionalObjectProperty(expression: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.object_property_axiom.OWLObjectPropertyAxiom`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.object_property_axiom.functional_object_property.OWLFunctionalObjectProperty
      :parts: 1
      :private-bases:


   This axiom defines a constraint within an ontology stating that a specific object property is functional, meaning any given individual can be linked to at most one other individual via this property. Semantically, this allows reasoners to infer that if an individual is related to two distinct entities through this property, those entities must be identical (for example, if a person has two social security numbers, the numbers must refer to the same identifier). To utilize this, instantiate the class with the target `OWLObjectPropertyExpression` and an optional list of `OWLAnnotation` objects to provide metadata about the axiom itself.

   :parm object_property_expression: The object property expression that is declared to be functional, meaning it can relate an individual to at most one other individual.
   :type object_property_expression: OWLObjectPropertyExpression


   .. py:method:: __str__() -> str

      Returns a string representation of the axiom, formatted in a functional syntax style. The output string begins with the keyword 'FunctionalObjectProperty' and includes the object property expression associated with the instance. If the instance contains axiom annotations, they are included in the string; otherwise, an empty list is displayed in their place.

      :return: A string representation of the axiom in functional syntax, including the annotations and the object property expression.

      :rtype: str



   .. py:attribute:: _object_property_expression
      :type:  pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


   .. py:property:: object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Assigns the provided object property expression to this instance, defining the specific property that is subject to the functional constraint. This method updates the internal state of the axiom by replacing the existing property expression with the new value. It expects an `OWLObjectPropertyExpression` as input, ensuring that the axiom refers to a valid object property within the ontology.

      :param value: The OWL object property expression to assign.
      :type value: OWLObjectPropertyExpression

