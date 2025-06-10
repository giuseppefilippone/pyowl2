pyowl2.abstracts.axiom
======================

.. py:module:: pyowl2.abstracts.axiom


Classes
-------

.. autoapisummary::

   pyowl2.abstracts.axiom.OWLAxiom


Module Contents
---------------

.. py:class:: OWLAxiom(annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.object.OWLObject`, :py:obj:`abc.ABC`


   A fundamental statement or assertion within an ontology that contributes to its logical structure.


   .. py:method:: __eq__(value: object) -> bool


   .. py:method:: __ge__(value: object) -> bool


   .. py:method:: __gt__(value: object) -> bool


   .. py:method:: __hash__() -> int


   .. py:method:: __le__(value: object) -> bool


   .. py:method:: __lt__(value: object) -> bool


   .. py:method:: __ne__(value: object) -> bool


   .. py:method:: __repr__() -> str


   .. py:property:: axiom_annotations
      :type: Optional[list[pyowl2.base.annotation.OWLAnnotation]]


      Getter for axiom_annotations.


