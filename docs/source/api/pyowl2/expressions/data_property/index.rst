pyowl2.expressions.data_property
================================

.. py:module:: pyowl2.expressions.data_property



.. ── LLM-GENERATED DESCRIPTION START ──

A Python implementation of an OWL data property that associates ontology individuals with literal data values using a unique Internationalized Resource Identifier.


Description
-----------


It defines a structure for representing data properties within the Web Ontology Language, specifically those that connect individual entities to concrete data values like integers or strings rather than other objects. Central to this design is the use of an Internationalized Resource Identifier (IRI) as the primary means of identification, ensuring that each property can be uniquely referenced and distinguished within a semantic graph. The implementation provides access to standard OWL vocabulary terms, specifically the universal top data property and the empty bottom data property, through static factory methods that encapsulate the creation of these specific system entities. Utility logic is included to verify whether a given instance corresponds to these special system properties, facilitating logical reasoning and validation tasks within the broader ontology framework. By inheriting from base entity and expression classes, the component integrates seamlessly into a larger library designed for manipulating and querying semantic web data structures.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.expressions.data_property.OWLDataProperty


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_expressions_data_property_OWLDataProperty.png
       :alt: UML Class Diagram for OWLDataProperty
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDataProperty**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_expressions_data_property_OWLDataProperty.pdf
       :alt: UML Class Diagram for OWLDataProperty
       :align: center
       :width: 13.3cm
       :class: uml-diagram

       UML Class Diagram for **OWLDataProperty**

.. py:class:: OWLDataProperty(iri: Union[rdflib.URIRef, pyowl2.base.iri.IRI])

   Bases: :py:obj:`pyowl2.abstracts.entity.OWLEntity`, :py:obj:`pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression`

   .. autoapi-inheritance-diagram:: pyowl2.expressions.data_property.OWLDataProperty
      :parts: 1
      :private-bases:


   This class represents a property within an ontology that associates an individual entity with a literal data value, such as a string, integer, or date, rather than linking to another individual. It is uniquely identified by an Internationalized Resource Identifier (IRI), which acts as its canonical name and allows it to be referenced in axioms and assertions. Instances can be created by specifying an IRI, or users can retrieve the universal and empty data properties using the static `top` and `bottom` methods. The class also includes functionality to determine if a specific instance corresponds to these special system properties, which is useful for logical reasoning and ontology validation.

   :parm iri: The Internationalized Resource Identifier that uniquely identifies this data property within the ontology. It serves as the primary identifier for the entity, enabling its use in axioms, assertions, and logical comparisons.
   :type iri: typing.Union[URIRef, IRI]


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the data property, formatted to include the class name and the associated Internationalized Resource Identifier (IRI). The output follows the pattern "DataProperty({iri})", making it suitable for debugging and logging purposes. This method does not modify the object's state and relies on the internal `_iri` attribute being defined and convertible to a string.

      :return: A string representation of the object, formatted as 'DataProperty({iri})' where {iri} is the object's IRI.

      :rtype: str



   .. py:method:: bottom() -> Self
      :staticmethod:


      Returns the standard OWL entity representing the bottom data property, which is the data property that has no instances. This static method constructs an instance using the specific IRI `owl:bottomDataProperty` from the OWL namespace. It serves as a factory for accessing this built-in vocabulary term, creating a new object instance on each invocation without side effects.

      :return: Returns the OWL bottom data property.

      :rtype: typing.Self



   .. py:method:: is_bottom_data_property() -> bool

      Determines whether the current data property instance represents the bottom data property within the OWL ontology hierarchy. The bottom data property is the most specific concept in the hierarchy, often corresponding to the empty set or a property that no individual possesses. This method performs a direct equality comparison against the canonical bottom data property instance and returns True if they match, otherwise False.

      :return: True if this data property is the bottom data property, False otherwise.

      :rtype: bool



   .. py:method:: is_top_data_property() -> bool

      Determines whether this data property instance represents the top data property, which is the universal property encompassing all data properties in the ontology. The method returns `True` if the instance is identical to the class-level definition of the top property, and `False` otherwise. This check is performed without modifying the state of the object.

      :return: True if this data property is the top data property, False otherwise.

      :rtype: bool



   .. py:method:: top() -> Self
      :staticmethod:


      Returns the instance representing the universal data property defined in the OWL 2 specification. This static method constructs an entity using the specific IRI for `owl:topDataProperty` within the standard OWL namespace. Semantically, this property serves as the most general data property, being a super-property of every other data property in the ontology.

      :return: Returns the OWL top data property instance, representing the universal super-property of all data properties.

      :rtype: typing.Self



   .. py:attribute:: _iri
      :type:  Union[rdflib.URIRef, pyowl2.base.iri.IRI]


   .. py:property:: iri
      :type: Union[rdflib.URIRef, pyowl2.base.iri.IRI]


      Sets the Internationalized Resource Identifier (IRI) for the OWL data property instance. This method accepts a value of type `URIRef` or `IRI` and assigns it to the internal `_iri` attribute, effectively updating the unique identifier of the property. Changing the IRI modifies the core identity of the entity, which may impact its resolution and relationships within an ontology graph.

      :param value: The IRI or URI reference to assign to the object.
      :type value: typing.Union[URIRef, IRI]

