import typing

from pyowl2.abstracts.axiom import OWLAxiom
from pyowl2.abstracts.class_expression import OWLClassExpression
from pyowl2.abstracts.data_property_expression import OWLDataPropertyExpression
from pyowl2.abstracts.individual import OWLIndividual
from pyowl2.abstracts.object import OWLObject
from pyowl2.abstracts.object_property_expression import OWLObjectPropertyExpression
from pyowl2.axioms.assertion.class_assertion import OWLClassAssertion
from pyowl2.axioms.class_axiom.disjoint_classes import OWLDisjointClasses
from pyowl2.axioms.class_axiom.disjoint_union import OWLDisjointUnion
from pyowl2.axioms.class_axiom.equivalent_classes import OWLEquivalentClasses
from pyowl2.axioms.class_axiom.sub_class_of import OWLSubClassOf
from pyowl2.axioms.has_key import OWLHasKey
from pyowl2.base.annotation import OWLAnnotation
from pyowl2.base.iri import IRI
from pyowl2.base.owl_class import OWLClass
from pyowl2.class_expression.object_all_values_from import OWLObjectAllValuesFrom
from pyowl2.class_expression.object_complement_of import OWLObjectComplementOf
from pyowl2.class_expression.object_exact_cardinality import OWLObjectExactCardinality
from pyowl2.class_expression.object_intersection_of import OWLObjectIntersectionOf
from pyowl2.class_expression.object_max_cardinality import OWLObjectMaxCardinality
from pyowl2.class_expression.object_min_cardinality import OWLObjectMinCardinality
from pyowl2.class_expression.object_one_of import OWLObjectOneOf
from pyowl2.class_expression.object_some_values_from import OWLObjectSomeValuesFrom
from pyowl2.class_expression.object_union_of import OWLObjectUnionOf


class OWLFullClass(OWLObject):
    """
    This class acts as a comprehensive container for an OWL (Web Ontology Language) class definition, combining the core class identity with its logical axioms and metadata annotations. It provides a fluent interface for constructing complex ontology structures, allowing users to define subclass relationships, equivalences, disjointness, and various property restrictions such as cardinality and value constraints. By managing an internal list of axioms, it ensures that duplicate logical statements are not added, while offering properties to easily retrieve specific subsets of axioms, such as intersections, unions, or class assertions. The class is designed to accept both raw class expressions and other full class instances as arguments, facilitating flexible ontology modeling.

    :param class: The underlying OWLClass instance representing the core definition of the class, identified by its IRI, which serves as the subject for the axioms and annotations managed by this wrapper.
    :type class: OWLClass
    :param axioms: A list of axioms defining the logical relationships and constraints for the class, including subclass relationships, equivalence, disjointness, and cardinality restrictions.
    :type axioms: list[OWLAxiom]
    :param annotations: Stores the optional list of annotations associated with the class, providing metadata such as labels or comments.
    :type annotations: typing.Optional[list[OWLAnnotation]]

    :raises TypeError: Raised when the input provided to methods defining class relationships (such as equivalence, disjointness, or unions) is not an `OWLClassExpression`, an `OWLFullClass`, or a list of these types.
    """

    def __init__(self, iri: IRI) -> None:
        """
        Initializes a new instance representing an OWL class, identified by the provided Internationalized Resource Identifier (IRI). The constructor creates an internal OWLClass object to encapsulate the entity's identity and prepares the state for storing logical statements and metadata. It establishes an empty list to hold associated axioms and initializes the annotations attribute to None, indicating that no annotations are currently defined.

        :param iri: The unique identifier for the OWL class.
        :type iri: IRI
        """

        self._class: OWLClass = OWLClass(iri)
        self._axioms: list[OWLAxiom] = []
        self._annotations: typing.Optional[list[OWLAnnotation]] = None

    @staticmethod
    def thing() -> typing.Self:
        """
        This static method acts as a factory for the root class of the OWL hierarchy, returning an `OWLFullClass` instance that represents the `owl:Thing` entity. As the most general class in the Web Ontology Language, `owl:Thing` implicitly includes all individuals and serves as the ultimate superclass for all other defined classes. The implementation relies on the standard IRI associated with `owl:Thing` to instantiate the object, ensuring that the returned class aligns with the W3C OWL specification. Since this method takes no arguments and performs no state mutations, it has no side effects and simply provides a semantic reference to the universal class.

        :return: An instance representing the OWL "Thing" class, the most general class in the ontology that encompasses all individuals.

        :rtype: typing.Self
        """

        return OWLFullClass(IRI.thing_iri())

    @staticmethod
    def nothing() -> typing.Self:
        """
        This static method serves as a factory for creating an `OWLFullClass` instance that represents the OWL `Nothing` class, which is the empty class containing no individuals. It initializes the instance using the standard IRI `http://www.w3.org/2002/07/owl#Nothing` obtained from the `IRI` utility. As the most specific class in the OWL hierarchy, `Nothing` is implicitly a subclass of every other class, and this method provides a convenient way to reference it without manually constructing the IRI. The function has no side effects and returns a new instance on every call.

        :return: An OWLFullClass instance representing the OWL "Nothing" class, which is the empty class containing no individuals.

        :rtype: typing.Self
        """

        return OWLFullClass(IRI.nothing_iri())

    @property
    def class_(self) -> OWLClass:
        """
        Retrieves the `OWLClass` object that this `OWLFullClass` instance represents or wraps. As a property, it provides read-only access to the internal `_class` attribute, ensuring that the underlying ontology class can be accessed without triggering side effects or state changes.

        :return: The OWL class associated with this instance.

        :rtype: OWLClass
        """

        return self._class

    @property
    def axioms(self) -> list[OWLAxiom]:
        """
        Retrieves the list of axioms associated with this OWL class instance. This property provides direct access to the internal collection of `OWLAxiom` objects stored within the class, representing the logical statements that define or describe it. The method returns the list reference without performing any computation or side effects, though modifications to the returned list may alter the internal state of the object.

        :return: A list of axioms associated with this object.

        :rtype: list[OWLAxiom]
        """

        return self._axioms

    @property
    def annotations(self) -> typing.Optional[list[OWLAnnotation]]:
        """
        Updates the annotations associated with the OWL class by replacing the existing collection with the provided value. The method accepts a list of OWLAnnotation objects or None, allowing the annotations to be explicitly set or cleared. This operation directly modifies the internal state of the instance to reflect the new metadata.

        :param value: A list of OWL annotations to assign to the object, or None.
        :type value: typing.Optional[list[OWLAnnotation]]
        """

        return self._annotations

    @annotations.setter
    def annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
        self._annotations = value

    @property
    def assertions(self) -> list[OWLClassAssertion]:
        """
        Retrieves a list of class assertion axioms that explicitly declare individuals as instances of this class. By filtering the internal collection of axioms, this method identifies all statements where an individual is asserted to belong to the current class expression. The returned list contains `OWLClassAssertion` objects, which encapsulate the specific individuals along with any annotations attached to those assertions. This operation is read-only and returns a new list, meaning modifications to the result will not affect the underlying ontology structure, and it will return an empty list if no such assertions exist.

        :return: A list of `OWLClassAssertion` axioms that assert individuals as instances of this class.

        :rtype: list[OWLClassAssertion]
        """

        return [axiom for axiom in self.axioms if isinstance(axiom, OWLClassAssertion)]

    @property
    def intersections(self) -> list[OWLObjectIntersectionOf]:
        """
        Retrieves a list of axioms that define this class as the logical intersection of multiple class expressions. This property filters the class's internal collection of axioms, returning only those instances of `OWLObjectIntersectionOf`. The operation is read-only and returns a new list; if no intersection axioms are associated with the class, an empty list is returned.

        :return: A list of axioms representing the intersection of class expressions associated with this class, indicating the conditions an individual must satisfy to be an instance.

        :rtype: list[OWLObjectIntersectionOf]
        """

        return [
            axiom for axiom in self.axioms if isinstance(axiom, OWLObjectIntersectionOf)
        ]

    @property
    def unions(self) -> list[OWLObjectOneOf]:
        """
        This property retrieves a list of axioms associated with the current class that are instances of `OWLObjectOneOf`. It filters the class's internal collection of axioms to isolate those representing union constructs, as implied by the property name. The returned list is a new list instance, ensuring that modifications to the collection will not affect the underlying state of the class. If no axioms of this specific type are present, the property returns an empty list.

        :return: A list of OWLObjectOneOf axioms associated with this object.

        :rtype: list[OWLObjectOneOf]
        """

        return [axiom for axiom in self.axioms if isinstance(axiom, OWLObjectOneOf)]

    @property
    def is_complement(self) -> bool:
        """
        Indicates whether this class is defined as a complement of another class by examining its associated axioms. The property returns True if at least one of the axioms is an instance of OWLObjectComplementOf, signifying that the class represents a logical negation of another class. If no such complement axioms are present, it returns False.

        :return: True if the class is defined as a complement of another class, False otherwise.

        :rtype: bool
        """

        return any(isinstance(axiom, OWLObjectComplementOf) for axiom in self.axioms)

    @property
    def subclasses(self) -> list[OWLSubClassOf]:
        """
        This property retrieves a list of `OWLSubClassOf` axioms that define this class as the superclass. It filters the internal collection of axioms associated with this entity to identify relationships where another class is explicitly stated to be a subclass of the current instance. Each returned axiom represents a direct hierarchical link, indicating that all individuals belonging to the subclass are also instances of this class. If no such axioms exist, an empty list is returned.

        :return: A list of axioms asserting this class as the superclass.

        :rtype: list[OWLSubClassOf]
        """

        return [
            axiom
            for axiom in self.axioms
            if isinstance(axiom, OWLSubClassOf)
            and axiom.super_class_expression == self.class_
        ]

    @property
    def superclasses(self) -> list[OWLSubClassOf]:
        """
        Retrieves the axioms that define the superclasses of this class by filtering the internal collection of axioms. Specifically, it returns a list of `OWLSubClassOf` axioms where the subclass expression matches the current class, thereby identifying the classes that this class is a subclass of. This property is read-only and returns a new list, meaning modifications to the returned list will not affect the object's internal state. If no matching axioms are found, an empty list is returned.

        :return: A list of OWLSubClassOf axioms asserting that this class is a subclass of another class.

        :rtype: list[OWLSubClassOf]
        """

        return [
            axiom
            for axiom in self.axioms
            if isinstance(axiom, OWLSubClassOf)
            and axiom.sub_class_expression == self.class_
        ]

    @property
    def equivalent_classes(self) -> list[OWLEquivalentClasses]:
        """
        Retrieves a list of axioms asserting that this class is equivalent to other class expressions within the ontology. This property filters the class's associated axioms to return only those of type `OWLEquivalentClasses`, which indicate that the current class and the referenced classes share exactly the same set of instances. The result is a list that may be empty if no equivalence relationships are defined for this class.

        :return: A list of axioms asserting that this class is equivalent to other class expressions.

        :rtype: list[OWLEquivalentClasses]
        """

        return [
            axiom for axiom in self.axioms if isinstance(axiom, OWLEquivalentClasses)
        ]

    @property
    def disjoint_classes(self) -> list[OWLDisjointClasses]:
        """
        This property retrieves a list of axioms that explicitly declare this class to be disjoint with other classes within the ontology. It filters the class's associated axioms to return only those of type `OWLDisjointClasses`. Each axiom in the resulting list enforces the semantic constraint that the class extensions are mutually exclusive, meaning no individual can be an instance of both this class and the classes specified in the axiom.

        :return: A list of axioms asserting that this class is disjoint with other classes, meaning they have no common instances.

        :rtype: list[OWLDisjointClasses]
        """

        return [axiom for axiom in self.axioms if isinstance(axiom, OWLDisjointClasses)]

    @property
    def disjoint_union_classes(self) -> list[OWLDisjointUnion]:
        """
        Retrieves a list of `OWLDisjointUnion` axioms that define this class as a disjoint union of other classes within the ontology. This property filters the axioms associated with the class to identify those asserting that the class is equivalent to the union of a set of distinct, non-overlapping classes. If the class is not involved in any disjoint union axioms, an empty list is returned. The operation is read-only and does not modify the underlying ontology structure.

        :return: A list of `OWLDisjointUnion` axioms associated with this class.

        :rtype: list[OWLDisjointUnion]
        """

        return [axiom for axiom in self.axioms if isinstance(axiom, OWLDisjointUnion)]

    @property
    def all_axioms(self) -> list[OWLObjectAllValuesFrom]:
        """
        Retrieves a filtered list of axioms representing universal restrictions (specifically `OWLObjectAllValuesFrom`) that are associated with this class. This property iterates through the general collection of axioms and selects only those that define constraints requiring all values of a given object property to belong to a specified filler class. The operation is read-only and returns an empty list if no such axioms are present.

        :return: A list of universal restriction axioms (OWLObjectAllValuesFrom) associated with this class, indicating that all values of a specific property for instances of this class must belong to a specified class.

        :rtype: list[OWLObjectAllValuesFrom]
        """

        return [
            axiom for axiom in self.axioms if isinstance(axiom, OWLObjectAllValuesFrom)
        ]

    @property
    def some_axioms(self) -> list[OWLObjectSomeValuesFrom]:
        """
        Filters the class's collection of axioms to return only those representing existential restrictions, specifically instances of `OWLObjectSomeValuesFrom`. Each returned axiom indicates that some instances of this class are required to participate in a specific object property relationship. This property is read-only and returns a new list instance; if no such restrictions are defined within the class's axioms, an empty list is returned.

        :return: A list of existential restriction axioms (ObjectSomeValuesFrom) associated with this class, indicating properties that some instances of the class must satisfy.

        :rtype: list[OWLObjectSomeValuesFrom]
        """

        return [
            axiom for axiom in self.axioms if isinstance(axiom, OWLObjectSomeValuesFrom)
        ]

    @property
    def has_key_axioms(self) -> list[OWLHasKey]:
        """
        Retrieves a collection of axioms that define unique identifiers for instances of this class. Each returned axiom specifies a set of properties that, when combined, distinguish individual instances of the class within the ontology. This property filters the general list of axioms associated with the class to isolate those of type `OWLHasKey`, returning an empty list if no such constraints are defined. The operation is read-only and does not alter the internal state of the object.

        :return: A list of OWLHasKey axioms associated with this class, specifying the properties that uniquely identify its instances.

        :rtype: list[OWLHasKey]
        """

        return [axiom for axiom in self.axioms if isinstance(axiom, OWLHasKey)]

    @property
    def min_axioms(self) -> list[OWLObjectMinCardinality]:
        """
        This property retrieves a collection of minimum cardinality restrictions defined for the current OWL class by filtering the class's complete set of axioms. It specifically isolates instances of `OWLObjectMinCardinality`, which assert that members of this class must participate in at least a specified number of relationships via a particular object property. The method returns a new list containing these specific axioms; if no minimum cardinality restrictions are present, an empty list is returned. Because this is a computed property, it has no side effects on the object's state, and the returned list is a distinct copy from the internal storage.

        :return: A list of minimum cardinality axioms involving this class.

        :rtype: list[OWLObjectMinCardinality]
        """

        return [
            axiom for axiom in self.axioms if isinstance(axiom, OWLObjectMinCardinality)
        ]

    @property
    def max_axioms(self) -> list[OWLObjectMaxCardinality]:
        """
        This property retrieves a list of `OWLObjectMaxCardinality` axioms associated with the current `OWLFullClass`. It filters the class's general collection of axioms to isolate those that define maximum cardinality restrictions, which specify the upper limit on the number of object property relationships an instance of this class may possess. The operation does not modify the internal state of the class and returns a new list; if no matching axioms are found, an empty list is returned.

        :return: A list of axioms defining the maximum cardinality restrictions applicable to this class.

        :rtype: list[OWLObjectMaxCardinality]
        """

        return [
            axiom for axiom in self.axioms if isinstance(axiom, OWLObjectMaxCardinality)
        ]

    @property
    def exact_axioms(self) -> list[OWLObjectExactCardinality]:
        """
        Retrieves a filtered list of axioms that impose exact cardinality restrictions on the class. This property iterates through the class's associated axioms and selects only those that are instances of `OWLObjectExactCardinality`, which define constraints requiring instances of the class to have a specific, precise number of relationships via a given object property. The operation returns a new list, ensuring that modifications to the result do not affect the internal state of the class, and yields an empty list if no matching restrictions are found.

        :return: A list of exact cardinality axioms involving this class.

        :rtype: list[OWLObjectExactCardinality]
        """

        return [
            axiom
            for axiom in self.axioms
            if isinstance(axiom, OWLObjectExactCardinality)
        ]

    def add_assertion(
        self,
        individual: OWLIndividual,
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Creates and stores a class assertion axiom stating that the specified individual is an instance of the class represented by this object. The method accepts an optional list of annotations to attach metadata to the assertion. It ensures idempotency by checking the existing axioms; if an identical assertion is already present, the method returns without making changes. Otherwise, the new assertion is appended to the internal list of axioms.

        :param individual: The entity to be asserted as an instance of the class represented by this object.
        :type individual: OWLIndividual
        :param annotations: Optional list of annotation objects to attach to the class assertion, providing additional metadata or context.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        assertion = OWLClassAssertion(self.class_, individual, annotations)
        if assertion in self.axioms:
            return
        self.axioms.append(assertion)

    def is_subclass_of(
        self,
        super_class: typing.Union[OWLClassExpression, typing.Self],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Asserts a subclass relationship between the current class and the specified `super_class` by adding a corresponding axiom to the internal collection. The method accepts either a raw `OWLClassExpression` or another `OWLFullClass` instance, extracting the underlying class expression as needed. Optional annotations can be provided to attach metadata to the relationship. This operation modifies the state of the object by appending the new axiom, but it is idempotent; if the specific subclass relationship already exists within the axioms, the method returns without making changes to prevent duplicates.

        :param super_class: The class expression or class instance representing the superclass to which this class is asserted as a subclass.
        :type super_class: typing.Union[OWLClassExpression, typing.Self]
        :param annotations:
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        element = OWLSubClassOf(
            self.class_,
            (
                super_class
                if isinstance(super_class, OWLClassExpression)
                else super_class.class_
            ),
            annotations,
        )
        if element in self.axioms:
            return
        self.axioms.append(element)

    def is_superclass_of(
        self,
        sub_class: typing.Union[OWLClassExpression, typing.Self],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Asserts that the current class is a superclass of the specified subclass by creating and registering a corresponding `OWLSubClassOf` axiom. The subclass argument can be either a direct class expression or another `OWLFullClass` instance, from which the underlying class expression is extracted. If the specific relationship is already present in the object's axioms, the operation is skipped to prevent duplication. Optional annotations may be provided to attach metadata, such as provenance or confidence, to the relationship.

        :param sub_class: The class expression or class instance to be asserted as a subclass of the current class.
        :type sub_class: typing.Union[OWLClassExpression, typing.Self]
        :param annotations: Optional list of annotations to attach to the subclass axiom, providing additional metadata or context for the relationship.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        element = OWLSubClassOf(
            (
                sub_class
                if isinstance(sub_class, OWLClassExpression)
                else sub_class.class_
            ),
            self.class_,
            annotations,
        )
        if element in self.axioms:
            return
        self.axioms.append(element)

    def _get_classes(
        self,
        classes: typing.Union[
            OWLClassExpression, list[OWLClassExpression], typing.Self, list[typing.Self]
        ],
    ) -> list[OWLClassExpression]:
        """
        Normalizes input class representations into a standardized list of OWLClassExpression objects. The method accepts either a single instance or a list of instances, supporting both OWLClassExpression objects and the current class type (OWLFullClass). When an OWLFullClass is encountered, its underlying class expression is extracted via the `class_` attribute. The input list must be homogeneous; mixing types or providing invalid arguments results in a TypeError. This function performs no side effects on the instance state.

        :param classes: The class or classes to be converted into a list of `OWLClassExpression` objects. Can be a single instance or a list of `OWLClassExpression` or `OWLFullClass` instances.
        :type classes: typing.Union[OWLClassExpression, list[OWLClassExpression], typing.Self, list[typing.Self]]

        :raises TypeError: Raised if the `classes` argument is not an `OWLClassExpression`, an `OWLFullClass`, or a list exclusively containing one of these types.

        :return: A list of OWLClassExpression objects normalized from the input, handling single items, lists, and unwrapping OWLFullClass instances.

        :rtype: list[OWLClassExpression]
        """

        new_classes: list[OWLClassExpression] = []
        if isinstance(classes, list):
            if all(isinstance(c, OWLClassExpression) for c in classes):
                new_classes.extend(classes)
            elif all(isinstance(c, OWLFullClass) for c in classes):
                new_classes.extend([c.class_ for c in classes])
            else:
                raise TypeError(
                    "Input must be an OWLClassExpression, OWLFullClass, or a list of these."
                )
        else:
            if isinstance(classes, OWLClassExpression):
                new_classes.append(classes)
            elif isinstance(classes, OWLFullClass):
                new_classes.append(classes.class_)
            else:
                raise TypeError(
                    "Input must be an OWLClassExpression, OWLFullClass, or a list of these."
                )
        return new_classes

    def is_equivalent_to(
        self,
        classes: typing.Union[
            OWLClassExpression, list[OWLClassExpression], typing.Self, list[typing.Self]
        ],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Asserts that the current class is equivalent to the specified class or classes by adding an equivalence axiom to the ontology. If multiple classes are provided, the method asserts that the current class is equivalent to the intersection of those classes. Optional annotations can be included to attach metadata to the axiom. The method ensures idempotency by checking the existing axioms; if the specific equivalence axiom is already present, it is not added again.

        :param classes: The class expression(s) to which the current class is asserted as equivalent. If a list is provided, the current class is asserted as equivalent to the intersection of the specified classes.
        :type classes: typing.Union[OWLClassExpression, list[OWLClassExpression], typing.Self, list[typing.Self]]
        :param annotations: Optional list of annotations to include with the equivalence axiom, providing additional metadata or context.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        element = OWLEquivalentClasses(
            [self.class_] + self._get_classes(classes), annotations
        )
        if element in self.axioms:
            return
        self.axioms.append(element)

    def is_disjoint_from(
        self,
        classes: typing.Union[
            OWLClassExpression, list[OWLClassExpression], typing.Self, list[typing.Self]
        ],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        Asserts that the current class is disjoint from the specified class or classes, meaning they share no common instances. This method constructs a disjointness axiom using the current class and the provided class expressions, which can be supplied as individual objects or lists. If the generated axiom already exists within the internal collection of axioms, it is not added again, ensuring idempotency. Optionally, a list of annotations can be provided to attach metadata to the axiom. The primary side effect of this operation is the modification of the internal axioms list by appending the new disjointness axiom if it is unique.

        :param classes: The class or classes to be asserted as disjoint from the current class. Can be a single OWLClassExpression or OWLFullClass, or a list of such objects.
        :type classes: typing.Union[OWLClassExpression, list[OWLClassExpression], typing.Self, list[typing.Self]]
        :param annotations: Optional list of annotations to include with the disjointness axiom, providing additional metadata or context.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        element = OWLDisjointClasses(
            [self.class_] + self._get_classes(classes), annotations
        )
        if element in self.axioms:
            return
        self.axioms.append(element)

    def is_disjoint_union_from(
        self,
        classes: typing.Union[
            OWLClassExpression, list[OWLClassExpression], typing.Self, list[typing.Self]
        ],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        This method asserts that the current class is a disjoint union of the specified class expressions, meaning the class is exactly equivalent to the union of the provided classes while ensuring those classes are mutually exclusive (pairwise disjoint). It accepts a single class expression or a list of expressions, and optionally associates a list of annotations with the axiom to provide metadata. The method constructs the corresponding `OWLDisjointUnion` axiom and appends it to the internal list of axioms, but only if an identical axiom does not already exist, thereby preventing redundancy.

        :param classes: The class expressions or class instances that constitute the disjoint union, representing the mutually exclusive and exhaustive components of the current class.
        :type classes: typing.Union[OWLClassExpression, list[OWLClassExpression], typing.Self, list[typing.Self]]
        :param annotations: An optional list of annotations to attach to the disjoint union axiom, providing additional metadata or context.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        element = OWLDisjointUnion(self.class_, self._get_classes(classes), annotations)
        if element in self.axioms:
            return
        self.axioms.append(element)

    def is_intersection_of(
        self,
        classes: typing.Union[
            OWLClassExpression, list[OWLClassExpression], typing.Self, list[typing.Self]
        ],
    ) -> None:
        """
        This method asserts that the current class is equivalent to the intersection of the provided class expressions. It accepts a single class expression or a list of expressions, which can be standard OWL class expressions or other `OWLFullClass` instances, to define the necessary and sufficient conditions for class membership. The method constructs an intersection axiom representing this relationship and adds it to the class's list of axioms. To ensure data integrity and avoid redundancy, it checks if the specific intersection axiom already exists; if it is present, the method performs no action, otherwise, it appends the new axiom to the internal collection.

        :param classes: One or more class expressions to be combined with the current class to form an intersection.
        :type classes: typing.Union[OWLClassExpression, list[OWLClassExpression], typing.Self, list[typing.Self]]
        """

        intersection = OWLObjectIntersectionOf(
            [self.class_] + self._get_classes(classes)
        )
        if intersection in self.axioms:
            return
        self.axioms.append(intersection)

    def is_union_of(
        self,
        classes: typing.Union[
            OWLClassExpression, list[OWLClassExpression], typing.Self, list[typing.Self]
        ],
    ) -> None:
        """
        Asserts that the current class is equivalent to the union of the provided class expressions. The method accepts a single class or a list of classes, constructing an `OWLObjectUnionOf` instance that represents this relationship. It checks for existing axioms to prevent duplication; if the specific union expression is already present, the method takes no action. Otherwise, the new union expression is appended to the internal list of axioms, effectively defining the class as the union of the specified components.

        :param classes: The class or classes that form the union with the current class. Can be a single class expression or a list of class expressions.
        :type classes: typing.Union[OWLClassExpression, list[OWLClassExpression], typing.Self, list[typing.Self]]
        """

        union = OWLObjectUnionOf([self.class_] + self._get_classes(classes))
        if union in self.axioms:
            return
        self.axioms.append(union)

    def to_complement(self) -> None:
        """Creates a representation of the logical complement of the current class and adds it to the internal list of axioms. The method verifies that this specific complement axiom is not already present in the collection to avoid redundancy. This process modifies the object's internal state and does not return a value."""

        complement = OWLObjectComplementOf(self.class_)
        if complement in self.axioms:
            return
        self.axioms.append(complement)

    def all_values(
        self,
        object: OWLObjectPropertyExpression,
    ) -> None:
        """
        Constructs an OWL restriction asserting that all values associated with the provided object property must be instances of the current class. This method creates an `OWLObjectAllValuesFrom` element, which defines the current class as the universal range for the given property, and adds it to the internal collection of axioms. The operation is idempotent; if the specific restriction is already present in the axioms list, it will not be added again.

        :param object: The object property expression defining the relationship for which the universal restriction applies.
        :type object: OWLObjectPropertyExpression
        """

        element = OWLObjectAllValuesFrom(object, self.class_)
        if element in self.axioms:
            return
        self.axioms.append(element)

    def some_values(
        self,
        object: OWLObjectPropertyExpression,
    ) -> None:
        """
        Adds an existential restriction to the class's axioms, asserting that instances of the class must have at least one value for the specified object property. The restriction is constructed using the provided property and the class itself, implying a relationship where the value is an instance of the current class. This method ensures idempotency by verifying that the restriction does not already exist in the axioms list before adding it; if it is found, the method returns without changes. Otherwise, the new restriction is appended to the axioms.

        :param object: The object property expression used to assert that the class has some values from this property.
        :type object: OWLObjectPropertyExpression
        """

        element = OWLObjectSomeValuesFrom(object, self.class_)
        if element in self.axioms:
            return
        self.axioms.append(element)

    def has_key(
        self,
        object_properties: list[OWLObjectPropertyExpression],
        data_properties: list[OWLDataPropertyExpression],
        annotations: typing.Optional[list[OWLAnnotation]] = None,
    ) -> None:
        """
        This method defines a key for the current OWL class by asserting that a specific combination of object and data properties uniquely identifies instances of the class. It constructs an OWLHasKey axiom using the provided property lists and optional annotations, appending it to the class's internal collection of axioms. The operation is idempotent; if an identical axiom already exists within the axioms, the method returns without modification to avoid duplicates.

        :param object_properties: Object properties that constitute part of the key, uniquely identifying instances of this class based on relationships to other individuals.
        :type object_properties: list[OWLObjectPropertyExpression]
        :param data_properties: A list of data properties that uniquely identify instances of this class based on their associated literal values.
        :type data_properties: list[OWLDataPropertyExpression]
        :param annotations: Optional metadata to attach to the axiom, providing additional context such as source or confidence.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        element = OWLHasKey(
            self.class_, object_properties, data_properties, annotations
        )
        if element in self.axioms:
            return
        self.axioms.append(element)

    def min_cardinality(
        self, cardinality: int, object_property: OWLObjectPropertyExpression
    ) -> None:
        """
        Asserts a minimum cardinality restriction on the current class for a specified object property, requiring that instances of the class have at least the defined number of relationships via that property. This method constructs the corresponding axiom and appends it to the internal collection of axioms, but only if an identical axiom does not already exist, thereby preventing redundancy. The operation modifies the state of the class by updating its axioms list but does not return a value.

        :param cardinality: The minimum number of relationships instances of the class must have via the specified object property.
        :type cardinality: int
        :param object_property: The object property expression to which the minimum cardinality restriction applies.
        :type object_property: OWLObjectPropertyExpression
        """

        curr = OWLObjectMinCardinality(cardinality, object_property, self.class_)
        if curr in self.axioms:
            return
        self.axioms.append(curr)

    def max_cardinality(
        self, cardinality: int, object_property: OWLObjectPropertyExpression
    ) -> None:
        """
        Asserts a maximum cardinality restriction on the current class, indicating that any instance of this class can participate in at most the specified number of relationships defined by the given object property. This method creates an `OWLObjectMaxCardinality` axiom and adds it to the internal collection of axioms associated with the class. It ensures idempotency by verifying that an identical axiom does not already exist before performing the addition, thereby preventing duplicate entries.

        :param cardinality: The maximum number of distinct individuals that instances of this class can be related to via the specified object property.
        :type cardinality: int
        :param object_property: The object property expression representing the relationship to which the maximum cardinality restriction applies.
        :type object_property: OWLObjectPropertyExpression
        """

        curr = OWLObjectMaxCardinality(cardinality, object_property, self.class_)
        if curr in self.axioms:
            return
        self.axioms.append(curr)

    def exact_cardinality(
        self, cardinality: int, object_property: OWLObjectPropertyExpression
    ) -> None:
        """
        Adds an exact cardinality restriction to the class, asserting that instances must have exactly the specified number of relationships via the given object property. The method creates an `OWLObjectExactCardinality` axiom and appends it to the internal list of axioms, checking first to ensure that an identical axiom is not already present. This prevents duplicate constraints and enforces a specific count of object property assertions for any individual classified under this class.

        :param cardinality: The exact number of relationships that instances of the class must have via the specified object property.
        :type cardinality: int
        :param object_property: The object property expression to which the exact cardinality restriction applies.
        :type object_property: OWLObjectPropertyExpression
        """

        curr = OWLObjectExactCardinality(cardinality, object_property, self.class_)
        if curr in self.axioms:
            return
        self.axioms.append(curr)
