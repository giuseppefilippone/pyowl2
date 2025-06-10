pyowl2.abstracts.annotation_value
=================================

.. py:module:: pyowl2.abstracts.annotation_value


Classes
-------

.. autoapisummary::

   pyowl2.abstracts.annotation_value.OWLAnnotationValue


Module Contents
---------------

.. py:class:: OWLAnnotationValue

   Bases: :py:obj:`pyowl2.abstracts.object.OWLObject`, :py:obj:`abc.ABC`


   The value associated with an annotation property for a given subject. It can be an anonymous individual, an IRI or a Literal.


   .. py:method:: __eq__(value: object) -> bool


   .. py:method:: __ge__(value: object) -> bool


   .. py:method:: __gt__(value: object) -> bool


   .. py:method:: __hash__() -> int


   .. py:method:: __le__(value: object) -> bool


   .. py:method:: __lt__(value: object) -> bool


   .. py:method:: __ne__(value: object) -> bool


   .. py:method:: __repr__() -> str


   .. py:attribute:: __slots__
      :value: ()



