

import spacy


def tag_sentence(sentence):
    # Load the English model
    nlp = spacy.load('en_core_web_sm')

    # Create a Doc object
    doc = nlp(sentence)

    # Apply transformation-based tagging
    tagged_words = [(token.text, token.pos_) for token in doc]

    return tagged_words

english_words = set(word.strip() for word in open('words_alpha.txt'))

# Step 2: Load the text that needs to be tagged
text = "The quick brown fox jumps over 25 lazy dogs. There are 567,899 cars on the road."

# Step 3: Split the text into words
words = text.lower().split()

# Step 4: Use the 'isalpha()' method to check if the word is an English word
tagged_words = []
for word in words:
    if word.isalpha():
        tag = 'ENGLISH' if word in english_words else 'UNKNOWN'
    elif word.replace(',', '', 1).isdigit():
        tag = 'NUMBER'
    else:
        tag = 'UNKNOWN'

    tagged_words.append((word, tag))

print(f"Transformation Based Tagging : \n {tagged_words} \n")
