pyowl2.axioms.object_property_axiom.symmetric_object_property
=============================================================

.. py:module:: pyowl2.axioms.object_property_axiom.symmetric_object_property



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a data structure representing the Web Ontology Language axiom that declares an object property to be symmetric.


Description
-----------


Models the semantic rule where a relationship between two entities holds true in both directions, such as in sibling or spouse relationships. By extending the base axiom class, the software integrates seamlessly into the broader ontology framework while allowing for the attachment of supplementary metadata through optional annotations. The core logic involves storing a specific object property expression, which defines the scope of the symmetry constraint enforced by the ontology. A string representation method generates the axiom in functional syntax, ensuring the output adheres to standard serialization formats used in semantic web applications.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.object_property_axiom.symmetric_object_property.OWLSymmetricObjectProperty


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_axioms_object_property_axiom_symmetric_object_property_OWLSymmetricObjectProperty.png
       :alt: UML Class Diagram for OWLSymmetricObjectProperty
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLSymmetricObjectProperty**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_axioms_object_property_axiom_symmetric_object_property_OWLSymmetricObjectProperty.pdf
       :alt: UML Class Diagram for OWLSymmetricObjectProperty
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLSymmetricObjectProperty**

.. py:class:: OWLSymmetricObjectProperty(expression: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.object_property_axiom.OWLObjectPropertyAxiom`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.object_property_axiom.symmetric_object_property.OWLSymmetricObjectProperty
      :parts: 1
      :private-bases:


   This class models an axiom in the Web Ontology Language (OWL) that asserts the symmetric nature of an object property. Semantically, it enforces the rule that if a specific property connects entity A to entity B, it must also connect entity B to entity A, which is characteristic of relationships like 'isSiblingOf' or 'isSpouseOf'. Users can instantiate this object by providing the target object property expression, and optionally include a list of annotations to attach supplementary metadata or context to the axiom.

   :param object_property_expression: The object property expression that is asserted to be symmetric by this axiom.
   :type object_property_expression: OWLObjectPropertyExpression


   .. py:method:: __str__() -> str

      Returns a string representation of the symmetric object property axiom formatted in a functional syntax style. The output string begins with the axiom type followed by the list of annotations; if no annotations are present, an empty list is explicitly displayed. The representation concludes with the object property expression to which the symmetry property applies.

      :return: A string representation of the axiom, formatted as 'SymmetricObjectProperty([annotations] object_property_expression)'.

      :rtype: str



   .. py:attribute:: _object_property_expression
      :type:  pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


   .. py:property:: object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Assigns the specified object property expression to this symmetric object property instance, updating the internal state to reflect the new property that is being defined as symmetric. The provided value must be an instance of `OWLObjectPropertyExpression`, and this operation will overwrite any previously stored expression.

      :param value: The OWL object property expression to assign.
      :type value: OWLObjectPropertyExpression

