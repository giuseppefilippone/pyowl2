import typing

from pyowl.abstracts.axiom import OWLAxiom
from pyowl.abstracts.data_range import OWLDataRange
from pyowl.base.annotation import OWLAnnotation
from pyowl.base.datatype import OWLDatatype


class OWLDatatypeDefinition(OWLAxiom):
    """An axiom that defines a new datatype in terms of existing datatypes."""

    def __init__(
        self,
        datatype: OWLDatatype,
        data_range: OWLDataRange,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        super().__init__(annotations)
        # super().__init__()
        # self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = (
        #     sorted(annotations) if annotations else annotations
        # )
        self._datatype: OWLDatatype = datatype
        self._data_range: OWLDataRange = data_range

    # @property
    # def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
    #     """Getter for axiom_annotations."""
    #     return self._axiom_annotations

    # @axiom_annotations.setter
    # def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
    #     """Setter for axiom_annotations."""
    #     self._axiom_annotations = sorted(value) if value else value

    @property
    def datatype(self) -> OWLDatatype:
        """Getter for datatype."""
        return self._datatype

    @datatype.setter
    def datatype(self, value: OWLDatatype) -> None:
        """Setter for datatype."""
        self._datatype = value

    @property
    def data_range(self) -> OWLDataRange:
        """Getter for data_range."""
        return self._data_range

    @data_range.setter
    def data_range(self, value: OWLDataRange) -> None:
        """Setter for data_range."""
        self._data_range = value

    def __str__(self) -> str:
        if self.axiom_annotations:
            return f"DatatypeDefinition({self.axiom_annotations} {self.datatype} {self.data_range})"
        else:
            return f"DatatypeDefinition([] {self.datatype} {self.data_range})"
