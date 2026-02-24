import abc
import typing

from pyowl2.abstracts.object import OWLObject
from pyowl2.base.annotation import OWLAnnotation


class OWLAxiom(OWLObject, abc.ABC, metaclass=abc.ABCMeta):
    """
    This abstract base class represents a fundamental assertion or statement within an ontology, serving as the foundational component for defining the logical structure of the knowledge base. It supports the attachment of optional metadata through a list of annotations, which are automatically sorted upon assignment to maintain a consistent state. Instances of this class utilize their string representation to determine equality, hash values, and ordering, meaning that comparisons are based on the textual form of the axiom rather than object identity.

    :param axiom_annotations: Sorted list of annotations providing metadata about the axiom, or None if no annotations are present.
    :type axiom_annotations: typing.Optional[list[OWLAnnotation]]
    """

    # __slots__ = ()
    def __init__(self, annotations: typing.Optional[list[OWLAnnotation]] = None):
        """
        Initializes the instance with an optional list of annotations, storing them in a normalized, sorted state to ensure consistent structural representation. If annotations are provided, they are sorted lexicographically before assignment to the internal attribute; otherwise, the annotation collection remains unset. This behavior facilitates reliable comparison and hashing of axioms by decoupling the internal state from the arbitrary order of input annotations.

        :param annotations: Optional list of annotations to be associated with the axiom. If provided, the list is sorted before storage.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = (
            sorted(annotations) if annotations else annotations
        )

    @property
    def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
        """
        Sets the annotations associated with the OWL axiom, overwriting any previously stored annotations. The method accepts a list of OWLAnnotation objects or None; if a non-empty list is provided, it is sorted before being assigned to the internal state to maintain a consistent order. If the input is None or an empty list, it is stored as is without sorting.

        :param value: A list of OWL annotations to assign to the axiom.
        :type value: typing.Optional[list[OWLAnnotation]]
        """

        return self._axiom_annotations

    @axiom_annotations.setter
    def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
        """Setter for axiom_annotations."""
        self._axiom_annotations = sorted(value) if value else value

    def __eq__(self, value: object) -> bool:
        """
        Determines equality between the current instance and another object by comparing their string representations. This method returns True if the result of converting the current object to a string is identical to the string representation of the provided value. Consequently, equality is defined based on the textual serialization of the axiom rather than object identity or direct attribute comparison, and it allows for comparison with objects of different types provided their string representations match.

        :param value: The object to compare against. Equality is determined by comparing the string representation of this object with the string representation of the current instance.
        :type value: object

        :return: True if the string representation of the instance is equal to the string representation of the provided value; otherwise, False.

        :rtype: bool
        """

        return str(self) == str(value)

    def __ne__(self, value: object) -> bool:
        """
        Determines whether the current axiom is not equal to the specified object by comparing their string representations. The method converts both the instance and the provided value to strings and returns True if they differ, allowing for comparison against arbitrary object types. This behavior implies that inequality is defined based on the textual serialization of the axioms rather than strict structural identity.

        :param value: The item to compare against the current instance, converted to a string for the comparison.
        :type value: object

        :return: True if the string representation of the instance is not equal to the string representation of the specified value, False otherwise.

        :rtype: bool
        """

        return str(self) != str(value)

    def __lt__(self, value: object) -> bool:
        """
        Determines if the current instance is considered less than the provided value based on their string representations. This method enables the use of the less-than operator (`<`) for `OWLAxiom` objects by performing a lexicographical comparison between the string representation of the current axiom and the string representation of the input value. Because the comparison relies on the textual format rather than the logical structure of the axioms, this behavior is primarily intended for sorting or ordering purposes rather than semantic evaluation.

        :param value: The object to compare against the current instance, compared based on their string representations.
        :type value: object

        :return: True if the string representation of the current object is lexicographically less than the string representation of the provided value, otherwise False.

        :rtype: bool
        """

        return str(self) < str(value)

    def __le__(self, value: object) -> bool:
        """
        Implements the less-than-or-equal-to comparison operator for the axiom by comparing the lexicographical order of their string representations. This method determines if the string representation of the current instance is less than or equal to that of the provided object, which may be any entity supporting string conversion. It is important to note that this comparison is based on syntax rather than semantic equivalence, meaning axioms that are logically identical but formatted differently may not compare as equal.

        :param value: The object to compare against the current instance, where the comparison is performed on the string representations of the objects.
        :type value: object

        :return: True if the string representation of the current object is less than or equal to the string representation of the specified value; otherwise, False.

        :rtype: bool
        """

        return str(self) <= str(value)

    def __gt__(self, value: object) -> bool:
        """
        Determines if the current instance is considered greater than the provided object based on their string representations. The comparison is performed lexicographically by converting both the axiom and the input value to strings. This allows the axiom to be compared against any object that supports string conversion, though the specific ordering depends entirely on the format of the string representation.

        :param value: The object to compare with the current instance. The comparison is performed on the string representations of the objects.
        :type value: object

        :return: True if the string representation of the current object is greater than the string representation of the provided value.

        :rtype: bool
        """

        return str(self) > str(value)

    def __ge__(self, value: object) -> bool:
        """
        Determines if the current axiom is greater than or equal to another object based on their string representations. This method enables the use of the `>=` operator with `OWLAxiom` instances by performing a lexicographical comparison between the string representation of the current instance and the string representation of the provided value. Note that this comparison relies on the textual format of the axioms rather than their logical semantics or structural properties.

        :param value: The object to compare against, where the comparison is performed on the string representations of the two objects.
        :type value: object

        :return: True if the string representation of the instance is greater than or equal to the string representation of the provided value, otherwise False.

        :rtype: bool
        """

        return str(self) >= str(value)

    def __hash__(self) -> int:
        """
        Calculates the hash code for the axiom by hashing its string representation, thereby allowing the object to be used in hash-based collections such as sets and dictionaries. This implementation delegates the hashing logic to the `__str__` method, which requires that the string output be deterministic and consistent with the object's equality definition to maintain the invariant that equal objects have equal hash values. Consequently, any changes to the string formatting logic will directly impact the hash value and the object's behavior in hashed containers.

        :return: An integer hash value derived from the string representation of the object.

        :rtype: int
        """

        return hash(str(self))

    def __repr__(self) -> str:
        """
        Returns a string representation of the OWL axiom by delegating directly to the standard string conversion method. This implementation ensures that the formal representation is identical to the string representation, providing a human-readable format suitable for debugging and logging. The method does not modify the object's state and relies on the underlying string conversion logic to handle the specific formatting of the axiom's components.

        :return: The string representation of the object, identical to the output of str().

        :rtype: str
        """

        return str(self)
