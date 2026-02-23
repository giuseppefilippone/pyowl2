pyowl2.individual.named_individual
==================================

.. py:module:: pyowl2.individual.named_individual



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a concrete implementation of an OWL entity that is uniquely identified by an Internationalized Resource Identifier (IRI).


Description
-----------


Extending the abstract concept of an individual within the Web Ontology Language, the implementation provides a mechanism to model concrete instances that possess a persistent, globally resolvable identity. Unlike anonymous nodes, this entity relies on an Internationalized Resource Identifier (IRI) to serve as a unique key, enabling unambiguous reference in axioms and assertions across the ontology. The design encapsulates this identifier within a property interface, allowing for both retrieval and mutation of the identity after instantiation. Furthermore, a string representation is included to facilitate debugging and logging by clearly displaying the associated IRI.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.individual.named_individual.OWLNamedIndividual


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/pyowl2_individual_named_individual_OWLNamedIndividual.png
       :alt: UML Class Diagram for OWLNamedIndividual
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLNamedIndividual**

.. only:: latex

    .. figure:: /_uml/pyowl2_individual_named_individual_OWLNamedIndividual.pdf
       :alt: UML Class Diagram for OWLNamedIndividual
       :align: center
       :width: 10.9cm
       :class: uml-diagram

       UML Class Diagram for **OWLNamedIndividual**

.. py:class:: OWLNamedIndividual(iri: Union[rdflib.URIRef, pyowl2.base.iri.IRI])

   Bases: :py:obj:`pyowl2.abstracts.individual.OWLIndividual`

   .. autoapi-inheritance-diagram:: pyowl2.individual.named_individual.OWLNamedIndividual
      :parts: 1
      :private-bases:


   This class represents a specific entity within an OWL ontology that is distinguished by a unique Internationalized Resource Identifier (IRI). Unlike anonymous individuals, this entity possesses a persistent, globally resolvable identifier that allows it to be unambiguously referenced in axioms and assertions. It is typically used to model concrete instances of classes, such as specific people, objects, or data points, and provides mechanisms to initialize, access, and modify its associated IRI.

   :parm iri: The unique Internationalized Resource Identifier (IRI) that identifies the named individual within the ontology, allowing for unambiguous reference in axioms and assertions.
   :type iri: typing.Union[URIRef, IRI]


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the current instance, formatted as "NamedIndividual({iri})" where {iri} is the value of the object's IRI attribute. This method is invoked implicitly by the `str()` built-in function and print statements, providing a concise summary useful for debugging and logging. The operation has no side effects and relies solely on the current state of the `iri` attribute; if the IRI is not set or is None, the string will reflect that state accordingly.

      :return: A string representation of the instance, formatted as 'NamedIndividual(<iri>)'.

      :rtype: str



   .. py:attribute:: _iri
      :type:  Union[rdflib.URIRef, pyowl2.base.iri.IRI]


   .. py:property:: iri
      :type: Union[rdflib.URIRef, pyowl2.base.iri.IRI]


      Assigns a new Internationalized Resource Identifier (IRI) to the named individual, effectively changing its identity within the ontology. The method accepts a value that is either a URIRef or an IRI object and updates the internal state accordingly. This operation directly mutates the instance, replacing any previously stored IRI.

      :param value: The IRI or URI reference to assign to the object.
      :type value: typing.Union[URIRef, IRI]

