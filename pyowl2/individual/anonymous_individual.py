import rdflib

from pyowl2.abstracts.annotation_value import OWLAnnotationValue
from pyowl2.abstracts.individual import OWLIndividual


class OWLAnonymousIndividual(OWLAnnotationValue, OWLIndividual):
    """An individual without a globally unique identifier (IRI), typically used for unnamed entities."""

    def __init__(self, node_id: rdflib.URIRef) -> None:
        self._node_id: rdflib.URIRef = node_id

    @property
    def node_id(self) -> rdflib.URIRef:
        """Getter for node_id."""
        return self._node_id

    @node_id.setter
    def node_id(self, value: rdflib.URIRef) -> None:
        """Setter for node_id."""
        self._node_id = value

    def __str__(self) -> str:
        return f"AnonymousIndividual({self.node_id})"
