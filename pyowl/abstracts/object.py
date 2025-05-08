import abc


class OWLObject(abc.ABC, metaclass=abc.ABCMeta):
    """
    Abstract class for OWL objects.
    """
    __slots__ = ()

    def __init__(self):
        """
        Initialize the OWLObject.
        """
        pass
