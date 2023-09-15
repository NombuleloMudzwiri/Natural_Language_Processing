import spacy

# Load the English language model
nlp = spacy.load('en_core_web_sm')

# Process a text
doc = nlp("This is a test sentence")
print([(w.text, w.pos_) for w in doc])
