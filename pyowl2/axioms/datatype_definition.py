import typing

from pyowl2.abstracts.axiom import OWLAxiom
from pyowl2.abstracts.data_range import OWLDataRange
from pyowl2.base.annotation import OWLAnnotation
from pyowl2.base.datatype import OWLDatatype


class OWLDatatypeDefinition(OWLAxiom):
    """
    This axiom serves to define a new datatype within an ontology by equating it to a specific data range, which may consist of simple literals or complex restrictions on existing datatypes. It functions as a logical building block, allowing the newly created datatype to be utilized in other parts of the ontology to enforce precise value constraints. The definition is composed of a target datatype and a defining data range, and it can optionally include annotations to provide additional context or metadata about the axiom itself.

    :param datatype: The new datatype being defined by this axiom, identified by its IRI.
    :type datatype: OWLDatatype
    :param data_range: Specifies the set of values or constraints that define the new datatype.
    :type data_range: OWLDataRange
    """

    def __init__(
        self,
        datatype: OWLDatatype,
        data_range: OWLDataRange,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Initializes a new instance representing a datatype definition axiom, which establishes a definition for a specific OWL datatype based on a provided data range. This constructor accepts the target datatype, the defining data range, and an optional list of annotations to associate with the axiom. It stores the datatype and data range as internal attributes and delegates the initialization of annotations to the parent class.

        :param datatype: The OWL datatype being defined or restricted by this axiom.
        :type datatype: OWLDatatype
        :param data_range: The data range defining the set of literal values.
        :type data_range: OWLDataRange
        :param annotations: A list of annotations to be associated with the axiom. If None, no annotations are added.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

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
        """
        Updates the OWL datatype associated with this definition by assigning the provided value to the internal storage. This setter allows the underlying data type reference to be replaced or initialized. The method accepts an instance of OWLDatatype and directly overwrites the existing attribute without performing additional validation.

        :param value: The OWL datatype to assign.
        :type value: OWLDatatype
        """

        return self._datatype

    @datatype.setter
    def datatype(self, value: OWLDatatype) -> None:
        """Setter for datatype."""
        self._datatype = value

    @property
    def data_range(self) -> OWLDataRange:
        """
        Updates the data range associated with this OWL datatype definition by assigning the provided `OWLDataRange` object to the internal state. This operation overwrites any existing data range, effectively modifying the definition's constraints in place. While the method signature expects an instance of `OWLDataRange`, the implementation does not perform explicit runtime validation of the input type.

        :param value: The OWL data range to assign.
        :type value: OWLDataRange
        """

        return self._data_range

    @data_range.setter
    def data_range(self, value: OWLDataRange) -> None:
        """Setter for data_range."""
        self._data_range = value

    def __str__(self) -> str:
        """
        Returns a formatted string representation of the datatype definition axiom, incorporating the axiom's annotations, the specific datatype being defined, and the data range used for the definition. If the axiom has no associated annotations, the representation explicitly includes an empty list in place of the annotations to maintain a consistent structure.

        :return: A string representation of the datatype definition axiom, formatted as `DatatypeDefinition([annotations] datatype data_range)`.

        :rtype: str
        """

        if self.axiom_annotations:
            return f"DatatypeDefinition({self.axiom_annotations} {self.datatype} {self.data_range})"
        else:
            return f"DatatypeDefinition([] {self.datatype} {self.data_range})"
