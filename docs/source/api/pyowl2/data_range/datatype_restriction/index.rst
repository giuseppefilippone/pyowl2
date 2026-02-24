pyowl2.data_range.datatype_restriction
======================================

.. py:module:: pyowl2.data_range.datatype_restriction



.. ── LLM-GENERATED DESCRIPTION START ──

Implements the logic for creating datatype restrictions in OWL ontologies by applying specific facet constraints to base datatypes.


Description
-----------


The software provides a mechanism to narrow the value space of standard datatypes by applying specific constraints, such as minimum or maximum values, which are essential for defining precise data characteristics in semantic web applications. It introduces an enumeration for standard facet types and a class to represent individual constraints, ensuring that only valid XML Schema Definition (XSD) restrictions are utilized during instantiation. The central component combines a base datatype with a collection of these constraints, automatically sorting them to maintain a canonical order and enforcing that at least one restriction is present. By implementing comparison and hashing methods based on string representations, the software ensures that these constraints can be reliably used within sets and sorted collections, facilitating the construction of complex data ranges.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.data_range.datatype_restriction.OWLDatatypeRestriction
   pyowl2.data_range.datatype_restriction.OWLFacet
   pyowl2.data_range.datatype_restriction.OWLFacetTypes


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_data_range_datatype_restriction_OWLDatatypeRestriction.png
       :alt: UML Class Diagram for OWLDatatypeRestriction
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDatatypeRestriction**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_data_range_datatype_restriction_OWLDatatypeRestriction.pdf
       :alt: UML Class Diagram for OWLDatatypeRestriction
       :align: center
       :width: 11.7cm
       :class: uml-diagram

       UML Class Diagram for **OWLDatatypeRestriction**

.. py:class:: OWLDatatypeRestriction(datatype: pyowl2.base.datatype.OWLDatatype, restrictions: list[OWLFacet])

   Bases: :py:obj:`pyowl2.abstracts.data_range.OWLDataRange`

   .. autoapi-inheritance-diagram:: pyowl2.data_range.datatype_restriction.OWLDatatypeRestriction
      :parts: 1
      :private-bases:


   Represents a constrained data range within an ontology that narrows the value space of a base datatype through the application of specific facet restrictions. This class is utilized to define precise data characteristics, such as limiting integers to a specific interval or strings to a maximum length, by associating a parent `OWLDatatype` with a collection of `OWLFacet` constraints. Upon instantiation, the provided list of restrictions must contain at least one facet, and the class automatically sorts these facets to maintain a canonical internal order. It serves as a specialized `OWLDataRange` that allows for the granular definition of data property domains in semantic web applications.

   :param datatype: The base datatype that serves as the foundation for the restriction, to which the specific facet constraints are applied.
   :type datatype: OWLDatatype
   :param restrictions: A sorted list of facets defining the constraints applied to the base datatype.
   :type restrictions: list[OWLFacet]


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the OWL datatype restriction, encapsulating the specific datatype and the set of facet restrictions applied to it. The output format places the datatype identifier followed by a space-separated list of the restriction conditions within parentheses, prefixed by 'DatatypeRestriction'. This method is side-effect free and serves primarily to facilitate debugging and logging by providing a concise textual summary of the object's internal state.

      :return: A string representation of the restriction, displaying the datatype and the list of applied restrictions.

      :rtype: str



   .. py:attribute:: _datatype
      :type:  pyowl2.base.datatype.OWLDatatype


   .. py:attribute:: _restrictions
      :type:  list[OWLFacet]


   .. py:property:: datatype
      :type: pyowl2.base.datatype.OWLDatatype


      Updates the OWL datatype associated with this restriction by assigning a new value to the internal state. This setter accepts an instance of `OWLDatatype` and replaces the existing datatype reference, effectively changing the base type upon which the restriction's facets are applied. The operation modifies the object in place and does not return a value.

      :param value: The OWL datatype to assign to the object.
      :type value: OWLDatatype


   .. py:property:: restrictions
      :type: list[OWLFacet]


      Updates the collection of facet constraints applied to the datatype restriction by assigning the provided list of OWLFacet objects. The input list is sorted before being stored in the internal state, ensuring a canonical order for the restrictions. This operation overwrites any previously defined facets.

      :param value: The list of OWL facets to assign as restrictions. The list will be sorted before storage.
      :type value: list[OWLFacet]


.. only:: html

    .. figure:: /_uml/class_pyowl2_data_range_datatype_restriction_OWLFacet.png
       :alt: UML Class Diagram for OWLFacet
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLFacet**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_data_range_datatype_restriction_OWLFacet.pdf
       :alt: UML Class Diagram for OWLFacet
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLFacet**

.. py:class:: OWLFacet(constraint: Union[rdflib.URIRef, pyowl2.base.iri.IRI], value: pyowl2.literal.literal.OWLLiteral)

   Represents a specific constraint applied to a datatype within an OWL ontology, serving to define precise data ranges by pairing a restriction type with a literal value. To use this entity, instantiate it with a constraint type—referenced by a URIRef or IRI—and an OWLLiteral representing the specific bound, such as a minimum or maximum value. The constructor validates that the provided constraint corresponds to a recognized OWL facet type, raising an error if the restriction is invalid. Furthermore, the implementation supports standard comparison and hashing operations based on the string representation of the facet, allowing for easy integration into sets and sorted collections.

   :param valid_restrictions: A whitelist of URI references defining the supported facet types (e.g., minInclusive, maxExclusive) used to validate constraints during instance initialization.
   :type valid_restrictions: list[URIRef]
   :param MIN_INCLUSIVE: URI reference representing the "minInclusive" facet, which restricts a datatype to values greater than or equal to a specified lower bound.
   :type MIN_INCLUSIVE: URIRef
   :param MIN_EXCLUSIVE: Represents the "minExclusive" facet type, indicating that values must be strictly greater than a specified lower bound.
   :type MIN_EXCLUSIVE: URIRef
   :param MAX_INCLUSIVE: URI reference for the "maxInclusive" facet, indicating that values for the associated datatype must be less than or equal to a specified upper bound.
   :type MAX_INCLUSIVE: URIRef
   :param MAX_EXCLUSIVE: A URI reference representing the "maxExclusive" facet, which restricts datatype values to be strictly less than a specified upper bound.
   :type MAX_EXCLUSIVE: URIRef
   :param constraint: The specific type of restriction applied to the datatype, identified by a URI reference or IRI. It defines the nature of the constraint (e.g., minimum or maximum value) and is restricted to valid OWL facet types.
   :type constraint: typing.Union[URIRef, IRI]
   :param value: The specific literal value defining the boundary or limit for the datatype restriction.
   :type value: OWLLiteral


   .. py:method:: __eq__(value: object) -> bool

      Checks if the current instance is equal to the provided object by comparing their string representations. The method converts both the `OWLFacet` instance and the input value to strings and returns `True` if these strings are identical. This implementation allows for equality checks against objects of varying types, provided their string outputs match exactly.

      :param value: The object to compare against. Equality is determined by comparing the string representations of the two objects.
      :type value: object

      :return: True if the string representation of the current instance is equal to the string representation of the specified value, otherwise False.

      :rtype: bool



   .. py:method:: __ge__(value: object) -> bool

      Determines whether the current instance is greater than or equal to the specified value by comparing their string representations. This method converts both the object and the provided argument to strings and performs a standard lexicographical comparison, returning True if the string representation of the current instance is greater than or equal to that of the value.

      :param value: The object to compare against.
      :type value: object

      :return: True if the string representation of the current object is greater than or equal to the string representation of the provided value, otherwise False.

      :rtype: bool



   .. py:method:: __gt__(value: object) -> bool

      Determines whether the current instance is considered greater than the provided value by comparing their string representations. The comparison is performed lexicographically after converting both the instance and the argument to strings. This method enables sorting and ordering operations, relying on the string output rather than the internal structure of the objects.

      :param value: The object to compare against the current instance.
      :type value: object

      :return: True if the string representation of the object is greater than the string representation of the provided value, otherwise False.

      :rtype: bool



   .. py:method:: __hash__() -> int

      Computes the hash value for the OWL facet instance by hashing its string representation. This allows the object to be used as a key in dictionaries or as a member of sets, assuming that the string representation remains stable for the lifetime of the instance. The method delegates the calculation to the built-in hash function applied to the result of `str(self)`.

      :return: An integer representing the hash value of the object, derived from its string representation.

      :rtype: int



   .. py:method:: __le__(value: object) -> bool

      Determines if the current instance is less than or equal to a specified value by comparing their string representations. The method converts both the instance and the provided value to strings and performs a standard lexicographical comparison, returning the result. This allows `OWLFacet` objects to be sorted or compared using the `<=` operator, even against objects of different types, provided they can be converted to strings, without modifying the state of either object.

      :param value: The object to compare against. The comparison is performed using the string representation of the provided object.
      :type value: object

      :return: True if the string representation of the current object is less than or equal to the string representation of the provided value, otherwise False.

      :rtype: bool



   .. py:method:: __lt__(value: object) -> bool

      Determines if the current instance is considered less than the provided value based on their string representations. This method enables the use of the less-than operator (`<`) for `OWLFacet` objects, allowing them to be sorted or compared within sequences. The comparison is performed by converting both the instance and the argument to strings using the built-in `str()` function and evaluating the resulting strings lexicographically. It returns `True` if the string representation of the current instance precedes that of the value, and `False` otherwise.

      :param value: The object to compare against, which is converted to a string for the comparison.
      :type value: object

      :return: True if the string representation of the instance is lexicographically less than the string representation of the provided value.

      :rtype: bool



   .. py:method:: __ne__(value: object) -> bool

      Determines whether the current instance is not equal to the specified object by comparing their string representations. The method converts both the `OWLFacet` instance and the provided value to strings using the built-in `str()` function and returns `True` if the resulting strings differ. This implementation implies that inequality is based solely on the textual output of the objects, meaning that two distinct objects with identical string representations will be considered equal.

      :param value: The object to compare against the current instance.
      :type value: object

      :return: True if the string representation of the instance is not equal to the string representation of the provided value, False otherwise.

      :rtype: bool



   .. py:method:: __repr__() -> str

      Returns the official string representation of the OWLFacet instance. This method delegates directly to the __str__ method, ensuring that the representation used for debugging and logging is identical to the informal string representation. The resulting string provides a human-readable description of the facet.

      :return: Returns the string representation of the object.

      :rtype: str



   .. py:method:: __str__() -> str

      Provides a human-readable string representation of the OWL facet, primarily intended for display or debugging purposes. The returned string follows the format "Facet(constraint value)", incorporating the specific constraint type and the value associated with the facet. This method has no side effects on the object's state.

      :return: A string representation of the object in the format 'Facet(constraint value)'.

      :rtype: str



   .. py:method:: constraint_to_uriref() -> rdflib.URIRef

      Returns the constraint associated with the OWL facet as a URIRef object. If the constraint is currently represented as an IRI instance, the method converts it by calling its `to_uriref` method. Otherwise, the constraint is returned directly, assuming it is already a URIRef or compatible type. This method does not modify the state of the object.

      :return: The constraint represented as a URIRef, converting it from an IRI if necessary.

      :rtype: URIRef



   .. py:attribute:: MAX_EXCLUSIVE
      :type:  rdflib.URIRef


   .. py:attribute:: MAX_INCLUSIVE
      :type:  rdflib.URIRef


   .. py:attribute:: MIN_EXCLUSIVE
      :type:  rdflib.URIRef


   .. py:attribute:: MIN_INCLUSIVE
      :type:  rdflib.URIRef


   .. py:attribute:: _constraint
      :type:  Union[rdflib.URIRef, pyowl2.base.iri.IRI]


   .. py:attribute:: _value
      :type:  pyowl2.literal.literal.OWLLiteral


   .. py:property:: constraint
      :type: Union[rdflib.URIRef, pyowl2.base.iri.IRI]


      Sets the constraint property of the OWL facet to the specified value. The value must be a URI reference or IRI that identifies the specific facet constraint. This method updates the internal state of the instance by assigning the provided value to the underlying `_constraint` attribute.

      :param value: The URI or IRI representing the constraint to be set.
      :type value: typing.Union[URIRef, IRI]


   .. py:attribute:: valid_restrictions
      :type:  list[rdflib.URIRef]


   .. py:property:: value
      :type: pyowl2.literal.literal.OWLLiteral


      Sets the literal constraint value associated with this OWL facet. It accepts an OWLLiteral object and updates the internal state of the facet to reflect the new restriction. This operation mutates the current instance, overwriting any previously defined value for this facet.

      :param value: The OWL literal value to assign.
      :type value: OWLLiteral


.. only:: html

    .. figure:: /_uml/class_pyowl2_data_range_datatype_restriction_OWLFacetTypes.png
       :alt: UML Class Diagram for OWLFacetTypes
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLFacetTypes**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_data_range_datatype_restriction_OWLFacetTypes.pdf
       :alt: UML Class Diagram for OWLFacetTypes
       :align: center
       :width: 4.2cm
       :class: uml-diagram

       UML Class Diagram for **OWLFacetTypes**

.. py:class:: OWLFacetTypes

   Bases: :py:obj:`enum.StrEnum`

   .. autoapi-inheritance-diagram:: pyowl2.data_range.datatype_restriction.OWLFacetTypes
      :parts: 1
      :private-bases:


   This enumeration defines the standard set of constraints, known as facets, used to restrict datatypes in OWL ontologies. It provides specific constants for defining value boundaries, distinguishing between minimum and maximum limits that are either inclusive or exclusive. These types are utilized when constructing data ranges to enforce precise logical constraints on literal values, such as ensuring a number falls within a specific interval. By using this enumeration, developers can reliably specify the exact nature of a datatype restriction within the ontology model.

   :param MIN_INCLUSIVE: Represents the constraint that a data value must be greater than or equal to a specified lower bound.
   :type MIN_INCLUSIVE: typing.Any
   :param MIN_EXCLUSIVE: Restricts the data range to values strictly greater than a specified lower bound.
   :type MIN_EXCLUSIVE: typing.Any
   :param MAX_INCLUSIVE: Represents a constraint that restricts values to be less than or equal to a specified upper bound.
   :type MAX_INCLUSIVE: typing.Any
   :param MAX_EXCLUSIVE: Represents a restriction requiring the value to be strictly less than a specified upper bound.
   :type MAX_EXCLUSIVE: typing.Any


   .. py:attribute:: MAX_EXCLUSIVE


   .. py:attribute:: MAX_INCLUSIVE


   .. py:attribute:: MIN_EXCLUSIVE


   .. py:attribute:: MIN_INCLUSIVE

