pyowl2.axioms.data_property_axiom.data_property_domain
======================================================

.. py:module:: pyowl2.axioms.data_property_axiom.data_property_domain



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a Web Ontology Language (OWL) axiom that restricts the domain of a data property by asserting that individuals associated with the property must belong to a specific class.


Description
-----------


The software models a specific type of logical constraint within the Web Ontology Language by linking a data property expression to a class expression that defines its valid subjects. By storing references to both the property and the domain class, the implementation ensures that any individual utilizing the data property logically belongs to the specified class, thereby enforcing consistency within an ontology. Design choices include support for optional annotations, allowing users to attach metadata to the axiom, and the use of property getters and setters to manage the internal state of the property and class expressions. Furthermore, the logic includes a string representation method that outputs the axiom in a functional syntax style, explicitly handling the presence or absence of annotations to maintain a consistent structural format.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.data_property_axiom.data_property_domain.OWLDataPropertyDomain


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_axioms_data_property_axiom_data_property_domain_OWLDataPropertyDomain.png
       :alt: UML Class Diagram for OWLDataPropertyDomain
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDataPropertyDomain**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_axioms_data_property_axiom_data_property_domain_OWLDataPropertyDomain.pdf
       :alt: UML Class Diagram for OWLDataPropertyDomain
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDataPropertyDomain**

.. py:class:: OWLDataPropertyDomain(property: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression, expression: pyowl2.abstracts.class_expression.OWLClassExpression, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.data_property_axiom.OWLDataPropertyAxiom`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.data_property_axiom.data_property_domain.OWLDataPropertyDomain
      :parts: 1
      :private-bases:


   Represents an axiom in the Web Ontology Language (OWL) that defines the domain restriction for a specific data property, asserting that any individual associated with the property must belong to a specified class. It links a data property expression—which connects individuals to literal values—with a class expression that defines the valid types of subjects for that property. Users can utilize this structure to enforce logical consistency within an ontology by specifying the property, its domain class, and optional annotations for metadata. The implementation supports both simple named classes and complex class expressions, allowing for nuanced constraints on the individuals that may participate in data property assertions.

   :param data_property_expression: The data property expression whose domain is defined by this axiom.
   :type data_property_expression: OWLDataPropertyExpression
   :param class_expression: Specifies the domain of the data property, defining the class of individuals that can be associated with it.
   :type class_expression: OWLClassExpression


   .. py:method:: __str__() -> str

      Returns a string representation of the data property domain axiom using a functional syntax style. The formatted string includes the axiom's annotations, the associated data property expression, and the class expression defining the domain. If the axiom does not contain any annotations, the representation explicitly includes an empty list `[]` in the annotations position to maintain structural consistency.

      :return: Returns a string representation of the data property domain axiom, including its annotations, data property expression, and class expression.

      :rtype: str



   .. py:attribute:: _class_expression
      :type:  pyowl2.abstracts.class_expression.OWLClassExpression


   .. py:attribute:: _data_property_expression
      :type:  pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression


   .. py:property:: class_expression
      :type: pyowl2.abstracts.class_expression.OWLClassExpression


      Sets the class expression that defines the domain for this data property axiom. This method assigns the provided `OWLClassExpression` instance to the internal state, effectively replacing any previously associated domain expression. As a setter, it mutates the object in place and does not return a value.

      :param value: The OWL class expression to assign.
      :type value: OWLClassExpression


   .. py:property:: data_property_expression
      :type: pyowl2.abstracts.data_property_expression.OWLDataPropertyExpression


      Sets the data property expression for this OWL data property domain axiom. This method assigns the provided OWLDataPropertyExpression to the internal state, overwriting any previously stored value. It defines the specific data property whose domain is being restricted by this axiom.

      :param value: The OWL data property expression to assign.
      :type value: OWLDataPropertyExpression

