pyowl2.abstracts.data_property_expression
=========================================

.. py:module:: pyowl2.abstracts.data_property_expression


Classes
-------

.. autoapisummary::

   pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression


Module Contents
---------------

.. py:class:: OWLDataPropertyExpression

   Bases: :py:obj:`pyowl2.abstracts.object.OWLObject`, :py:obj:`abc.ABC`


   An expression involving data properties, which represent relationships between an individual and a literal.


   .. py:method:: is_bottom_data_property() -> bool
      :abstractmethod:



   .. py:method:: is_top_data_property() -> bool
      :abstractmethod:



   .. py:attribute:: __slots__
      :value: ()



