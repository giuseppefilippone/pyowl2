pyowl2.ontology
===============

.. py:module:: pyowl2.ontology


Classes
-------

.. autoapisummary::

   pyowl2.ontology.OWLOntology


Module Contents
---------------

.. py:class:: OWLOntology(base_iri: Union[pyowl2.base.iri.IRI, rdflib.URIRef], ontology_path: Optional[str] = None, OWL1_annotations: bool = False)

   A formal representation of knowledge that includes classes, properties, individuals, and axioms.


   .. py:method:: add_annotation(annotation: pyowl2.base.annotation.OWLAnnotation) -> bool

      Adds an annotation to the ontology.



   .. py:method:: add_annotation_to_element(element: pyowl2.abstracts.object.OWLObject, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]])

      Adds annotations to an element in the ontology.



   .. py:method:: add_annotations(annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]]) -> bool

      Adds annotations to the ontology.



   .. py:method:: add_annotations_to_relation(a: Any, property: Any, b: Any, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]]) -> bool

      Adds annotations to a relation in the ontology.



   .. py:method:: add_axiom(axiom: Any) -> bool

      Adds an axiom to the ontology.



   .. py:method:: add_axioms(axioms: list[pyowl2.abstracts.object.OWLObject]) -> bool

      Adds a list of axioms to the ontology.



   .. py:method:: get_axioms(axiom: pyowl2.getter.rdf_xml_getter.AxiomsType) -> list[pyowl2.abstracts.object.OWLObject]

      Retrieves an axiom from the ontology.



   .. py:method:: print_all() -> None

      Retrieves all axioms from the ontology.



   .. py:method:: save(filepath: str, format: str = 'rdfxml') -> bool

      Saves the ontology to a file.



   .. py:property:: axioms
      :type: list[pyowl2.abstracts.axiom.OWLAxiom]


      Getter for axioms.


   .. py:property:: getter
      :type: pyowl2.getter.rdf_xml_getter.RDFXMLGetter



   .. py:property:: mapper
      :type: pyowl2.mapper.rdf_xml_mapper.RDFXMLMapper



   .. py:property:: namespace
      :type: rdflib.Namespace


      Getter for namespace.


   .. py:property:: ontology_annotations
      :type: Optional[list[pyowl2.base.annotation.OWLAnnotation]]


      Getter for ontology_annotations.


   .. py:property:: ontology_iri
      :type: Optional[rdflib.URIRef]


      Getter for ontology_iri.


