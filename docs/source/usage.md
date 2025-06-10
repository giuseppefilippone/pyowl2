# Usage

## Basic Usage
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

### Access to the ontology elements

```python
from rdfxml import Namespace, URIRef
from pyowl2 import OWLOntology, AxiomsType

reference = URIRef("https://example.org#")
namespace = Namespace(reference)
ontology = OWLOntology(reference, PATH_TO_ONTOLOGY)

# print the list of all classes in the ontology
print(ontology.get_axioms(AxiomsType.CLASSES))
```

## Advanced usage

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