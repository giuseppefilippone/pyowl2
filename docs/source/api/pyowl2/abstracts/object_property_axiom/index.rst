pyowl2.abstracts.object_property_axiom
======================================

.. py:module:: pyowl2.abstracts.object_property_axiom



.. ── LLM-GENERATED DESCRIPTION START ──

Defines an abstract base class representing axioms that govern the semantics and characteristics of object properties in OWL ontologies.


Description
-----------


Acting as a specialized extension of the general ``OWLAxiom`` interface, this class establishes a structural foundation for statements that define how object properties behave and relate to one another. It encompasses a wide range of semantic constraints, including sub-property hierarchies, domain and range specifications, and logical characteristics such as transitivity or symmetry. By utilizing the Abstract Base Class module, the design ensures that this component serves solely as a contract, forcing developers to implement concrete subclasses for modeling specific relationships between individuals rather than instantiating this generic definition directly.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.abstracts.object_property_axiom.OWLObjectPropertyAxiom


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_abstracts_object_property_axiom_OWLObjectPropertyAxiom.png
       :alt: UML Class Diagram for OWLObjectPropertyAxiom
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLObjectPropertyAxiom**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_abstracts_object_property_axiom_OWLObjectPropertyAxiom.pdf
       :alt: UML Class Diagram for OWLObjectPropertyAxiom
       :align: center
       :width: 13.8cm
       :class: uml-diagram

       UML Class Diagram for **OWLObjectPropertyAxiom**

.. py:class:: OWLObjectPropertyAxiom(annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.axiom.OWLAxiom`, :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: pyowl2.abstracts.object_property_axiom.OWLObjectPropertyAxiom
      :parts: 1
      :private-bases:


   This class serves as an abstract base class representing axioms that define the semantics, relationships, or characteristics of object properties within an OWL ontology. As a specialization of the general `OWLAxiom` interface, it provides the foundational structure for specific statements that describe how object properties behave, such as declaring sub-property hierarchies, specifying domains and ranges, or defining property characteristics like transitivity or symmetry. Developers should not instantiate this class directly but rather rely on its concrete subclasses to model specific constraints and rules governing the relationships between individuals in an ontology.


   .. py:attribute:: __slots__
      :value: ()


