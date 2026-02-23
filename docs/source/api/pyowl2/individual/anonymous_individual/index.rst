pyowl2.individual.anonymous_individual
======================================

.. py:module:: pyowl2.individual.anonymous_individual



.. ── LLM-GENERATED DESCRIPTION START ──

Represents an anonymous individual within an OWL ontology by utilizing a blank node identifier instead of a globally unique IRI.


Description
-----------


The software implements a specific type of entity that exists within an ontology without possessing a permanent, resolvable name, relying instead on a local blank node identifier to ensure distinction within the graph. By inheriting from both abstract individual and annotation value interfaces, the class enables the construction of complex structures and restrictions where specific instances must be referenced without requiring a globally unique identifier. Internal state management revolves around a node identifier stored as an RDFLib URI reference, which can be accessed or modified to reflect the entity's unique local identity. A string representation method facilitates debugging by displaying the class name alongside the internal identifier, ensuring that developers can easily track specific instances during runtime.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.individual.anonymous_individual.OWLAnonymousIndividual


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_individual_anonymous_individual_OWLAnonymousIndividual.png
       :alt: UML Class Diagram for OWLAnonymousIndividual
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLAnonymousIndividual**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_individual_anonymous_individual_OWLAnonymousIndividual.pdf
       :alt: UML Class Diagram for OWLAnonymousIndividual
       :align: center
       :width: 12.1cm
       :class: uml-diagram

       UML Class Diagram for **OWLAnonymousIndividual**

.. py:class:: OWLAnonymousIndividual(node_id: rdflib.URIRef)

   Bases: :py:obj:`pyowl2.abstracts.annotation_value.OWLAnnotationValue`, :py:obj:`pyowl2.abstracts.individual.OWLIndividual`

   .. autoapi-inheritance-diagram:: pyowl2.individual.anonymous_individual.OWLAnonymousIndividual
      :parts: 1
      :private-bases:


   This class represents an entity within an OWL ontology that does not possess a globally unique identifier (IRI), serving as a mechanism to describe unnamed or local instances. It is primarily utilized when an individual needs to be referenced to define relationships or restrictions without assigning it a permanent, resolvable name. The entity is uniquely identified within the local graph context by a blank node identifier, which distinguishes it from other anonymous individuals. Functioning as both an individual and an annotation value, it allows for the expression of complex structures involving specific, yet unnamed, components of the ontology.

   :parm node_id: Internal storage for the unique identifier representing the anonymous individual as a blank node in the RDF graph, ensuring local distinction without a globally unique IRI.
   :type node_id: rdflib.URIRef


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the anonymous individual, formatted to display the class name alongside its internal node identifier. The output follows the pattern 'AnonymousIndividual(node_id)', which is useful for debugging and logging to distinguish specific instances. This method does not modify the object's state and relies on the presence of the `node_id` attribute.

      :return: A string representation of the object, formatted as 'AnonymousIndividual(node_id)'.

      :rtype: str



   .. py:attribute:: _node_id
      :type:  rdflib.URIRef


   .. py:property:: node_id
      :type: rdflib.URIRef


      Updates the internal identifier for the anonymous individual by assigning the provided URI reference to the private `_node_id` attribute. This method acts as the setter for the `node_id` property, enabling the modification of the individual's unique identifier after instantiation. The input value is expected to be a valid `rdflib.URIRef`, and setting this value will directly mutate the state of the object.

      :param value: The URI reference representing the unique identifier for the node.
      :type value: rdflib.URIRef

