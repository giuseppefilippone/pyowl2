pyowl2.literal
==============

.. only:: html

    .. figure:: /_uml/module_pyowl2_literal.png
       :alt: UML Class Diagram for pyowl2.literal
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **pyowl2.literal**

.. only:: latex

    .. raw:: latex

       \begin{landscape}

       \vspace*{\fill}

    .. figure:: /_uml/module_pyowl2_literal.pdf
       :alt: UML Class Diagram for pyowl2.literal
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **pyowl2.literal**

    .. raw:: latex

       \vspace*{\fill}

       \end{landscape}

.. py:module:: pyowl2.literal



.. ── LLM-GENERATED DESCRIPTION START ──

A structured object-oriented framework for modeling and manipulating OWL literals, including typed values and language-tagged strings, within ontology processing workflows.


Description
-----------


The software employs a polymorphic design to handle data values within an OWL ontology, distinguishing between typed data, plain strings, and language-tagged text through a central wrapper class. Specific subclasses manage distinct literal categories, such as integers or booleans with explicit type definitions versus textual content associated with natural languages, ensuring that ontology assertions maintain precise semantic meaning. To facilitate interoperability with semantic web standards, the implementation converts these high-level objects into standard RDFLib formats while providing utility methods for runtime type checking against XML Schema and OWL datatypes.


Modules
-------


* [``pyowl2.literal.literal``] — A set of Python classes that model and manipulate OWL literals, including typed values and language-tagged strings, for ontology processing.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/pyowl2/literal/literal/index

