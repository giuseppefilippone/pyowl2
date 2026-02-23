pyowl2.axioms.general
=====================

.. py:module:: pyowl2.axioms.general



.. ── LLM-GENERATED DESCRIPTION START ──

Models a logical assertion within an ontology that links a subject class expression to an object class expression via a specific property.


Description
-----------


The implementation extends the base axiom structure to represent complex constraints by associating a subject class expression with a target class expression through an intermediate property identified by an Internationalized Resource Identifier (IRI). Designed for flexibility, the internal state is fully mutable, allowing the modification of the subject, property, and target components after instantiation to accommodate evolving ontology models. Optional metadata can be attached to the logical assertion through a list of annotations, which are managed by the parent class to support rich semantic descriptions. A string representation is provided to visualize the logical structure, explicitly displaying the components in a readable format that highlights the relationship between the defined entities.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.general.OWLGeneralClassAxiom


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/pyowl2_axioms_general_OWLGeneralClassAxiom.png
       :alt: UML Class Diagram for OWLGeneralClassAxiom
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLGeneralClassAxiom**

.. only:: latex

    .. figure:: /_uml/pyowl2_axioms_general_OWLGeneralClassAxiom.pdf
       :alt: UML Class Diagram for OWLGeneralClassAxiom
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLGeneralClassAxiom**

.. py:class:: OWLGeneralClassAxiom(left_expression: pyowl2.abstracts.class_expression.OWLClassExpression, property: pyowl2.base.iri.IRI, right_expression: pyowl2.abstracts.class_expression.OWLClassExpression, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.axiom.OWLAxiom`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.general.OWLGeneralClassAxiom
      :parts: 1
      :private-bases:


   This class models a logical assertion within an ontology that defines a relationship between two class expressions via a specific property. It enables the representation of complex constraints and associations by linking a subject class expression to an object class expression through an intermediate property identified by an IRI. To use this component, instantiate it with the left and right class expressions along with the property IRI, optionally providing a list of annotations to attach metadata to the axiom. The structure is fully mutable, allowing users to update the class expressions, the property IRI, or the annotations after creation to reflect changes in the underlying ontology model.

   :parm left_expression: The class expression on the left side of the axiom, representing the subject of the relationship asserted by the property.
   :type left_expression: OWLClassExpression
   :parm property_iri: The IRI representing the property that connects the left and right class expressions, defining the specific relationship asserted by the axiom.
   :type property_iri: IRI
   :parm right_expression: The class expression on the right side of the axiom, acting as the target of the relationship asserted by the property IRI.
   :type right_expression: OWLClassExpression


   .. py:method:: __str__() -> str

      Returns a string representation of the axiom, formatted to display the left expression, property IRI, and right expression. The output string begins with 'GeneralClassAxiom' followed by the annotation component and the core components of the axiom. The formatting of the annotation component depends on the truthiness of the `axiom_annotations` attribute: if the attribute is truthy, the string representation uses an empty list `[]`, while if it is falsy, the actual value of the attribute is included in the string.

      :return: A string representation of the axiom, displaying the annotations, left expression, property IRI, and right expression.

      :rtype: str



   .. py:attribute:: _left_expression
      :type:  pyowl2.abstracts.class_expression.OWLClassExpression


   .. py:attribute:: _property_iri
      :type:  pyowl2.base.iri.IRI


   .. py:attribute:: _right_expression
      :type:  pyowl2.abstracts.class_expression.OWLClassExpression


   .. py:property:: left_expression
      :type: pyowl2.abstracts.class_expression.OWLClassExpression


      Sets the left-hand side class expression for the axiom, replacing the current value. This method updates the internal state of the object by assigning the provided OWLClassExpression to the underlying private attribute. It serves as the setter for the left_expression property, enabling modification of the axiom's structure after instantiation.

      :param value: The class expression to assign as the left operand.
      :type value: OWLClassExpression


   .. py:property:: property_iri
      :type: pyowl2.base.iri.IRI


      Sets the Internationalized Resource Identifier (IRI) for the property associated with this OWL general class axiom. This method updates the internal state of the instance by assigning the provided IRI object to the underlying private attribute. It directly replaces the existing property reference without performing additional validation, meaning the caller is responsible for ensuring the input is a valid IRI object.

      :param value: The IRI to assign to the property.
      :type value: IRI


   .. py:property:: right_expression
      :type: pyowl2.abstracts.class_expression.OWLClassExpression


      Sets the right-hand side class expression for the general class axiom. This method updates the internal state of the object by assigning the provided OWLClassExpression to the corresponding private attribute. It is typically used to define or modify the operand on the right side of logical relationships represented by the axiom.

      :param value: The OWL class expression to assign as the right operand.
      :type value: OWLClassExpression

