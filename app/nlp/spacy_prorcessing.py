import spacy

nlp = spacy.load("en_core_web_sm")

def session__message_analyze(text: str):
    doc = nlp(text)
    
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return {"entities": entities}