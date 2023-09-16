# NLP Entity Recognition Task

This repository contains Python code that demonstrates Named Entity Recognition (NER) using the spaCy library. NER is a natural language processing (NLP) technique that identifies entities such as names of people, places, organizations, and more in text data. In this example, we use spaCy to process a set of sentences and extract information about the recognized entities.

## Code Overview

### GARDEN.PY TASK
- File: `code1.py`

```python
import spacy

# Load the English language model
nlp = spacy.load('en_core_web_sm')

# Define a list of sentences to analyze
gardenpathSentences = [
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi.",
    "The complex houses married and single soldiers and their families.",
    "The man whistling tunes pianos.",
    "The horse raced past the barn fell.",
]

# Process each sentence and extract named entities
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    for token in doc:
        if token.ent_type_ and token.ent_type_ != "":  # Check if it's an entity
            print(token.text, token.pos_, token.dep_, token.ent_type_)
            print(spacy.explain(token.ent_type_))

# Looked-up Entity 1:
# - Entity: CARDINAL
# - Explanation: Numerals that do not fall under another type
# - Sense: The entity makes sense as it represents numbers in the sentence.

# Looked-up Entity 2:
# - Entity: GPE
# - Explanation: Countries, cities, states
# - Sense: The entity makes sense as it represents a geographical location in the sentence.
```

### Code 2
- File: `code2.py`

```python
import spacy

# Load the English language model
nlp = spacy.load('en_core_web_sm')

# Define a list of sentences to analyze
gardenpathSentences = [
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi.",
    "The complex houses married and single soldiers and their families.",
    "The man whistling tunes pianos.",
    "The horse raced past the barn fell.",
]

# Process each sentence and extract named entities
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    for token in doc:
        if token.ent_type_ and token.ent_type_ != "":  # Check if it's an entity
            print(token.text, token.pos_, token.dep_, token.ent_type_)
            print(spacy.explain(token.ent_type_))

# Looked-up Entity 1:
# - Entity: CARDINAL
# - Explanation: Numerals that do not fall under another type
# - Sense: The entity makes sense as it represents numbers in the sentence.

# Looked-up Entity 2:
# - Entity: GPE
# - Explanation: Countries, cities, states
# - Sense: The entity makes sense as it represents a geographical location in the sentence.
```

## How to Run

1. Clone this GitHub repository to your local machine.
2. Make sure you have Python and spaCy installed. You can install spaCy and the English language model with the following command:
   ```
   pip install spacy
   python -m spacy download en_core_web_sm
   ```
3. Run either `code1.py` or `code2.py` using Python to perform Named Entity Recognition on the provided sentences.

Feel free to modify the sentences in the `gardenpathSentences` list or expand the code to analyze your own text data.

Enjoy experimenting with NER using spaCy!
