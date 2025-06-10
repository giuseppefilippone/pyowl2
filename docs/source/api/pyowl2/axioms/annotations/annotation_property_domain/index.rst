pyowl2.axioms.annotations.annotation_property_domain
====================================================

.. py:module:: pyowl2.axioms.annotations.annotation_property_domain


Classes
-------

.. autoapisummary::

   pyowl2.axioms.annotations.annotation_property_domain.OWLAnnotationPropertyDomain


Module Contents
---------------

.. py:class:: OWLAnnotationPropertyDomain(property: pyowl2.base.annotation_property.OWLAnnotationProperty, iri: Union[rdflib.URIRef, pyowl2.base.iri.IRI], annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.annotation_axiom.OWLAnnotationAxiom`


   An axiom specifying that a given annotation property applies to subjects of a certain class.


   .. py:method:: __str__() -> str


   .. py:property:: annotation_property
      :type: pyowl2.base.annotation_property.OWLAnnotationProperty


      Getter for annotation_property.


   .. py:property:: domain
      :type: Union[rdflib.URIRef, pyowl2.base.iri.IRI]


      Getter for iri.


