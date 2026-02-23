pyowl2.axioms.object_property_axiom.inverse_functional_object_property
======================================================================

.. py:module:: pyowl2.axioms.object_property_axiom.inverse_functional_object_property



.. ── LLM-GENERATED DESCRIPTION START ──

Defines an OWL axiom that enforces a uniqueness constraint on an object property by ensuring that no two distinct individuals can relate to the same target individual via that property.


Description
-----------


The implementation models the Web Ontology Language concept of an inverse-functional object property, which imposes a semantic constraint ensuring that a specific property maps a target individual back to a unique source individual. By asserting this axiom, a reasoner can infer that if two distinct entities are found to be related to the same individual via the defined property, those entities must actually be identical. This behavior is essential for representing unique identifiers, such as social security numbers or email addresses, where a single value should correspond to exactly one entity within the domain.

Structurally, the class inherits from a base object property axiom to leverage common functionality for handling metadata and annotations. It encapsulates the specific property expression being constrained and allows for the attachment of optional annotations to provide further context or documentation. Furthermore, the logic includes a string representation method that outputs the axiom in a format resembling OWL functional syntax, facilitating easier debugging and interoperability with other semantic web tools.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.object_property_axiom.inverse_functional_object_property.OWLInverseFunctionalObjectProperty


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/pyowl2_axioms_object_property_axiom_inverse_functional_object_property_OWLInverseFunctionalObjectProperty.png
       :alt: UML Class Diagram for OWLInverseFunctionalObjectProperty
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLInverseFunctionalObjectProperty**

.. only:: latex

    .. figure:: /_uml/pyowl2_axioms_object_property_axiom_inverse_functional_object_property_OWLInverseFunctionalObjectProperty.pdf
       :alt: UML Class Diagram for OWLInverseFunctionalObjectProperty
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLInverseFunctionalObjectProperty**

.. py:class:: OWLInverseFunctionalObjectProperty(expression: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.object_property_axiom.OWLObjectPropertyAxiom`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.object_property_axiom.inverse_functional_object_property.OWLInverseFunctionalObjectProperty
      :parts: 1
      :private-bases:


   This class represents an axiom within the Web Ontology Language (OWL) that declares a specific object property to be inverse-functional. Semantically, this imposes a uniqueness constraint such that if two individuals are found to be related to the same target individual through this property, a reasoner must infer that the two individuals are actually identical. This is commonly used to model unique identifiers, such as social security numbers or email addresses, where a specific value should map back to a single entity. To utilize this class, instantiate it with the target `OWLObjectPropertyExpression` and, optionally, a list of annotations to provide additional metadata about the axiom.

   :parm object_property_expression: The specific property that is declared to be inverse functional, ensuring that if two individuals are related to the same individual via this property, they must be the same individual.
   :type object_property_expression: OWLObjectPropertyExpression


   .. py:method:: __str__() -> str

      Returns a string representation of the inverse functional object property axiom, formatted in a style resembling OWL functional syntax. The method constructs the string by combining the axiom type identifier with the associated annotations and the object property expression. If annotations are present, they are included in the output; otherwise, an empty list is explicitly rendered to ensure the structure remains consistent.

      :return: A string representation of the inverse functional object property axiom in functional syntax, including the annotations and the object property expression.

      :rtype: str



   .. py:attribute:: _object_property_expression
      :type:  pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


   .. py:property:: object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Assigns the specified object property expression to this inverse functional object property axiom, replacing any previously held value. The input value represents the specific property that is being asserted to have inverse functionality within the ontology. This method mutates the instance's state by updating the internal reference to the provided expression.

      :param value:
      :type value: OWLObjectPropertyExpression

