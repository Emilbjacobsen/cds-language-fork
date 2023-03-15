import spacy

nlp = spacy.load("en_core_web_md")

def main():
    text = "this is a string"
    doc = nlp(text)

    for token in doc:
        print(token.text)

if __name__=="__main__":
    main()