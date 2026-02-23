pyowl2.abstracts.data_property_axiom
====================================

.. py:module:: pyowl2.abstracts.data_property_axiom



.. ── LLM-GENERATED DESCRIPTION START ──

Defines an abstract base class for axioms that govern data properties within the Web Ontology Language (OWL) framework.


Description
-----------


Building upon the general axiom structure, this interface specifically targets properties that associate individuals with literal values like strings or integers, distinguishing them from object properties that link individuals to other individuals. By utilizing the Abstract Base Class metaclass, it ensures that concrete subclasses must implement specific logic to represent semantic rules such as declaring a property functional or defining its domain. The design enforces a strict separation of concerns where the component serves solely as a type definition and contract, preventing direct instantiation and guiding developers toward using specialized implementations for precise ontological modeling. This abstraction facilitates the extension of the ontology system by providing a stable root for all data-related property constraints, ensuring consistency across the library's logical framework.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.abstracts.data_property_axiom.OWLDataPropertyAxiom


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/pyowl2_abstracts_data_property_axiom_OWLDataPropertyAxiom.png
       :alt: UML Class Diagram for OWLDataPropertyAxiom
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDataPropertyAxiom**

.. only:: latex

    .. figure:: /_uml/pyowl2_abstracts_data_property_axiom_OWLDataPropertyAxiom.pdf
       :alt: UML Class Diagram for OWLDataPropertyAxiom
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDataPropertyAxiom**

.. py:class:: OWLDataPropertyAxiom(annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.axiom.OWLAxiom`, :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: pyowl2.abstracts.data_property_axiom.OWLDataPropertyAxiom
      :parts: 1
      :private-bases:


   This abstract base class serves as the foundational interface for axioms that define the characteristics, constraints, and relationships of data properties within an OWL ontology. It distinguishes itself from object property axioms by focusing on properties that link individuals to literal data values, such as strings or integers, rather than to other individuals. As a specialization of the general axiom type, it provides a common contract for concrete implementations that model specific logical statements, such as declaring a property as functional, defining its domain, or establishing a sub-property hierarchy. Users should not instantiate this class directly but should instead utilize its specific subclasses to represent precise semantic rules in their ontological models.


   .. py:attribute:: __slots__
      :value: ()


