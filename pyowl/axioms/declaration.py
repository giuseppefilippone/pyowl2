import typing

from pyowl.abstracts.axiom import OWLAxiom
from pyowl.abstracts.entity import OWLEntity
from pyowl.base.annotation import OWLAnnotation


class OWLDeclaration(OWLAxiom):
    """An axiom that introduces a named entity (class, property, individual) into the ontology."""

    def __init__(
        self,
        entity: OWLEntity,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        super().__init__(annotations)
        # super().__init__()
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = (
        #     sorted(annotations) if annotations else annotations
        # )
        self._entity: OWLEntity = entity

    # @property
    # def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
    #     """Getter for axiom_annotations."""
    #     return self._axiom_annotations

    # @axiom_annotations.setter
    # def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
    #     """Setter for axiom_annotations."""
    #     self._axiom_annotations = sorted(value) if value else value

    @property
    def entity(self) -> OWLEntity:
        """Getter for entity."""
        return self._entity

    @entity.setter
    def entity(self, value: OWLEntity) -> None:
        """Setter for entity."""
        self._entity = value

    def __str__(self) -> str:
        if self.axiom_annotations:
            return f"Declaration({self.axiom_annotations} {self.entity})"
        else:
            return f"Declaration([] {self.entity})"
