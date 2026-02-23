pyowl2.base.iri
===============

.. py:module:: pyowl2.base.iri



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a class representing an Internationalized Resource Identifier (IRI) that acts as a global identifier for entities within an OWL ontology by combining a namespace prefix with a specific local value.


Description
-----------


The software provides a robust mechanism for creating and managing Internationalized Resource Identifiers (IRIs) which function as unique global identifiers for ontology elements such as classes, properties, and individuals. By inheriting from abstract annotation interfaces, the implementation ensures compatibility with broader OWL data structures while leveraging the ``rdflib`` library to handle the underlying namespace logic and URI resolution. It encapsulates a namespace and a local value, allowing the conversion of these components into a standard ``URIRef`` object for seamless integration with RDF data stores. Furthermore, the design includes utility logic to recognize fundamental OWL concepts like ``owl:Thing`` and ``owl:Nothing``, and it implements standard comparison and hashing protocols based on the string representation of the identifier to support use in collections and sorting operations.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.base.iri.IRI


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/pyowl2_base_iri_IRI.png
       :alt: UML Class Diagram for IRI
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **IRI**

.. only:: latex

    .. figure:: /_uml/pyowl2_base_iri_IRI.pdf
       :alt: UML Class Diagram for IRI
       :align: center
       :width: 10.9cm
       :class: uml-diagram

       UML Class Diagram for **IRI**

.. py:class:: IRI(namespace: rdflib.Namespace, value: Union[str, rdflib.URIRef] = '')

   Bases: :py:obj:`pyowl2.abstracts.annotation_subject.OWLAnnotationSubject`, :py:obj:`pyowl2.abstracts.annotation_value.OWLAnnotationValue`

   .. autoapi-inheritance-diagram:: pyowl2.base.iri.IRI
      :parts: 1
      :private-bases:


   This class models an Internationalized Resource Identifier (IRI), acting as a global identifier for entities within an ontology by combining a namespace prefix with a specific local value. It is primarily used to reference classes, individuals, or properties in OWL structures and can be instantiated by providing a `Namespace` object and an optional string identifier. The class facilitates interaction with RDF data by offering a method to convert the IRI into a `URIRef`, while also providing utility methods to identify standard OWL entities such as `owl:Thing` and `owl:Nothing`. Comparisons and string representations are handled based on the full resolved identifier.

   :parm namespace: The base prefix or context for the identifier, representing a collection of related entities and combining with the specific value to construct the full Internationalized Resource Identifier.
   :type namespace: Namespace
   :parm value: The specific identifier for an entity, which can be a local string fragment combined with the namespace or a complete URI reference.
   :type value: typing.Union[str, URIRef]


   .. py:method:: __eq__(value: object) -> bool

      Determines equality between the current IRI and another object by comparing their string representations. This allows the IRI to be compared not only against other IRI instances but also against string objects or any other type that can be serialized to a string. The comparison relies on the specific output of the `__str__` method, meaning that two IRIs are considered equal if their serialized forms are identical, regardless of whether they are distinct objects in memory. This method does not modify the state of the IRI instance.

      :param value: The object to compare for equality. The comparison is performed based on the string representation of the object.
      :type value: object

      :return: True if the string representation of the instance equals the string representation of the provided value, otherwise False.

      :rtype: bool



   .. py:method:: __ge__(value: object) -> bool

      Compares the current IRI instance to another object to determine if it is greater than or equal to it based on lexicographical order. The comparison is performed by converting both the IRI and the provided value to their string representations. This method accepts any object type, relying on the standard string conversion of the argument, and does not modify the state of the IRI or the compared value.

      :param value: The object to compare against, evaluated via its string representation.
      :type value: object

      :return: True if the string representation of the object is greater than or equal to the string representation of the provided value, otherwise False.

      :rtype: bool



   .. py:method:: __gt__(value: object) -> bool

      Determines whether the current IRI instance is lexicographically greater than the provided object. The comparison is performed by converting both the IRI and the input value to their string representations and evaluating the standard greater-than relationship between them. This allows the IRI to be compared against other IRIs or arbitrary objects that support string conversion.

      :param value: The object to compare against the current instance, where the comparison is performed on the string representations of both objects.
      :type value: object

      :return: True if the string representation of the instance is lexicographically greater than the string representation of the provided value, otherwise False.

      :rtype: bool



   .. py:method:: __hash__() -> int

      Computes the hash value for the IRI instance by hashing its string representation, enabling the object to be used as a dictionary key or stored in a set. The implementation relies on the built-in hash function applied to the result of `str(self)`, ensuring that two IRIs with identical string representations yield the same hash. Because the hash is derived from the object's state, the IRI should be treated as immutable; if the internal components of the IRI are modified after hashing, the hash value will change, potentially causing the object to be lost in hash-based collections.

      :return: An integer representing the hash of the object's string representation.

      :rtype: int



   .. py:method:: __le__(value: object) -> bool

      Determines if the current IRI instance is lexicographically less than or equal to the provided object. The comparison is performed by converting both the current instance and the target value to their string representations and applying the standard less-than-or-equal-to operator. This allows the IRI to be compared against other IRI instances or arbitrary objects that can be cast to strings.

      :param value: The object to compare against, which is converted to a string for lexicographical comparison.
      :type value: object

      :return: True if the string representation of the instance is less than or equal to the string representation of the provided value, otherwise False.

      :rtype: bool



   .. py:method:: __lt__(value: object) -> bool

      Implements the less-than comparison operator for the IRI instance by evaluating the lexicographical order of their string representations. The method converts both the current object and the provided value to strings and returns True if the current instance's string is smaller. This allows the IRI to be compared against other IRIs, strings, or any object that can be cast to a string, enabling standard sorting and ordering operations.

      :param value: The object to compare against, converted to a string for comparison.
      :type value: object

      :return: True if the string representation of the current object is lexicographically less than the string representation of the provided value, otherwise False.

      :rtype: bool



   .. py:method:: __ne__(value: object) -> bool

      Determines whether the current IRI instance is not equal to a specified value. The comparison is performed by converting both the IRI and the provided value to their string representations and checking for inequality. This allows the IRI to be compared against other IRI objects or arbitrary strings based on their lexical content. If the string representations differ, the method returns True; otherwise, it returns False.

      :param value: The object to compare against. The comparison is performed based on the string representation of the value.
      :type value: object

      :return: True if the string representation of the object is not equal to the string representation of the specified value, otherwise False.

      :rtype: bool



   .. py:method:: __repr__() -> str

      Returns the official string representation of the IRI instance. This implementation delegates directly to the `__str__` method, resulting in the same output as the informal string conversion, which is typically the IRI string itself. It does not modify the object and has no side effects.

      :return: The string representation of the object.

      :rtype: str



   .. py:method:: __str__() -> str

      Returns the string representation of the IRI in its URI-encoded form. By delegating to the `to_uriref` method, this ensures that the returned string is a valid URI reference, typically involving the percent-encoding of any non-ASCII characters present in the IRI. This behavior makes the object compatible with contexts requiring standard ASCII URIs, such as HTTP headers or legacy systems, while the internal representation may retain the original Unicode characters.

      :return: The string representation of the URI reference.

      :rtype: str



   .. py:method:: is_owl_nothing() -> bool

      Checks if the current IRI corresponds to the OWL Nothing entity, which represents the empty class in Web Ontology Language (OWL) semantics. The method performs this check by converting the object to a URI reference and comparing it against the standard `owl:Nothing` constant. It returns `True` if the identifiers match exactly, and `False` otherwise, without modifying the state of the object.

      :return: True if the entity represents the OWL Nothing concept, False otherwise.

      :rtype: bool



   .. py:method:: is_owl_thing() -> bool

      Determines whether the current IRI corresponds to the universal class 'owl:Thing' within the Web Ontology Language (OWL). The method performs a strict equality check by converting the IRI instance to a URI reference and comparing it against the standard OWL.Thing constant. It returns True if the identifiers match exactly, and False otherwise. This operation is read-only and does not modify the state of the IRI object.

      :return: True if the object is the OWL Thing class, otherwise False.

      :rtype: bool



   .. py:method:: nothing_iri() -> Self
      :staticmethod:


      Returns an IRI instance representing the OWL concept of "Nothing," which denotes the empty class containing no instances. This static method constructs the IRI by combining the standard OWL namespace with the specific identifier for "Nothing," providing a convenient accessor for this fundamental ontology term. The method creates a new IRI object upon each invocation.

      :return: Returns the IRI for `owl:Nothing`.

      :rtype: typing.Self



   .. py:method:: thing_iri() -> Self
      :staticmethod:


      Returns an instance of the IRI class representing the `owl:Thing` concept, which serves as the root class of the class hierarchy in the OWL ontology. This static method generates the IRI by combining the standard OWL namespace with the specific identifier for 'Thing'. The function requires no arguments and has no side effects, simply providing a convenient way to access the IRI for the universal class.

      :return: Returns the IRI for `owl:Thing`.

      :rtype: typing.Self



   .. py:method:: to_uriref() -> rdflib.URIRef

      Converts the IRI instance into a concrete URIRef object by resolving it against the associated namespace. If the internal value is already a URIRef, it is returned directly; otherwise, the value is treated as a local identifier and used to construct a URIRef via the namespace. This method requires the `namespace` attribute to be a valid `Namespace` instance, raising an `AssertionError` if this condition is not met, and may propagate errors if the value cannot be resolved within the namespace context.

      :return: A `URIRef` representing the fully qualified URI. Returns the value directly if it is already a `URIRef`, otherwise resolves it against the associated namespace.

      :rtype: URIRef



   .. py:attribute:: _namespace
      :type:  rdflib.Namespace


   .. py:attribute:: _value
      :type:  Union[str, rdflib.URIRef]
      :value: ''



   .. py:property:: namespace
      :type: rdflib.Namespace


      Updates the namespace associated with the IRI instance by assigning the provided Namespace object to the internal state. This setter replaces any previously defined namespace, effectively altering the IRI's context or prefix mapping. The operation mutates the object in place and does not return a value.

      :param value: The Namespace object to assign to the instance.
      :type value: Namespace


   .. py:property:: value
      :type: Union[str, rdflib.URIRef]


      Updates the internal representation of the IRI by assigning the provided value to the private `_value` attribute. This setter accepts either a string or a URIRef object as input, performing no validation or type conversion before assignment. As a result, the internal state is modified directly to reflect the provided argument, regardless of whether it constitutes a valid IRI or matches the expected type strictly.

      :param value: The full IRI to set, provided as either a string or a URIRef.
      :type value: typing.Union[str, URIRef]

