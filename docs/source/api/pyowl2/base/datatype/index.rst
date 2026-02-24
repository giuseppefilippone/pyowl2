pyowl2.base.datatype
====================

.. py:module:: pyowl2.base.datatype



.. ── LLM-GENERATED DESCRIPTION START ──

A Python implementation of an OWL datatype that represents data value categories identified by IRIs and includes utilities for checking against standard XML Schema and OWL types.


Description
-----------


The software defines a class that models data types within the Web Ontology Language (OWL), serving as a bridge between abstract ontology concepts and concrete RDF representations. By inheriting from both entity and data range abstractions, the class establishes a dual identity that allows it to function as a named resource and a range of permissible values. The core design relies on an Internationalized Resource Identifier (IRI) to uniquely define the data type, enabling the representation of both standard XML Schema definitions—such as integers, strings, and dates—and custom user-defined types. To facilitate semantic processing, the implementation includes logic to compare the stored IRI against canonical namespaces, allowing applications to easily determine if a specific instance corresponds to common numeric, boolean, or temporal categories without manual string parsing. This abstraction simplifies the manipulation of typed literals in semantic web applications by providing a consistent interface for type identification and conversion to standard RDF URI references.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.base.datatype.OWLDatatype


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_base_datatype_OWLDatatype.png
       :alt: UML Class Diagram for OWLDatatype
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDatatype**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_base_datatype_OWLDatatype.pdf
       :alt: UML Class Diagram for OWLDatatype
       :align: center
       :width: 12.5cm
       :class: uml-diagram

       UML Class Diagram for **OWLDatatype**

.. py:class:: OWLDatatype(iri: Union[pyowl2.base.iri.IRI, rdflib.URIRef])

   Bases: :py:obj:`pyowl2.abstracts.entity.OWLEntity`, :py:obj:`pyowl2.abstracts.data_range.OWLDataRange`

   .. autoapi-inheritance-diagram:: pyowl2.base.datatype.OWLDatatype
      :parts: 1
      :private-bases:


   This entity represents a specific category of data values within an ontology, such as integers, strings, or dates, effectively defining a set of permissible values. It is uniquely identified by an Internationalized Resource Identifier (IRI), which links the datatype to standard definitions like those found in the XML Schema (XSD) or OWL namespaces. Users can instantiate this class with an IRI to define custom or standard datatypes, and utilize the provided helper methods to verify if the instance corresponds to common numeric, boolean, string, or date types. As a subclass of `OWLEntity` and `OWLDataRange`, it serves as a fundamental building block for typing data properties and literals in semantic web applications.

   :param iri: Stores the unique Internationalized Resource Identifier (IRI) that identifies the datatype. This value determines the specific nature of the data range (e.g., integer, string) and is used for unambiguous reference within the ontology.
   :type iri: typing.Union[IRI, URIRef]


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the OWL datatype instance. The output is formatted by wrapping the datatype's internal IRI (Internationalized Resource Identifier) within the text "Datatype(...)". This representation is primarily intended for debugging and logging, providing a concise summary of the datatype's identity.

      :return: A string representation of the datatype, including its IRI.

      :rtype: str



   .. py:method:: is_anyuri() -> bool

      Determines whether this OWL datatype corresponds to the XML Schema Definition (XSD) datatype `anyURI`. The method performs a strict string comparison between the IRI of the current datatype instance and the canonical IRI for `xsd:anyURI`. It returns `True` if the IRIs match, indicating that the datatype represents a URI reference, and `False` otherwise. This operation has no side effects and does not modify the state of the object.

      :return: True if the IRI corresponds to the XSD anyURI datatype, False otherwise.

      :rtype: bool



   .. py:method:: is_boolean() -> bool

      Determines whether the current OWL datatype corresponds to the XML Schema Definition (XSD) boolean datatype. This check is performed by comparing the datatype's Internationalized Resource Identifier (IRI) against the standard IRI for `xsd:boolean`. The method returns `True` if the IRIs match, indicating the datatype is the built-in boolean type, and `False` otherwise. This operation does not modify the state of the object.

      :return: True if the IRI corresponds to the XSD boolean datatype, otherwise False.

      :rtype: bool



   .. py:method:: is_date() -> bool

      Determines whether the current OWL datatype corresponds to specific XML Schema Definition (XSD) temporal types. This method checks the datatype's Internationalized Resource Identifier (IRI) and returns True if it matches `xsd:date`, `xsd:dateTime`, `xsd:dateTimeStamp`, or `xsd:dayTimeDuration`. It is a read-only check with no side effects, returning False for any other datatype IRI.

      :return: True if the IRI corresponds to an XSD date, dateTime, dateTimeStamp, or dayTimeDuration datatype; otherwise, False.

      :rtype: bool



   .. py:method:: is_decimal() -> bool

      Checks if the current datatype instance represents the standard XML Schema Definition (XSD) decimal type. This determination is made by comparing the datatype's Internationalized Resource Identifier (IRI) against the canonical IRI for `xsd:decimal`. The method returns `True` if the IRIs match, indicating the datatype is a decimal, and `False` otherwise.

      :return: True if the IRI represents the XML Schema decimal datatype, False otherwise.

      :rtype: bool



   .. py:method:: is_double() -> bool

      Checks if the current datatype represents the XML Schema Definition (XSD) double type. This method performs a strict equality check between the datatype's Internationalized Resource Identifier (IRI) and the standard IRI associated with the `xsd:double` namespace. It returns `True` if the identifiers match, indicating that the datatype is a double, and `False` otherwise.

      :return: True if the IRI corresponds to the XSD double datatype, False otherwise.

      :rtype: bool



   .. py:method:: is_float() -> bool

      Checks if the current datatype corresponds to the XML Schema Definition (XSD) float type by comparing its Internationalized Resource Identifier (IRI) against the standard IRI for `xsd:float`. The method returns `True` only if the IRI matches exactly, indicating a 32-bit floating-point number, and returns `False` for any other datatype, including other numeric types like `xsd:double` or `xsd:decimal`. This operation is a pure comparison and has no side effects.

      :return: True if the IRI corresponds to the XSD float datatype.

      :rtype: bool



   .. py:method:: is_integer() -> bool

      Determines whether the current datatype corresponds to an XML Schema Definition (XSD) integer type. This check is performed by comparing the datatype's IRI against a comprehensive list of numeric IRIs, including `xsd:integer`, `xsd:int`, `xsd:long`, `xsd:short`, `xsd:byte`, and their signed or unsigned variants (such as `xsd:nonNegativeInteger` or `xsd:unsignedLong`). The method returns `True` if a match is found, indicating the datatype is an integer, and `False` otherwise.

      :return: True if the IRI corresponds to an XSD integer datatype, otherwise False.

      :rtype: bool



   .. py:method:: is_rational() -> bool

      Checks if the current datatype instance represents the OWL rational datatype. This is determined by comparing the instance's Internationalized Resource Identifier (IRI) against the canonical IRI for `owl:rational` defined in the OWL namespace. The method returns `True` if the IRIs match, indicating the datatype is specifically a rational number type, and `False` for any other datatype.

      :return: True if the object's IRI matches the OWL rational IRI, False otherwise.

      :rtype: bool



   .. py:method:: is_real() -> bool

      Determines if the current datatype represents the specific OWL datatype for real numbers. This is achieved by comparing the Internationalized Resource Identifier (IRI) of the instance against the canonical IRI for `owl:real` within the OWL namespace. The method returns `True` if the IRIs match, indicating the datatype is a real number, and `False` otherwise.

      :return: True if the object's IRI matches the OWL 'real' IRI, False otherwise.

      :rtype: bool



   .. py:method:: is_string() -> bool

      Checks if the current datatype corresponds to a string-based data type within the RDF and OWL specifications. This determination is made by verifying whether the datatype's IRI matches a specific set of recognized string IRIs, including `xsd:string`, `xsd:normalizedString`, `rdf:langString`, `rdf:PlainLiteral`, and `rdf:CompoundLiteral`. The method returns `True` if the IRI is found within this set, indicating that the datatype is designed to represent textual content, and `False` otherwise. This check relies entirely on the IRI identifier and does not modify the state of the object.

      :return: True if the IRI corresponds to a string datatype (e.g., XSD string, normalizedString, or RDF langString), otherwise False.

      :rtype: bool



   .. py:method:: to_uriref() -> rdflib.URIRef

      Returns the underlying RDF resource identifier as a URIRef object. If the internal identifier is currently stored as an IRI instance, the method delegates to that object's conversion logic; otherwise, it returns the identifier directly. This operation is stateless and does not modify the datatype instance.

      :return: The URIRef representation of the IRI, or the value itself if it is already a URIRef.

      :rtype: URIRef



   .. py:attribute:: _iri
      :type:  Union[pyowl2.base.iri.IRI, rdflib.URIRef]


   .. py:property:: iri
      :type: Union[pyowl2.base.iri.IRI, rdflib.URIRef]


      Sets the Internationalized Resource Identifier (IRI) for this OWL datatype instance. The method accepts either an IRI or a URIRef object as the new identifier value. This operation directly updates the internal state of the object, effectively changing the semantic identity of the datatype to the specified URI.

      :param value: The IRI or URI reference to assign to the object.
      :type value: typing.Union[IRI, URIRef]

