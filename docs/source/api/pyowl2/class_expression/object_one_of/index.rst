pyowl2.class_expression.object_one_of
=====================================

.. py:module:: pyowl2.class_expression.object_one_of



.. ── LLM-GENERATED DESCRIPTION START ──

An implementation of the OWL ObjectOneOf class expression that defines a class by explicitly enumerating a finite set of individuals.


Description
-----------


The software models a specific type of class expression found in the Web Ontology Language (OWL) where a class is defined strictly by the explicit listing of its member instances. By requiring a non-empty collection of individuals during initialization, the logic enforces that an enumeration must contain at least one element, preventing the creation of empty class definitions through this mechanism. To maintain a canonical and predictable internal state, the implementation automatically sorts the provided individuals whenever the collection is set or modified, ensuring that the order of input does not affect the identity of the logical construct. This design facilitates consistent comparisons and storage, while the string representation adheres to standard functional syntax, making the output suitable for parsing or display in ontology engineering tools.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.class_expression.object_one_of.OWLObjectOneOf


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_class_expression_object_one_of_OWLObjectOneOf.png
       :alt: UML Class Diagram for OWLObjectOneOf
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLObjectOneOf**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_class_expression_object_one_of_OWLObjectOneOf.pdf
       :alt: UML Class Diagram for OWLObjectOneOf
       :align: center
       :width: 9.9cm
       :class: uml-diagram

       UML Class Diagram for **OWLObjectOneOf**

.. py:class:: OWLObjectOneOf(individuals: list[pyowl2.abstracts.individual.OWLIndividual])

   Bases: :py:obj:`pyowl2.abstracts.class_expression.OWLClassExpression`

   .. autoapi-inheritance-diagram:: pyowl2.class_expression.object_one_of.OWLObjectOneOf
      :parts: 1
      :private-bases:


   This class represents an enumeration class expression, which defines a specific class by explicitly listing a finite set of individuals as its members. It is used to assert that the class extension consists exactly of the provided instances, allowing for the precise definition of classes based on specific entities rather than general properties. When initializing this expression, a non-empty list of `OWLIndividual` objects must be provided; the class automatically sorts these individuals internally to ensure a canonical representation. As a subclass of `OWLClassExpression`, it can be utilized in complex logical constructs where a specific set of instances needs to be referenced as a class.

   :param individuals: The sorted list of individuals explicitly enumerated as members of the class expression.
   :type individuals: list[OWLIndividual]


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the object enumeration, formatted using the standard functional syntax. The method concatenates the string representations of all contained individuals, separated by spaces, and encloses them within 'ObjectOneOf(...)'. If the collection of individuals is empty, the method returns 'ObjectOneOf()'.

      :return: A string representation of the object, formatted as "ObjectOneOf(...)" containing the space-separated string representations of the individuals.

      :rtype: str



   .. py:attribute:: _individuals
      :type:  list[pyowl2.abstracts.individual.OWLIndividual]


   .. py:property:: individuals
      :type: list[pyowl2.abstracts.individual.OWLIndividual]


      Replaces the current set of individuals defining this OWL enumeration with the provided list. The method sorts the input list of OWLIndividual objects before assigning them to the internal attribute, thereby enforcing a canonical order for the stored individuals.

      :param value: A list of OWL individuals to be stored. The list is sorted before assignment.
      :type value: list[OWLIndividual]

