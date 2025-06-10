pyowl2.axioms.declaration
=========================

.. py:module:: pyowl2.axioms.declaration


Classes
-------

.. autoapisummary::

   pyowl2.axioms.declaration.OWLDeclaration


Module Contents
---------------

.. py:class:: OWLDeclaration(entity: pyowl2.abstracts.entity.OWLEntity, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.axiom.OWLAxiom`


   An axiom that introduces a named entity (class, property, individual) into the ontology.


   .. py:method:: __str__() -> str


   .. py:property:: entity
      :type: pyowl2.abstracts.entity.OWLEntity


      Getter for entity.


