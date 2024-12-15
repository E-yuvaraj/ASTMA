import re
from googleapiclient.discovery import build
import nltk
from textblob import TextBlob

apikey = 'AIzaSyA82uQ04ZyxzsS1S7nZqIuvFuZCfERwabI'
youtube = build('youtube', 'v3', developerKey=apikey)

def fetch_comments(video_id, max_results=5):
    comments = []
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=max_results
    )
    response = request.execute()
    for item in response.get('items', []):
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        clean_comment = re.sub(r'[^\x00-\x7F]+', '', comment)
        comments.append(clean_comment)
    return comments

video_id = "SWZyuEQPQYo"
comments = fetch_comments(video_id)
for idx, comment in enumerate(comments, start=1):
    print(f"{idx}. {comment}")

def SA(comments):
    analysis = TextBlob(comments)
    senti = analysis.sentiment
    return senti.polarity, senti.subjectivity

for i in comments:
    polarity, subjectivity = SA(i)
    senti = 'Positive' if polarity > 0 else 'Negative' if polarity < 0 else 'Neutral'
    print(f"Comment: {i}")
    print(senti, polarity, subjectivity)
    print()