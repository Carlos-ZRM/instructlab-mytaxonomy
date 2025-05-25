from pdfminer.high_level import extract_text
from textblob import TextBlob



text = extract_text("docs/Drug-Treatment-of-Cluster-Headache.pdf")

blob = TextBlob(text)

key_phrases = blob.noun_phrases
print(key_phrases)

#print(blob.tags)

#print(blob.sentences)

#print(blob.ngrams(n=10))
