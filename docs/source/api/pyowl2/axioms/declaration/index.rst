pyowl2.axioms.declaration
=========================

.. py:module:: pyowl2.axioms.declaration



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a class representing an OWL declaration axiom that formally introduces named entities into an ontology.


Description
-----------


The implementation centers on the ``OWLDeclaration`` class, which extends the base ``OWLAxiom`` to provide the structural representation required for asserting the existence of vocabulary terms like classes, properties, or individuals. By storing a reference to a specific ``OWLEntity``, the class ensures that the subject of the declaration is explicitly defined and accessible within the broader ontology structure. The design supports the attachment of optional metadata through a list of ``OWLAnnotation`` objects, which are managed by the parent class to allow for rich contextual information without cluttering the core declaration logic. Furthermore, the logic includes a custom string representation method to facilitate debugging and human-readable output, displaying the associated annotations and the declared entity in a standardized format.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.declaration.OWLDeclaration


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_axioms_declaration_OWLDeclaration.png
       :alt: UML Class Diagram for OWLDeclaration
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDeclaration**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_axioms_declaration_OWLDeclaration.pdf
       :alt: UML Class Diagram for OWLDeclaration
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDeclaration**

.. py:class:: OWLDeclaration(entity: pyowl2.abstracts.entity.OWLEntity, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.axiom.OWLAxiom`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.declaration.OWLDeclaration
      :parts: 1
      :private-bases:


   This axiom serves as the formal mechanism for introducing a named entity—such as a class, property, or individual—into the ontology's vocabulary. By asserting the existence of an entity, this declaration enables it to be referenced and utilized within other axioms and logical expressions throughout the ontology. To use this class, instantiate it with the specific `OWLEntity` to be declared, optionally providing a list of annotations to attach metadata or contextual information to the declaration itself.

   :parm entity: The OWL entity (class, property, or individual) that is being declared and introduced into the ontology.
   :type entity: OWLEntity


   .. py:method:: __str__() -> str

      Returns a string representation of the OWL declaration axiom, formatted to display the annotations and the declared entity. If the axiom contains annotations, they are included within the parentheses; otherwise, an empty list representation is used. This method does not modify the object's state and is intended for generating human-readable output or debugging information.

      :return: Returns a string representation of the declaration, including the axiom annotations and the entity.

      :rtype: str



   .. py:attribute:: _entity
      :type:  pyowl2.abstracts.entity.OWLEntity


   .. py:property:: entity
      :type: pyowl2.abstracts.entity.OWLEntity


      Assigns the specified OWL entity to this declaration, replacing the existing entity reference. This method updates the internal state of the declaration to point to the provided entity object, effectively changing the subject of the axiom.

      :param value: The ontology object to assign.
      :type value: OWLEntity

