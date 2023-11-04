import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
text = "The quick brown fox jumps over the lazy dog"
words = word_tokenize(text)
pos_tags = pos_tag(words)
for word, pos_tag in pos_tags:
    print(f"{word}: {pos_tag}")
