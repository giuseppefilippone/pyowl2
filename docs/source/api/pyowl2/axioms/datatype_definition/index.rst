pyowl2.axioms.datatype_definition
=================================

.. py:module:: pyowl2.axioms.datatype_definition



.. ── LLM-GENERATED DESCRIPTION START ──

Represents an OWL axiom that defines a new datatype by equating it to a specific data range.


Description
-----------


The implementation extends the base *OWLAxiom* class to model the logical construct of defining a custom datatype within an ontology. By associating a specific *OWLDatatype* instance with a defining *OWLDataRange*, the software enables the creation of complex data types that restrict values based on existing ranges or literal constraints. Optional annotations can be attached to the definition to provide metadata, which are handled through inheritance from the parent axiom class. State management is facilitated through properties that allow the retrieval and modification of both the target datatype and the defining data range, while a custom string representation ensures the axiom can be displayed in a human-readable format consistent with OWL syntax.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.datatype_definition.OWLDatatypeDefinition


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/pyowl2_axioms_datatype_definition_OWLDatatypeDefinition.png
       :alt: UML Class Diagram for OWLDatatypeDefinition
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLDatatypeDefinition**

.. only:: latex

    .. figure:: /_uml/pyowl2_axioms_datatype_definition_OWLDatatypeDefinition.pdf
       :alt: UML Class Diagram for OWLDatatypeDefinition
       :align: center
       :width: 13.7cm
       :class: uml-diagram

       UML Class Diagram for **OWLDatatypeDefinition**

.. py:class:: OWLDatatypeDefinition(datatype: pyowl2.base.datatype.OWLDatatype, data_range: pyowl2.abstracts.data_range.OWLDataRange, annotations: Optional[list[pyowl2.base.annotation.OWLAnnotation]] = None)

   Bases: :py:obj:`pyowl2.abstracts.axiom.OWLAxiom`

   .. autoapi-inheritance-diagram:: pyowl2.axioms.datatype_definition.OWLDatatypeDefinition
      :parts: 1
      :private-bases:


   This axiom serves to define a new datatype within an ontology by equating it to a specific data range, which may consist of simple literals or complex restrictions on existing datatypes. It functions as a logical building block, allowing the newly created datatype to be utilized in other parts of the ontology to enforce precise value constraints. The definition is composed of a target datatype and a defining data range, and it can optionally include annotations to provide additional context or metadata about the axiom itself.

   :parm datatype: The new datatype being defined by this axiom, identified by its IRI.
   :type datatype: OWLDatatype
   :parm data_range: Specifies the set of values or constraints that define the new datatype.
   :type data_range: OWLDataRange


   .. py:method:: __str__() -> str

      Returns a formatted string representation of the datatype definition axiom, incorporating the axiom's annotations, the specific datatype being defined, and the data range used for the definition. If the axiom has no associated annotations, the representation explicitly includes an empty list in place of the annotations to maintain a consistent structure.

      :return: A string representation of the datatype definition axiom, formatted as `DatatypeDefinition([annotations] datatype data_range)`.

      :rtype: str



   .. py:attribute:: _data_range
      :type:  pyowl2.abstracts.data_range.OWLDataRange


   .. py:attribute:: _datatype
      :type:  pyowl2.base.datatype.OWLDatatype


   .. py:property:: data_range
      :type: pyowl2.abstracts.data_range.OWLDataRange


      Updates the data range associated with this OWL datatype definition by assigning the provided `OWLDataRange` object to the internal state. This operation overwrites any existing data range, effectively modifying the definition's constraints in place. While the method signature expects an instance of `OWLDataRange`, the implementation does not perform explicit runtime validation of the input type.

      :param value: The OWL data range to assign.
      :type value: OWLDataRange


   .. py:property:: datatype
      :type: pyowl2.base.datatype.OWLDatatype


      Updates the OWL datatype associated with this definition by assigning the provided value to the internal storage. This setter allows the underlying data type reference to be replaced or initialized. The method accepts an instance of OWLDatatype and directly overwrites the existing attribute without performing additional validation.

      :param value: The OWL datatype to assign.
      :type value: OWLDatatype

