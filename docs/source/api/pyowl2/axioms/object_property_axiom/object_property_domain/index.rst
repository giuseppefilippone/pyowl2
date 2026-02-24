pyowl2.axioms.object_property_axiom.object_property_domain
==========================================================

.. py:module:: pyowl2.axioms.object_property_axiom.object_property_domain



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a representation for the Web Ontology Language axiom that restricts the domain of an object property to a specific class expression.


Description
-----------


The software models a specific type of Web Ontology Language (OWL) axiom used to define the domain of an object property, ensuring that any individual acting as the subject of a relationship belongs to a specified class. By inheriting from a base axiom class, it integrates standard annotation handling capabilities while introducing specific attributes to hold the object property expression and the class expression that defines the domain constraint. The design allows for the dynamic assignment and retrieval of both the property and the class expression, enabling the construction of complex ontological rules where the validity of property assertions depends on the type of the source individual. Furthermore, the implementation includes a string conversion mechanism that outputs the axiom in a functional syntax format, which is useful for serialization, debugging, or interoperability with other OWL tools.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.object_property_axiom.object_property_domain.OWLObjectPropertyDomain


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_axioms_object_property_axiom_object_property_domain_OWLObjectPropertyDomain.png
       :alt: UML Class Diagram for OWLObjectPropertyDomain
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLObjectPropertyDomain**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_axioms_object_property_axiom_object_property_domain_OWLObjectPropertyDomain.pdf
       :alt: UML Class Diagram for OWLObjectPropertyDomain
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLObjectPropertyDomain**

.. py:class:: OWLObjectPropertyDomain(property: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression, expression: pyowl2.abstracts.class_expression.OWLClassExpression, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.object_property_axiom.OWLObjectPropertyAxiom`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.object_property_axiom.object_property_domain.OWLObjectPropertyDomain
      :parts: 1
      :private-bases:


   This class models an axiom within the Web Ontology Language (OWL) that constrains the types of individuals which may serve as the subject of a specific object property relationship. By associating an object property expression with a class expression, it asserts that any individual linked to another via the specified property must belong to the defined class. Users can instantiate this class by providing the target property, the defining class expression, and an optional list of annotations to attach metadata to the axiom.

   :param object_property_expression: The object property expression for which the domain is being defined.
   :type object_property_expression: OWLObjectPropertyExpression
   :param class_expression: The class expression defining the domain of the object property, specifying the class of individuals that can be the subject of the property relationship.
   :type class_expression: OWLClassExpression


   .. py:method:: __str__() -> str

      Returns a string representation of the object property domain axiom in a functional syntax format. The output string begins with "ObjectPropertyDomain" followed by the axiom annotations, the object property expression, and the class expression, all enclosed in parentheses. If the object has associated annotations, they are included in the string; otherwise, an empty list representation is substituted in their place. This method does not modify the state of the object.

      :return: A string representation of the axiom in functional syntax, including annotations if available.

      :rtype: str



   .. py:attribute:: _class_expression
      :type:  pyowl2.abstracts.class_expression.OWLClassExpression


   .. py:attribute:: _object_property_expression
      :type:  pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


   .. py:property:: class_expression
      :type: pyowl2.abstracts.class_expression.OWLClassExpression


      Updates the domain class expression associated with this OWL object property domain axiom. It assigns the provided `OWLClassExpression` instance to the internal state, defining the specific class to which the property applies. This operation modifies the object's internal state by overwriting the existing class expression with the new value.

      :param value: The OWL class expression to assign.
      :type value: OWLClassExpression


   .. py:property:: object_property_expression
      :type: pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression


      Assigns the specified object property expression to this domain axiom, replacing any previously stored value. This method updates the internal state of the instance by setting the `_object_property_expression` attribute to the provided `OWLObjectPropertyExpression` instance. The operation directly mutates the object and does not return a value.

      :param value: The OWL object property expression to assign to the instance.
      :type value: OWLObjectPropertyExpression

