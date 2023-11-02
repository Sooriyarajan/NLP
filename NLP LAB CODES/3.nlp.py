import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Sample text for morphological analysis
text = "Studying morphological analysis using NLTK is interesting."

# Tokenize the text into words
words = word_tokenize(text)

# Perform stemming using different stemmers
porter = PorterStemmer()
lancaster = LancasterStemmer()
snowball = SnowballStemmer('english')

stemmed_words_porter = [porter.stem(word) for word in words]
stemmed_words_lancaster = [lancaster.stem(word) for word in words]
stemmed_words_snowball = [snowball.stem(word) for word in words]

# Perform lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word, wordnet.VERB) for word in words]

# Part-of-speech tagging
pos_tags = nltk.pos_tag(words)

# Display the results
print("Original Words:", words)
print("Porter Stemming:", stemmed_words_porter)
print("Lancaster Stemming:", stemmed_words_lancaster)
print("Snowball Stemming:", stemmed_words_snowball)
print("Lemmatization:", lemmatized_words)
print("Part-of-Speech Tags:", pos_tags)
