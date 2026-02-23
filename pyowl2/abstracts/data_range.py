import abc

from pyowl2.abstracts.object import OWLObject


class OWLDataRange(OWLObject, abc.ABC, metaclass=abc.ABCMeta):
    """
    This abstract base class represents a set of literal values within an ontology, typically corresponding to specific datatypes or logical combinations of datatypes. It serves as the foundational type for defining the value space of data properties, specifying what kinds of literal inputs—such as integers, strings, or restricted value sets—are permissible. Equality, ordering, and hashing for instances are determined exclusively by their string representations, meaning two objects are considered equal if their string forms match. Because this is an abstract class, it is intended to be subclassed by concrete implementations that define specific data ranges rather than instantiated directly.
    """


    __slots__ = ()

    def __eq__(self, value: object) -> bool:
        """
        Determines equality between the current instance and another object by comparing their string representations. The method returns `True` if the result of converting the current instance to a string matches the result of converting the provided value to a string. This approach allows for comparison based on the textual serialization of the data range, meaning two objects are considered equal if their string forms are identical, regardless of whether they are the same object in memory or share the same type.

        :param value: The object to compare against. Equality is determined by comparing the string representations of both objects.
        :type value: object

        :return: True if the string representation of the current object is equal to the string representation of the provided value, otherwise False.

        :rtype: bool
        """

        return str(self) == str(value)

    def __ne__(self, value: object) -> bool:
        """
        Determines inequality between the current instance and another object by comparing their string representations. This method returns `True` if the string representation of the current `OWLDataRange` differs from that of the provided value, and `False` otherwise. Because the comparison relies on string conversion, objects of differing types may be considered equal if their string representations happen to match.

        :param value: The object to compare against the current instance.
        :type value: object

        :return: True if the string representation of the current instance is not equal to the string representation of the provided value; otherwise, False.

        :rtype: bool
        """

        return str(self) != str(value)

    def __lt__(self, value: object) -> bool:
        """
        Implements the less-than comparison operator by evaluating the lexicographical order of the string representations of the current object and the provided value. This method enables the use of the standard `<` operator for sorting or ordering instances, relying on the output of the `str()` function rather than logical equivalence or internal structure. It accepts any object type as the comparison value, converting it to a string before evaluation, and does not modify the state of the object.

        :param value: The object to compare against, evaluated based on its string representation.
        :type value: object

        :return: True if the string representation of the current instance is lexicographically less than the string representation of the provided value.

        :rtype: bool
        """

        return str(self) < str(value)

    def __le__(self, value: object) -> bool:
        """
        Determines whether the current instance is less than or equal to the specified value by comparing their string representations. The comparison is performed lexicographically by converting both the instance and the provided object to strings, regardless of the object's type. This behavior allows for sorting and ordering operations based on the textual representation of the data range, rather than its semantic properties.

        :param value: The object to compare against, which is converted to a string for the comparison.
        :type value: object

        :return: True if the string representation of the current object is less than or equal to the string representation of the provided value, otherwise False.

        :rtype: bool
        """

        return str(self) <= str(value)

    def __gt__(self, value: object) -> bool:
        """
        Determines whether the current instance is considered greater than the specified value by comparing their string representations. The method converts both the instance and the provided value to strings and performs a lexicographical comparison, returning `True` if the instance's string representation is greater. This implementation allows for comparison with any object type, provided the object can be converted to a string, and does not modify the state of either operand.

        :param value: The object to compare against the current instance, where the comparison is performed on the string representations of the objects.
        :type value: object

        :return: True if the string representation of the current object is lexicographically greater than the string representation of the provided value, otherwise False.

        :rtype: bool
        """

        return str(self) > str(value)

    def __ge__(self, value: object) -> bool:
        """
        Determines whether the current instance is greater than or equal to the specified object by comparing their string representations. This method enables the use of the greater-than-or-equal-to operator, facilitating sorting and ordering operations based on the lexical value of the objects. The comparison is case-sensitive and relies on standard lexicographical ordering, converting the provided value to a string if necessary.

        :param value: The object to compare against, converted to a string for comparison.
        :type value: object

        :return: True if the string representation of the object is greater than or equal to the string representation of the provided value.

        :rtype: bool
        """

        return str(self) >= str(value)

    def __hash__(self) -> int:
        """
        Computes a hash value for the instance, allowing it to be used as a key in dictionaries or stored in sets. The implementation delegates to the hash of the object's string representation, meaning the resulting integer is directly derived from the output of the `__str__` method. This ensures that objects with identical string representations produce the same hash code.

        :return: An integer hash value computed from the string representation of the object.

        :rtype: int
        """

        return hash(str(self))

    def __repr__(self) -> str:
        """
        Returns the official string representation of the OWL data range object. This implementation delegates the formatting logic directly to the `__str__` method, ensuring that the output used for debugging and logging mirrors the user-facing string representation. The method does not modify the state of the object and simply returns the result of the string conversion.

        :return: A string representation of the object.

        :rtype: str
        """

        return str(self)
