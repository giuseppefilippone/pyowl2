import rdflib

from pyowl2.abstracts.annotation_value import OWLAnnotationValue
from pyowl2.abstracts.individual import OWLIndividual


class OWLAnonymousIndividual(OWLAnnotationValue, OWLIndividual):
    """
    This class represents an entity within an OWL ontology that does not possess a globally unique identifier (IRI), serving as a mechanism to describe unnamed or local instances. It is primarily utilized when an individual needs to be referenced to define relationships or restrictions without assigning it a permanent, resolvable name. The entity is uniquely identified within the local graph context by a blank node identifier, which distinguishes it from other anonymous individuals. Functioning as both an individual and an annotation value, it allows for the expression of complex structures involving specific, yet unnamed, components of the ontology.

    :param node_id: Internal storage for the unique identifier representing the anonymous individual as a blank node in the RDF graph, ensuring local distinction without a globally unique IRI.
    :type node_id: rdflib.URIRef
    """

    def __init__(self, node_id: rdflib.URIRef) -> None:
        """
        Constructs a new instance of the OWL anonymous individual using the provided identifier. The method accepts an `rdflib.URIRef` representing the `node_id` and assigns it to the internal `_node_id` attribute. This establishes the identity of the individual within the graph structure without performing any validation or triggering external side effects.

        :param node_id: The URI reference that uniquely identifies the node.
        :type node_id: rdflib.URIRef
        """

        self._node_id: rdflib.URIRef = node_id

    @property
    def node_id(self) -> rdflib.URIRef:
        """
        Updates the internal identifier for the anonymous individual by assigning the provided URI reference to the private `_node_id` attribute. This method acts as the setter for the `node_id` property, enabling the modification of the individual's unique identifier after instantiation. The input value is expected to be a valid `rdflib.URIRef`, and setting this value will directly mutate the state of the object.

        :param value: The URI reference representing the unique identifier for the node.
        :type value: rdflib.URIRef
        """

        return self._node_id

    @node_id.setter
    def node_id(self, value: rdflib.URIRef) -> None:
        """Setter for node_id."""
        self._node_id = value

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the anonymous individual, formatted to display the class name alongside its internal node identifier. The output follows the pattern 'AnonymousIndividual(node_id)', which is useful for debugging and logging to distinguish specific instances. This method does not modify the object's state and relies on the presence of the `node_id` attribute.

        :return: A string representation of the object, formatted as 'AnonymousIndividual(node_id)'.

        :rtype: str
        """

        return f"AnonymousIndividual({self.node_id})"
