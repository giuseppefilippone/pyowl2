# PyOWL2
A python implementation of the OWL 2 standard. See [owl2-syntax](https://www.w3.org/TR/owl2-syntax/) and [owl2-to-rdf](https://www.w3.org/TR/owl2-mapping-to-rdf/).

A lightweight Python implementation of OWL 2 constructs, designed for mapping and interacting with OWL 2 ontology elements such as Class, ObjectProperty, Datatype, AnnotationProperty, and more.

Features:
- Object-oriented representation of OWL 2 elements
- Getter access for ontology elements
- Clean, extensible Python API
- Ideal for RDF/OWL-based modeling and semantic reasoning tools

## Installation
Check the [repository](https://github.com/giuseppefilippone/pyowl2/). The package is available on PyPI, so you can install it using pip: `pip install pyowl2`.

Examples of supported OWL 2 Constructs

| OWL Construct      | Python Class      |
|--------------------|-------------------|
| owl:Class          | OWLClass          |
| owl:Datatype       | OWLDatatype       |
| owl:ObjectProperty | OWLObjectProperty |

## Project Structure

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

## License

This project is licensed under the Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0).
