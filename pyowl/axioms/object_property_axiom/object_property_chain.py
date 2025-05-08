from pyowl.abstracts.object_property_expression import OWLObjectPropertyExpression


class OWLObjectPropertyChain:
    """
    A sequence of object property expressions used in property chain axioms.
    """

    def __init__(self, expressions: list[OWLObjectPropertyExpression]) -> None:
        assert len(expressions) >= 2
        self._chain: list[OWLObjectPropertyExpression] = sorted(expressions)

    @property
    def chain(self) -> list[OWLObjectPropertyExpression]:
        return self._chain

    @chain.setter
    def chain(self, value: list[OWLObjectPropertyExpression]) -> None:
        self._chain = sorted(value)

    def __eq__(self, value: object) -> bool:
        return str(self) == str(value)

    def __ne__(self, value: object) -> bool:
        return str(self) != str(value)

    def __lt__(self, value: object) -> bool:
        return str(self) < str(value)

    def __le__(self, value: object) -> bool:
        return str(self) <= str(value)

    def __gt__(self, value: object) -> bool:
        return str(self) > str(value)

    def __ge__(self, value: object) -> bool:
        return str(self) >= str(value)

    def __hash__(self) -> int:
        return hash(str(self))

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f"ObjectPropertyChain({' '.join(map(str, self.chain))})"
