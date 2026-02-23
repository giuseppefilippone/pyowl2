pyowl2.individual
=================

.. only:: html

    .. figure:: /_uml/module_pyowl2_individual.png
       :alt: UML Class Diagram for pyowl2.individual
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **pyowl2.individual**

.. only:: latex

    .. figure:: /_uml/module_pyowl2_individual.pdf
       :alt: UML Class Diagram for pyowl2.individual
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **pyowl2.individual**

.. py:module:: pyowl2.individual



.. ── LLM-GENERATED DESCRIPTION START ──

Provides concrete representations for both named and anonymous individuals within Web Ontology Language structures.


Description
-----------


Facilitates the modeling of entities in an OWL ontology by offering distinct classes for instances that require either a persistent global identity or a local, temporary reference. The architecture leverages inheritance from abstract individual and annotation value interfaces to ensure that both named and anonymous variants can participate in complex graph structures and restrictions. While one implementation encapsulates an Internationalized Resource Identifier (IRI) to provide a globally resolvable key for unambiguous reference, the other utilizes a blank node identifier to manage entities that must be distinguished locally without a permanent name. Internal state management focuses on the encapsulation and mutation of these identifiers, supplemented by string representation methods to aid in debugging and logging during runtime.


Modules
-------


* [``pyowl2.individual.anonymous_individual``] — Represents an anonymous individual within an OWL ontology by utilizing a blank node identifier instead of a globally unique IRI.
* [``pyowl2.individual.named_individual``] — Defines a concrete implementation of an OWL entity that is uniquely identified by an Internationalized Resource Identifier (IRI).

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/pyowl2/individual/anonymous_individual/index
   /api/pyowl2/individual/named_individual/index

