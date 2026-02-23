![Docs](https://img.shields.io/badge/docs-passing-brightgreen.svg)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)
[![Documentation](https://img.shields.io/badge/Read%20the%20Docs-8CA1AF?logo=readthedocs&logoColor=white)](https://pyowl2.readthedocs.io/en/latest)
[![PyPI](https://img.shields.io/pypi/v/pyowl2.svg)](https://pypi.org/project/pyowl2/)
![Python Versions](https://img.shields.io/pypi/pyversions/pyowl2.svg)
![Code Style](https://img.shields.io/badge/code%20style-python-green)


# PyOWL2
A python implementation of the OWL 2 standard. See [OWL 2 Syntax](https://www.w3.org/TR/owl2-syntax/) and [OWL 2 Mapping to RDF](https://www.w3.org/TR/owl2-mapping-to-rdf/).

---

PyOWL2

A lightweight Python implementation of OWL 2 constructs, designed for mapping and interacting with OWL 2 ontology elements such as Class, ObjectProperty, Datatype, AnnotationProperty, and more.

Features:
- Object-oriented representation of OWL 2 elements
- Getter access for ontology elements
- Clean, extensible Python API
- Ideal for RDF/OWL-based modeling and semantic reasoning tools

---

# Installation
```python
pip install pyowl2
```

---

Examples of supported OWL 2 Constructs

| OWL Construct      | Python Class      |
|--------------------|-------------------|
| owl:Class          | OWLClass          |
| owl:Datatype       | OWLDatatype       |
| owl:ObjectProperty | OWLObjectProperty |

---

# Basic Usage

```python
from rdfxml import Namespace, URIRef, XSD
from pyowl2 import (
    IRI,
    OWLOntology,
    OWLDeclaration,
    OWLClass,
    OWLObjectProperty,
    OWLDatatype,
    OWLObjectPropertyDomain,
    OWLObjectPropertyRange,
    OWLEquivalentClasses
)

# Define the namespace
reference = URIRef("https://example.org#")
namespace = Namespace(reference)

# Define the ontology
ontology = OWLOntology(reference)

# Define a class
person = OWLClass(IRI(namespace, "Person"))

# Define an object property
has_spouse = OWLObjectProperty(IRI(namespace, "hasSpouse")

# Define a datatype
birthdate = OWLDatatype(IRI(namespace, "birthDate"))

## Save axioms in the ontology
ontology.add_axioms([
    OWLDeclaration(person),
    OWLDeclaration(has_spouse),
    OWLObjectPropertyDomain(has_spouse, person),
    OWLObjectPropertyRange(has_spouse, person),
    OWLEquivalentClasses(birtdate, OWLDatatype(XSD.date)),
])
ontology.save(OUTPUT_PATH)
```

## Access to the ontology elements

```python
from rdfxml import Namespace, URIRef
from pyowl2 import OWLOntology, AxiomsType

reference = URIRef("https://example.org#")
namespace = Namespace(reference)
ontology = OWLOntology(reference, PATH_TO_ONTOLOGY)

# print the list of all classes in the ontology
print(ontology.get_axioms(AxiomsType.CLASSES))
```

---

# Advanced usage

```python
from rdfxml import Namespace, URIRef, XSD
from pyowl2 import (
    IRI,
    OWLOntology,
    OWLFullClass,
    OWLFullObjectProperty,
    OWLFullDataRange
)

# Define the namespace
reference = URIRef("https://example.org#")
namespace = Namespace(reference)

# Define the ontology
ontology = OWLOntology(reference)

# Define a class
person = OWLFullClass(IRI(namespace, "Person"))

# Define an object property
has_spouse = OWLFullObjectProperty(
    IRI(namespace, "hasSpouse"),
    range=person.class_,
    domain=person.class_
)

# Define a datatype
birthdate = OWLFullDataRange(IRI(namespace, "birthDate"))
birthdate.is_equivalent_to([OWLDatatype(XSD.date)])

# Save axioms in the ontology
ontology.add_axioms([
    person,
    has_spouse,
    birtdate,
])
ontology.save(OUTPUT_PATH)
```

---

# Project Structure

```text
pyowl
├── __init__.py
├── abstracts
│   ├── __init__.py
│   ├── annotation_axiom.py
│   ├── annotation_subject.py
│   ├── annotation_value.py
│   ├── assertion.py
│   ├── axiom.py
│   ├── class_axiom.py
│   ├── class_expression.py
│   ├── data_property_axiom.py
│   ├── data_property_expression.py
│   ├── data_range.py
│   ├── entity.py
│   ├── individual.py
│   ├── object_property_axiom.py
│   ├── object_property_expression.py
│   ├── object.py
│   └── property_range.py
├── axioms
│   ├── __init__.py
│   ├── annotations
│   │   ├── __init__.py
│   │   ├── annotation_assertion.py
│   │   ├── annotation_property_domain.py
│   │   ├── annotation_property_range.py
│   │   └── sub_annotation_property_of.py
│   ├── assertion
│   │   ├── __init__.py
│   │   ├── class_assertion.py
│   │   ├── data_property_assertion.py
│   │   ├── different_individuals.py
│   │   ├── negative_data_property_assertion.py
│   │   ├── negative_object_property_assertion.py
│   │   ├── object_property_assertion.py
│   │   └── same_individual.py
│   ├── class_axiom
│   │   ├── __init__.py
│   │   ├── disjoint_classes.py
│   │   ├── disjoint_union.py
│   │   ├── equivalent_classes.py
│   │   └── sub_class_of.py
│   ├── data_property_axiom
│   │   ├── __init__.py
│   │   ├── data_property_domain.py
│   │   ├── data_property_range.py
│   │   ├── disjoint_data_properties.py
│   │   ├── equivalent_data_properties.py
│   │   ├── functional_data_property.py
│   │   └── sub_data_property_of.py
│   ├── datatype_definition.py
│   ├── declaration.py
│   ├── general.py
│   ├── has_key.py
│   └── object_property_axiom
│       ├── __init__.py
│       ├── asymmetric_object_property.py
│       ├── disjoint_object_properties.py
│       ├── equivalent_object_properties.py
│       ├── functional_object_property.py
│       ├── inverse_functional_object_property.py
│       ├── inverse_object_properties.py
│       ├── irreflexive_object_property.py
│       ├── object_property_chain.py
│       ├── object_property_domain.py
│       ├── object_property_range.py
│       ├── reflexive_object_property.py
│       ├── sub_object_property_of.py
│       ├── symmetric_object_property.py
│       └── transitive_object_property.py
├── base
│   ├── __init__.py
│   ├── annotation_property.py
│   ├── annotation.py
│   ├── datatype.py
│   ├── iri.py
│   └── owl_class.py
├── class_expression
│   ├── __init__.py
│   ├── data_all_values_from.py
│   ├── data_exact_cardinality.py
│   ├── data_has_value.py
│   ├── data_max_cardinality.py
│   ├── data_min_cardinality.py
│   ├── data_some_values_from.py
│   ├── object_all_values_from.py
│   ├── object_complement_of.py
│   ├── object_exact_cardinality.py
│   ├── object_has_self.py
│   ├── object_has_value.py
│   ├── object_intersection_of.py
│   ├── object_max_cardinality.py
│   ├── object_min_cardinality.py
│   ├── object_one_of.py
│   ├── object_some_values_from.py
│   └── object_union_of.py
├── data_range
│   ├── __init__.py
│   ├── data_complement_of.py
│   ├── data_intersection_of.py
│   ├── data_one_of.py
│   ├── data_union_of.py
│   └── datatype_restriction.py
├── expressions
│   ├── __init__.py
│   ├── data_property.py
│   ├── inverse_object_property.py
│   └── object_property.py
├── getter
│   ├── __init__.py
│   ├── rdf_xml_clear.py
│   └── rdf_xml_getter.py
├── individual
│   ├── __init__.py
│   ├── anonymous_individual.py
│   └── named_individual.py
├── literal
│   ├── __init__.py
│   └── literal.py
├── mapper
│   ├── __init__.py
│   └── rdf_xml_mapper.py
├── ontology.py
├── setup.cfg
├── setup.py
└── utils
    ├── __init__.py
    ├── datatype.py
    ├── individual.py
    ├── object_property.py
    ├── thing.py
    └── utils.py
```

---

# License

This project is licensed under the Creative Commons Attribution-ShareAlike 4.0 International.
