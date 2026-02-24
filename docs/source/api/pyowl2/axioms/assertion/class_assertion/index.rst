pyowl2.axioms.assertion.class_assertion
=======================================

.. py:module:: pyowl2.axioms.assertion.class_assertion



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a Python class representing an OWL Class Assertion axiom that links a specific individual to a class expression within an ontology.


Description
-----------


The software models a specific type of axiom found in the Web Ontology Language (OWL) used to declare that a named entity is an instance of a particular class or complex class expression. By inheriting from a base assertion class, it provides a structured way to encapsulate the relationship between an individual and a class expression, allowing for the attachment of optional metadata annotations to enrich the semantic data. Internal state management is handled through properties that permit the modification of both the class expression and the individual after the object has been created, ensuring flexibility in ontology construction. A string representation method generates a functional syntax output that clearly displays the assertion type, any associated annotations, the class expression, and the individual, facilitating debugging and serialization.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.assertion.class_assertion.OWLClassAssertion


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_axioms_assertion_class_assertion_OWLClassAssertion.png
       :alt: UML Class Diagram for OWLClassAssertion
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLClassAssertion**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_axioms_assertion_class_assertion_OWLClassAssertion.pdf
       :alt: UML Class Diagram for OWLClassAssertion
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLClassAssertion**

.. py:class:: OWLClassAssertion(expression: pyowl2.abstracts.class_expression.OWLClassExpression, individual: pyowl2.abstracts.individual.OWLIndividual, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.assertion.OWLAssertion`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.assertion.class_assertion.OWLClassAssertion
      :parts: 1
      :private-bases:


   This class represents a fundamental axiom in the Web Ontology Language (OWL) used to declare that a specific individual is an instance of a given class expression. It serves to classify entities within an ontology by linking an `OWLIndividual` to an `OWLClassExpression`, effectively stating that the individual belongs to the defined type. Users can instantiate this object to define type relationships, optionally providing a list of annotations to attach metadata to the assertion itself. The component allows for the modification of both the class expression and the individual after instantiation through its properties, and it integrates into the broader ontology structure by inheriting from `OWLAssertion`.

   :param class_expression: The class expression that the individual is asserted to be an instance of.
   :type class_expression: OWLClassExpression
   :param individual: The specific entity that is asserted to be an instance of the class expression.
   :type individual: OWLIndividual


   .. py:method:: __str__() -> str

      Returns a string representation of the class assertion axiom using a functional syntax format. The string includes the axiom annotations, the class expression, and the individual. If the object has no annotations, the representation explicitly includes an empty list placeholder to preserve the structural format.

      :return: A string representation of the class assertion, formatted as "ClassAssertion([annotations] class_expression individual)".

      :rtype: str



   .. py:attribute:: _class_expression
      :type:  pyowl2.abstracts.class_expression.OWLClassExpression


   .. py:attribute:: _individual
      :type:  pyowl2.abstracts.individual.OWLIndividual


   .. py:property:: class_expression
      :type: pyowl2.abstracts.class_expression.OWLClassExpression


      Updates the class expression associated with this OWL class assertion by assigning the provided value. This operation overwrites the existing class expression stored internally, effectively changing the type or classification being asserted. The method expects an instance of OWLClassExpression as input to ensure the structural integrity of the axiom.

      :param value: The class expression to assign to this object.
      :type value: OWLClassExpression


   .. py:property:: individual
      :type: pyowl2.abstracts.individual.OWLIndividual


      Assigns the specified individual to this class assertion axiom, replacing any previously associated individual. This method updates the internal state of the object to reflect that the provided OWLIndividual is the subject of the assertion. It acts as a direct mutator and does not return a value.

      :param value: The OWL individual instance to assign.
      :type value: OWLIndividual

