import spacy


nlp = spacy.load("en_core_web_sm")


def analyze(text):
    doc = nlp(text)
    result = {
        'nouns' : [chunk.text for chunk in doc.noun_chunks],
        'verbs': [token.lemma_ for token in doc if token.pos_ == "VERB"], 
        "text":text
    }

    return result

