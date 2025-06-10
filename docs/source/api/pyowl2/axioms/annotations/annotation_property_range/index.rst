pyowl2.axioms.annotations.annotation_property_range
===================================================

.. py:module:: pyowl2.axioms.annotations.annotation_property_range


Classes
-------

.. autoapisummary::

   pyowl2.axioms.annotations.annotation_property_range.OWLAnnotationPropertyRange


Module Contents
---------------

.. py:class:: OWLAnnotationPropertyRange(property: pyowl2.base.annotation_property.OWLAnnotationProperty, iri: Union[rdflib.URIRef, pyowl2.base.iri.IRI], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.annotation_axiom.OWLAnnotationAxiom`


   An axiom specifying that the values of a given annotation property belong to a certain class.


   .. py:method:: __str__() -> str


   .. py:property:: annotation_property
      :type: pyowl2.base.annotation_property.OWLAnnotationProperty


      Getter for annotation_property.


   .. py:property:: range
      :type: Union[rdflib.URIRef, pyowl2.base.iri.IRI]


      Getter for iri.


