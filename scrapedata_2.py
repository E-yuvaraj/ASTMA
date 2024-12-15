from bs4 import BeautifulSoup
import pandas as pd
from textblob import TextBlob
def scrape_twitter_posts(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print("File not found")
        return None
    soup = BeautifulSoup(content, 'html.parser')
    posts = []
    for tweet in soup.find_all('p', class_='tweet'):
        tweet_content = tweet.get_text()  
        posts.append(tweet_content)
    return posts
file_path = "D:/Program Files/python/ASTMA/scrapehtml.html"  
posts = scrape_twitter_posts(file_path)
if posts:
    df = pd.DataFrame(posts, columns=['Post'])
    def analyze_sentiment(comment):
        analysis = TextBlob(comment)
        return analysis.sentiment.polarity, analysis.sentiment.subjectivity
    df['Polarity'] = df['Post'].apply(lambda x: analyze_sentiment(x)[0])
    df['Subjectivity'] = df['Post'].apply(lambda x: analyze_sentiment(x)[1])
    df['Sentiment'] = df['Polarity'].apply(lambda x: 'Positive' if x > 0 else 'Negative' if x < 0 else 'Neutral')
    print(df)
else:
    print("No posts retrieved.")
