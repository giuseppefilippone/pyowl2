pyowl2.literal.literal
======================

.. py:module:: pyowl2.literal.literal


Classes
-------

.. autoapisummary::

   pyowl2.literal.literal.OWLLiteral
   pyowl2.literal.literal.OWLLiteral
   pyowl2.literal.literal.OWLStringLiteralNoLanguage
   pyowl2.literal.literal.OWLStringLiteralWithLanguage
   pyowl2.literal.literal.OWLTypedLiteral


Module Contents
---------------

.. py:class:: OWLLiteral

   Bases: :py:obj:`pyowl2.abstracts.annotation_value.OWLAnnotationValue`


   The value associated with an annotation property for a given subject. It can be an anonymous individual, an IRI or a Literal.


.. py:class:: OWLLiteral(value: Union[rdflib.Literal, OWLTypedLiteral, OWLStringLiteralNoLanguage, OWLStringLiteralWithLanguage])

   Bases: :py:obj:`pyowl2.abstracts.annotation_value.OWLAnnotationValue`


   A data value, such as a string or number, used in an ontology.


   .. py:method:: __str__() -> str


   .. py:method:: is_anyuri() -> bool


   .. py:method:: is_boolean() -> bool


   .. py:method:: is_date() -> bool


   .. py:method:: is_decimal() -> bool


   .. py:method:: is_double() -> bool


   .. py:method:: is_float() -> bool


   .. py:method:: is_integer() -> bool


   .. py:method:: is_rational() -> bool


   .. py:method:: is_real() -> bool


   .. py:method:: is_string() -> bool


   .. py:method:: to_uriref() -> rdflib.URIRef


   .. py:property:: datatype
      :type: Optional[pyowl2.base.datatype.OWLDatatype]



   .. py:property:: value
      :type: Union[rdflib.Literal, OWLTypedLiteral, OWLStringLiteralNoLanguage, OWLStringLiteralWithLanguage]


      Getter for value.


.. py:class:: OWLStringLiteralNoLanguage(value: str)

   Bases: :py:obj:`OWLLiteral`


   The value associated with an annotation property for a given subject. It can be an anonymous individual, an IRI or a Literal.


   .. py:method:: __str__() -> str


   .. py:method:: to_uriref() -> rdflib.URIRef


   .. py:property:: value
      :type: str



.. py:class:: OWLStringLiteralWithLanguage(value: str, language: str)

   Bases: :py:obj:`OWLLiteral`


   The value associated with an annotation property for a given subject. It can be an anonymous individual, an IRI or a Literal.


   .. py:method:: __str__() -> str


   .. py:method:: to_uriref() -> rdflib.URIRef


   .. py:property:: language
      :type: str



   .. py:property:: value
      :type: str



.. py:class:: OWLTypedLiteral(lexical_form: Any, datatype: pyowl2.base.datatype.OWLDatatype)

   Bases: :py:obj:`OWLLiteral`


   A literal that includes an explicit datatype.


   .. py:method:: __str__() -> str


   .. py:method:: to_uriref() -> rdflib.URIRef


   .. py:property:: datatype
      :type: pyowl2.base.datatype.OWLDatatype



   .. py:property:: lexical_form
      :type: Any



