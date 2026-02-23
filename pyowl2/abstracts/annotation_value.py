import abc

from pyowl2.abstracts.object import OWLObject


class OWLAnnotationValue(OWLObject, abc.ABC, metaclass=abc.ABCMeta):
    """
    Represents the specific value assigned to an annotation property for a given subject in the Web Ontology Language (OWL). As an abstract base class, it defines a common interface for different types of values, which may include anonymous individuals, IRIs, or Literals. The implementation enforces that equality, ordering, and hashing are determined solely by the string representation of the object, ensuring that comparisons are based on lexical form rather than object identity.
    """


    __slots__ = ()

    def __eq__(self, value: object) -> bool:
        """
        Determines whether the current instance is equal to another object by comparing their string representations. The method converts both the current object and the provided value to strings using the built-in `str()` function and returns `True` if the resulting strings are identical. This implementation allows for equality checks between objects of potentially different types, provided they produce the same string output.

        :param value: The object to compare against. Equality is determined by comparing the string representation of this object with the string representation of the current instance.
        :type value: object

        :return: True if the string representation of the instance is equal to the string representation of the provided value, otherwise False.

        :rtype: bool
        """

        return str(self) == str(value)

    def __ne__(self, value: object) -> bool:
        """
        Determines inequality by comparing the string representation of the current instance with the string representation of the provided object. This implementation allows for comparison against any object type, as both operands are converted to strings before evaluation. The method returns True if the string representations differ, indicating inequality, and False otherwise.

        :param value: The object to compare with. The comparison is performed by converting both the current instance and this value to strings and checking if they are not equal.
        :type value: object

        :return: True if the string representation of the object is not equal to the string representation of the provided value, otherwise False.

        :rtype: bool
        """

        return str(self) != str(value)

    def __lt__(self, value: object) -> bool:
        """
        Determines whether the current instance is considered less than the specified object based on their string representations. The comparison is performed by converting both the current instance and the provided value to strings and evaluating the lexicographical order. This implementation allows for sorting and ordering of `OWLAnnotationValue` instances, though the result depends entirely on the string formatting logic rather than the intrinsic semantic value of the objects. If the provided object cannot be successfully converted to a string, the method may raise an exception.

        :param value: The object to compare against, converted to a string for comparison.
        :type value: object

        :return: True if the string representation of the current object is lexicographically less than the string representation of the provided value, otherwise False.

        :rtype: bool
        """

        return str(self) < str(value)

    def __le__(self, value: object) -> bool:
        """
        Determines if the current instance is less than or equal to a specified value by comparing their string representations. The comparison is performed lexicographically using the standard string ordering, converting both the instance and the provided value to strings before evaluation. This allows the object to be compared against any other object that supports string conversion, facilitating sorting and ordering operations based on textual representation.

        :param value: The object to compare against, where the comparison is performed based on the string representations of the operands.
        :type value: object

        :return: True if the string representation of the current instance is lexicographically less than or equal to the string representation of the specified value, otherwise False.

        :rtype: bool
        """

        return str(self) <= str(value)

    def __gt__(self, value: object) -> bool:
        """
        Determines if the current instance is greater than the provided object based on their string representations. This method converts both the annotation value and the input value to strings and performs a lexicographical comparison. It returns True if the string representation of the current instance is greater than that of the input value, and False otherwise.

        :param value: The object to compare against, where the comparison is based on the string representation of the objects.
        :type value: object

        :return: True if the string representation of the current object is lexicographically greater than the string representation of the provided value, otherwise False.

        :rtype: bool
        """

        return str(self) > str(value)

    def __ge__(self, value: object) -> bool:
        """
        Determines whether the current instance is greater than or equal to the specified value by comparing their string representations. The method converts both the current object and the provided value to strings and performs a lexicographical comparison, returning True if the string representation of the current instance is greater than or equal to that of the value. This behavior implies that the ordering is based on string formatting rather than the logical structure of the underlying ontology entities.

        :param value: The object to compare against. It is converted to a string before the comparison.
        :type value: object

        :return: True if the string representation of the current object is lexicographically greater than or equal to the string representation of the provided value; otherwise, False.

        :rtype: bool
        """

        return str(self) >= str(value)

    def __hash__(self) -> int:
        """
        Calculates a hash code for the object by converting it to a string and hashing the result. This allows the instance to be used in hash-based collections like dictionaries and sets. The method relies on the string representation of the object to determine the hash, meaning that any two objects with the same string output will share the same hash value.

        :return: An integer hash value derived from the string representation of the object.

        :rtype: int
        """

        return hash(str(self))

    def __repr__(self) -> str:
        """
        Returns a string representation of the OWL annotation value, typically used for debugging and logging. This implementation delegates directly to the `__str__` method, meaning the output is the same as the informal string representation rather than a strict, unambiguous constructor format. The method performs no modifications to the object's state and relies on the underlying string conversion logic to generate the result.

        :return: Returns the string representation of the object.

        :rtype: str
        """

        return str(self)
