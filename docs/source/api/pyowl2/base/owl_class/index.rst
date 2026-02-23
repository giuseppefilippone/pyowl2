pyowl2.base.owl_class
=====================

.. py:module:: pyowl2.base.owl_class



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a representation of named OWL ontology classes identified by an Internationalized Resource Identifier (IRI).


Description
-----------


The core component serves as a concrete implementation for named classes within the Web Ontology Language, bridging abstract entity definitions with specific resource identifiers. By inheriting from both ``OWLClassExpression`` and ``OWLEntity``, it functions as a fundamental building block for constructing complex logical descriptions and defining relationships. Instances are uniquely identified by an Internationalized Resource Identifier (IRI), which acts as the definitive reference for the class in axioms and assertions, ensuring that concepts like "Person" or "Vehicle" are distinct and addressable. The design includes static accessors for the universal class and the empty class, representing the top and bottom elements of the class hierarchy respectively, while instance methods allow for easy verification of these special states. Additionally, the internal IRI is managed through properties to maintain encapsulation while allowing for updates to the unique identifier.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.base.owl_class.OWLClass


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_base_owl_class_OWLClass.png
       :alt: UML Class Diagram for OWLClass
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLClass**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_base_owl_class_OWLClass.pdf
       :alt: UML Class Diagram for OWLClass
       :align: center
       :width: 10.2cm
       :class: uml-diagram

       UML Class Diagram for **OWLClass**

.. py:class:: OWLClass(iri: Union[rdflib.URIRef, pyowl2.base.iri.IRI])

   Bases: :py:obj:`pyowl2.abstracts.class_expression.OWLClassExpression`, :py:obj:`pyowl2.abstracts.entity.OWLEntity`

   .. autoapi-inheritance-diagram:: pyowl2.base.owl_class.OWLClass
      :parts: 1
      :private-bases:


   Represents a named class within an OWL ontology, functioning as a conceptual grouping for individuals that share specific characteristics or properties. It is uniquely identified by an Internationalized Resource Identifier (IRI), which serves as the definitive reference for the class in axioms and assertions. To define a specific concept, instances are created by providing an IRI, such as a URI representing "Person" or "Vehicle." The class also provides static methods to access the universal class (`owl:Thing`) and the empty class (`owl:Nothing`), enabling the representation of the top and bottom elements of the class hierarchy. As a subclass of both `OWLClassExpression` and `OWLEntity`, it serves as a fundamental building block for constructing complex logical descriptions and defining relationships within the ontology.

   :parm iri: Stores the Internationalized Resource Identifier (IRI) that uniquely identifies the class within the ontology, used for referencing the class in axioms and assertions.
   :type iri: typing.Union[URIRef, IRI]


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the OWL class, formatted as "Class({iri})" where {iri} corresponds to the class's Internationalized Resource Identifier. This method is primarily intended for debugging and logging purposes and is automatically invoked by the built-in `str()` function and print statements. It does not modify the object's state and relies on the current value of the `iri` attribute for the output content.

      :return: Returns a string representation of the object, formatted as 'Class({iri})'.

      :rtype: str



   .. py:method:: is_nothing() -> bool

      Checks if the current instance represents the empty class, often denoted as 'owl:Nothing' in the Web Ontology Language. This method returns True if the object is equivalent to the canonical bottom class, which signifies a class with no instances. It performs a direct equality comparison against the static nothing() instance to determine this status.

      :return: True if the object represents the OWL Nothing class, otherwise False.

      :rtype: bool



   .. py:method:: is_thing() -> bool

      Checks if the current instance represents the universal class 'owl:Thing', which serves as the root of the class hierarchy in OWL ontologies. This method compares the instance against the canonical 'Thing' class to determine equivalence. It returns True if the instance is the top-level class, and False otherwise.

      :return: True if this object is the OWL Thing class, otherwise False.

      :rtype: bool



   .. py:method:: nothing() -> Self
      :staticmethod:


      Returns the OWL class representing the empty set, formally known as `owl:Nothing`. This static method constructs an instance of `OWLClass` initialized with the specific IRI corresponding to the bottom element of the OWL class hierarchy. It is used to denote a contradiction or a class that cannot have any instances. The function has no side effects and does not accept any arguments.

      :return: Returns the OWL class representing the empty set (owl:Nothing).

      :rtype: typing.Self



   .. py:method:: thing() -> Self
      :staticmethod:


      Retrieves the `OWLClass` instance representing `owl:Thing`, which is the universal class in the OWL ontology and the root of the class hierarchy. This static method constructs the class using the standard OWL namespace IRI, ensuring the returned object corresponds to the official top-level concept defined by the specification. It does not depend on instance state and returns a new representation of the class each time it is called.

      :return: Returns the OWL class representing the universal class (owl:Thing).

      :rtype: typing.Self



   .. py:attribute:: _iri
      :type:  Union[rdflib.URIRef, pyowl2.base.iri.IRI]


   .. py:property:: iri
      :type: Union[rdflib.URIRef, pyowl2.base.iri.IRI]


      Sets the Internationalized Resource Identifier (IRI) for the OWL class instance. This method accepts a value that is either a URIRef or an IRI object and assigns it to the internal `_iri` attribute, thereby updating the unique identifier of the class. This operation modifies the state of the object in place.

      :param value: The IRI or URI reference to assign to the object.
      :type value: typing.Union[URIRef, IRI]

