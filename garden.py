import spacy

nlp = spacy.load('en_core_web_sm')

gardenpathSentences = [
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi.",
    "The complex houses married and single soldiers and their families.",
    "The man whistling tunes pianos.",
    "The horse raced past the barn fell.",
]

for sentence in gardenpathSentences:
    doc = nlp(sentence)
    for token in doc:
        if token.ent_type_ and token.ent_type_ != "":  # To Check if it's an entity
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


