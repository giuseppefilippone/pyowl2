pyowl2.expressions.object_property
==================================

.. py:module:: pyowl2.expressions.object_property



.. ── LLM-GENERATED DESCRIPTION START ──

Models an OWL Object Property as a binary relation connecting two individuals within an ontology, including support for universal top and bottom property vocabularies.


Description
-----------


The software defines a concrete implementation of an OWL Object Property, which functions as a binary relation connecting two individuals within an ontology. By inheriting from abstract base classes for entities and property expressions, it integrates into a larger framework for representing semantic web data structures. Instances are uniquely identified by an Internationalized Resource Identifier (IRI), which can be set or retrieved to manage the property's identity. The implementation also provides access to the universal top and bottom properties defined in the OWL vocabulary, allowing users to represent the most general and most specific relations respectively. Additionally, logic is included to determine whether a specific instance corresponds to these universal vocabulary elements, facilitating semantic reasoning and validation.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.expressions.object_property.OWLObjectProperty


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/pyowl2_expressions_object_property_OWLObjectProperty.png
       :alt: UML Class Diagram for OWLObjectProperty
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLObjectProperty**

.. only:: latex

    .. figure:: /_uml/pyowl2_expressions_object_property_OWLObjectProperty.pdf
       :alt: UML Class Diagram for OWLObjectProperty
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLObjectProperty**

.. py:class:: OWLObjectProperty(iri: Union[rdflib.URIRef, pyowl2.base.iri.IRI])

   Bases: :py:obj:`pyowl2.abstracts.entity.OWLEntity`, :py:obj:`pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression`

   .. autoapi-inheritance-diagram:: pyowl2.expressions.object_property.OWLObjectProperty
      :parts: 1
      :private-bases:


   This class models an OWL Object Property, which serves as a binary relation connecting two individuals within an ontology. Users can instantiate this class by providing an IRI (Internationalized Resource Identifier) that uniquely identifies the property, such as a URI representing "hasParent". Beyond standard instantiation, the class offers static methods to retrieve the universal top property and the empty bottom property, as well as instance methods to check if the current property corresponds to these specific OWL entities.

   :parm iri: Backing field for the public `iri` property, holding the Internationalized Resource Identifier (IRI) that uniquely identifies this object property within the ontology.
   :type iri: typing.Union[URIRef, IRI]


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the object property, formatted to display the entity type alongside its Internationalized Resource Identifier (IRI). This method is primarily used for debugging and logging, providing a concise summary that identifies the instance as an ObjectProperty and exposes its specific identifier. The operation has no side effects and relies on the internal `_iri` attribute to construct the output string.

      :return: A string representation of the object, formatted as 'ObjectProperty({iri})' where {iri} is the object's IRI.

      :rtype: str



   .. py:method:: bottom() -> Self
      :staticmethod:


      Returns the OWL 2 bottom object property, which represents the property that no pair of individuals instantiate. This static method constructs an `OWLObjectProperty` instance using the specific IRI defined in the OWL namespace for `owl:bottomObjectProperty`. It acts as the universal lower bound within the object property hierarchy and has no side effects.

      :return: Returns the OWL bottom object property (owl:bottomObjectProperty).

      :rtype: typing.Self



   .. py:method:: is_bottom_object_property() -> bool

      Checks if this object property instance is the bottom object property, which is the universal sub-property that relates no pairs of individuals. This method returns `True` if the current instance is identical to the static bottom property defined by the class, and `False` otherwise. It is a pure query method with no side effects.

      :return: True if this object property is the bottom object property, otherwise False.

      :rtype: bool



   .. py:method:: is_top_object_property() -> bool

      Determines whether the current object property instance is the universal top object property, which serves as the superclass of all object properties in OWL. This method performs a direct comparison against the specific entity representing the top property. It returns `True` if the instance is the top property, and `False` otherwise.

      :return: True if this property is the top object property, False otherwise.

      :rtype: bool



   .. py:method:: top() -> Self
      :staticmethod:


      Returns an instance representing the universal object property from the OWL vocabulary, which is the property that relates every individual to every other individual. This static method creates a new object property identified by the standard IRI `http://www.w3.org/2002/07/owl#topObjectProperty`. As the top element of the object property hierarchy, it acts as a superclass for all other specific object properties.

      :return: Returns an instance representing the OWL top object property (owl:topObjectProperty), which is the universal property relating all individuals.

      :rtype: typing.Self



   .. py:attribute:: _iri
      :type:  Union[rdflib.URIRef, pyowl2.base.iri.IRI]


   .. py:property:: iri
      :type: Union[rdflib.URIRef, pyowl2.base.iri.IRI]


      Sets the Internationalized Resource Identifier (IRI) for this OWL object property. The method accepts a value of type URIRef or IRI and assigns it to the internal `_iri` attribute, thereby updating the unique identifier of the entity. This operation directly modifies the object's state, changing how it is referenced within the ontology.

      :param value: The IRI or URI reference to assign to the object.
      :type value: typing.Union[URIRef, IRI]

