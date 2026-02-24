import typing

from pyowl2.abstracts.axiom import OWLAxiom
from pyowl2.abstracts.entity import OWLEntity
from pyowl2.base.annotation import OWLAnnotation


class OWLDeclaration(OWLAxiom):
    """
    This axiom serves as the formal mechanism for introducing a named entity—such as a class, property, or individual—into the ontology's vocabulary. By asserting the existence of an entity, this declaration enables it to be referenced and utilized within other axioms and logical expressions throughout the ontology. To use this class, instantiate it with the specific `OWLEntity` to be declared, optionally providing a list of annotations to attach metadata or contextual information to the declaration itself.

    :param entity: The OWL entity (class, property, or individual) that is being declared and introduced into the ontology.
    :type entity: OWLEntity
    """

    def __init__(
        self,
        entity: OWLEntity,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Initializes a new OWL declaration axiom, which serves to introduce a specific entity into the ontology. The constructor accepts an `OWLEntity` instance representing the subject of the declaration and stores it internally. It also accepts an optional list of `OWLAnnotation` objects, delegating their management to the parent class, thereby allowing the axiom to carry associated metadata. If the annotations list is omitted or None, the initialization proceeds without annotations.

        :param entity: The OWL entity associated with this object.
        :type entity: OWLEntity
        :param annotations: Optional list of annotations to associate with the entity.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

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
        """
        Assigns the specified OWL entity to this declaration, replacing the existing entity reference. This method updates the internal state of the declaration to point to the provided entity object, effectively changing the subject of the axiom.

        :param value: The ontology object to assign.
        :type value: OWLEntity
        """

        return self._entity

    @entity.setter
    def entity(self, value: OWLEntity) -> None:
        """Setter for entity."""
        self._entity = value

    def __str__(self) -> str:
        """
        Returns a string representation of the OWL declaration axiom, formatted to display the annotations and the declared entity. If the axiom contains annotations, they are included within the parentheses; otherwise, an empty list representation is used. This method does not modify the object's state and is intended for generating human-readable output or debugging information.

        :return: Returns a string representation of the declaration, including the axiom annotations and the entity.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"Declaration({self.axiom_annotations} {self.entity})"
        else:
            return f"Declaration([] {self.entity})"
