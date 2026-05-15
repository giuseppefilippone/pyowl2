pyowl2.abstracts.entity
=======================

.. py:module:: pyowl2.abstracts.entity



.. ── LLM-GENERATED DESCRIPTION START ──

Defines an abstract base class for named OWL ontology elements where identity, ordering, and hashing are derived strictly from string representations.


Description
-----------


The class serves as a structural ancestor for various components within an OWL ontology, such as classes, object properties, and individuals, ensuring they share a common interface and cannot be instantiated directly. A central design choice dictates that the identity and ordering of these components are determined exclusively by their string representations rather than internal object references or semantic properties. By implementing comparison and hashing operations that delegate to the string form of the object, the implementation ensures that entities with identical textual identifiers are treated as indistinguishable for storage in collections like sets and dictionaries. This approach simplifies the handling of ontology elements by standardizing how they are compared and sorted, relying on lexicographical ordering of their string outputs to drive all relational logic.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.abstracts.entity.OWLEntity


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_abstracts_entity_OWLEntity.png
       :alt: UML Class Diagram for OWLEntity
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLEntity**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_abstracts_entity_OWLEntity.pdf
       :alt: UML Class Diagram for OWLEntity
       :align: center
       :width: 6.2cm
       :class: uml-diagram

       UML Class Diagram for **OWLEntity**

.. py:class:: OWLEntity

   Bases: :py:obj:`pyowl2.abstracts.object.OWLObject`, :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: pyowl2.abstracts.entity.OWLEntity
      :parts: 1
      :private-bases:


   This abstract base class serves as the foundational representation for named elements within an OWL ontology, such as classes, object properties, and individuals. It is designed to be subclassed rather than instantiated directly, providing a common structural ancestor for all distinct ontology components. The class implements comparison and hashing logic that relies entirely on the string representation of the entity; therefore, equality, ordering, and hash values are determined by comparing the string forms of the objects. This behavior ensures that entities with identical string identifiers are treated as indistinguishable for the purposes of sorting and storage in collections like sets and dictionaries.


   .. py:attribute:: __slots__
      :value: ()


