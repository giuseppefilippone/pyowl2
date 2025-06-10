pyowl2.axioms.datatype_definition
=================================

.. py:module:: pyowl2.axioms.datatype_definition


Classes
-------

.. autoapisummary::

   pyowl2.axioms.datatype_definition.OWLDatatypeDefinition


Module Contents
---------------

.. py:class:: OWLDatatypeDefinition(datatype: pyowl2.base.datatype.OWLDatatype, data_range: pyowl2.abstracts.data_range.OWLDataRange, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.axiom.OWLAxiom`


   An axiom that defines a new datatype in terms of existing datatypes.


   .. py:method:: __str__() -> str


   .. py:property:: data_range
      :type: pyowl2.abstracts.data_range.OWLDataRange


      Getter for data_range.


   .. py:property:: datatype
      :type: pyowl2.base.datatype.OWLDatatype


      Getter for datatype.


