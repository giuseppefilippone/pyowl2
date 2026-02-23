pyowl2.axioms.object_property_axiom.object_property_chain
=========================================================

.. py:module:: pyowl2.axioms.object_property_axiom.object_property_chain



.. ── LLM-GENERATED DESCRIPTION START ──

Represents a sorted sequence of object property expressions used to define property chain axioms within an ontology.


Description
-----------


The implementation automatically sorts the provided expressions upon initialization to establish a canonical form, meaning the original input order is not preserved. Comparisons and hashing operations rely on this sorted structure and the resulting string representation, ensuring that two chains containing the same properties are considered equal regardless of the order in which they were provided. Requiring at least two property expressions enforces the structural constraints necessary for valid property chain axioms while providing a standardized string output for debugging and serialization.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   pyowl2.axioms.object_property_axiom.object_property_chain.OWLObjectPropertyChain


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_pyowl2_axioms_object_property_axiom_object_property_chain_OWLObjectPropertyChain.png
       :alt: UML Class Diagram for OWLObjectPropertyChain
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OWLObjectPropertyChain**

.. only:: latex

    .. figure:: /_uml/class_pyowl2_axioms_object_property_axiom_object_property_chain_OWLObjectPropertyChain.pdf
       :alt: UML Class Diagram for OWLObjectPropertyChain
       :align: center
       :width: 13.2cm
       :class: uml-diagram

       UML Class Diagram for **OWLObjectPropertyChain**

.. py:class:: OWLObjectPropertyChain(expressions: list[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression])

   This class represents a sequence of object property expressions used to define property chain axioms within an ontology, enabling the inference of indirect relationships between individuals. It requires a list of at least two property expressions upon initialization. Notably, the implementation automatically sorts the provided expressions, meaning the input order is not preserved for equality or hashing purposes; instead, identity is determined by the sorted string representation of the chain.

   :parm chain: Internal storage for the object property expressions comprising the chain, maintained in a sorted order to facilitate deterministic comparisons and string representations.
   :type chain: list[OWLObjectPropertyExpression]


   .. py:method:: __eq__(value: object) -> bool

      Checks if the current instance is equal to the specified object by comparing their string representations. This method returns `True` if the result of converting the current instance to a string is identical to the string conversion of the provided value, and `False` otherwise. Consequently, equality is determined based on the lexical output of the object rather than direct attribute comparison or object identity.

      :param value: The object to compare against. Equality is determined by comparing the string representation of this value to the string representation of the current instance.
      :type value: object

      :return: True if the string representation of the object is equal to the string representation of the provided value, otherwise False.

      :rtype: bool



   .. py:method:: __ge__(value: object) -> bool

      Determines whether the current instance is greater than or equal to the specified value by comparing their string representations. The method converts both the object property chain and the provided value to strings and performs a standard lexicographical comparison. This behavior enables sorting and ordering operations based on the textual format of the objects, though it may not reflect structural or semantic relationships within the ontology.

      :param value: The object to compare against, where the comparison is performed on the string representations.
      :type value: object

      :return: True if the string representation of the current object is lexicographically greater than or equal to the string representation of the specified value, otherwise False.

      :rtype: bool



   .. py:method:: __gt__(value: object) -> bool

      Determines whether the current object property chain is greater than the specified value by comparing their string representations. The comparison is performed lexicographically, converting both the instance and the input value to strings before evaluation. This method returns True if the string representation of the current instance is lexicographically greater than that of the value, and False otherwise.

      :param value: The object to compare against the current instance, evaluated based on its string representation.
      :type value: object

      :return: True if the string representation of the object is greater than the string representation of the specified value, otherwise False.

      :rtype: bool



   .. py:method:: __hash__() -> int

      Computes the hash code for the object property chain, enabling its use in hash-based collections like sets and dictionaries. The implementation derives the hash value from the string representation of the chain, ensuring that objects with identical string representations produce the same hash. This method relies on the stability and uniqueness of the `__str__` method to maintain the contract that equal objects have equal hash values.

      :return: An integer hash value computed from the object's string representation.

      :rtype: int



   .. py:method:: __le__(value: object) -> bool

      Determines if the current object property chain is less than or equal to the specified value by comparing their string representations. This method converts both the instance and the input value to strings and performs a lexicographical comparison, returning True if the instance's string representation comes before or is identical to the value's. The comparison logic depends entirely on the output of the `__str__` method rather than the internal structure of the objects, meaning that the sort order is defined by the specific string formatting of the class.

      :param value: The object to compare against the current instance.
      :type value: object

      :return: True if the string representation of the object is less than or equal to the string representation of the provided value, otherwise False.

      :rtype: bool



   .. py:method:: __lt__(value: object) -> bool

      Implements the less-than comparison operator by evaluating the lexicographical order of the string representations of the objects. It returns `True` if the string representation of the current instance is alphabetically smaller than that of the provided value. This behavior allows instances to be sorted or compared using standard Python operators, though the ordering is strictly dependent on the specific format of the string output rather than the internal structure of the property chain.

      :param value: The object to compare against the current instance. The comparison is performed based on the string representation of the provided object.
      :type value: object

      :return: True if the string representation of the current object is lexicographically less than the string representation of the provided value.

      :rtype: bool



   .. py:method:: __ne__(value: object) -> bool

      Determines inequality between the current object and another value by comparing their string representations. The method converts both the instance and the provided value to strings and returns `True` if these representations differ. This implementation allows for comparison with any object type, relying on the specific string formatting of the property chain to define uniqueness.

      :param value: The object to compare against the current instance, where the comparison is based on the string representations of the objects.
      :type value: object

      :return: True if the string representation of the current object is not equal to the string representation of the provided value, otherwise False.

      :rtype: bool



   .. py:method:: __repr__() -> str

      Returns a string representation of the object property chain. This implementation delegates directly to the `__str__` method, ensuring that the output used for debugging and logging matches the standard human-readable format of the object. The method has no side effects and relies on the string conversion logic defined elsewhere in the class.

      :return: The string representation of the object.

      :rtype: str



   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the object property chain, formatted as the class name followed by the sequence of properties in the chain enclosed in parentheses. The properties within the chain are joined into a single string separated by spaces. This method is primarily used for debugging and logging purposes to provide a concise textual summary of the chain's structure.

      :return: A string representation of the object, displaying the class name and the elements of the chain joined by spaces.

      :rtype: str



   .. py:attribute:: _chain
      :type:  list[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression]


   .. py:property:: chain
      :type: list[pyowl2.abstracts.object_property_expression.OWLObjectPropertyExpression]


      Updates the internal sequence of object properties that constitute this chain by accepting a list of OWLObjectPropertyExpression instances. The method sorts the input list to establish a canonical order before storing it, which means the original order of the provided elements is not preserved. This operation requires that the elements in the list be comparable to ensure successful sorting.

      :param value: A list of object property expressions that constitute the property chain.
      :type value: list[OWLObjectPropertyExpression]

