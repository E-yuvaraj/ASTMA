import nltk
from textblob import TextBlob

data = [
 "I love this video! Great content.",
 "This is terrible, I hate it.",
 "Just okay, nothing special.",
 "Amazing work, keep it up!",
 "Not my cup of tea, but well made."
]

def SA(data):
    analysis = TextBlob(data)
    senti = analysis.sentiment
    return senti.polarity, senti.subjectivity

for i in data:
    polarity, subjectivity = SA(i)
    senti = 'Positive' if polarity > 0 else 'Negative' if polarity < 0 else 'Neutral'
    print(f"Comment: {i}")
    print(senti, polarity, subjectivity)
    print()
    