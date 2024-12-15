import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from collections import Counter

# Step 1: Define the hashtags and generate synthetic data
hashtags = ['#AI', '#DataScience', '#MachineLearning', '#Python', '#BigData', 
            '#IoT', '#Blockchain', '#Cloud', '#CyberSecurity', '#VR']

def generate_hashtag_data(n_posts=10000):
    np.random.seed(42)
    data = {
        'post_id': range(1, n_posts + 1),
        'text': [f"Post with {' '.join(np.random.choice(hashtags, np.random.randint(1, 4), replace=False))}" 
                 for _ in range(n_posts)],
        'timestamp': pd.date_range(start='2024-01-01', periods=n_posts, freq='5T')
    }
    return pd.DataFrame(data)

def extract_hashtags(text):
    return [tag.lower() for tag in text.split() if tag.startswith('#')]

# Step 2: Analyze hashtag trends
def analyze_hashtag_trends(df):
    df['hashtags'] = df['text'].apply(extract_hashtags)
    df.set_index('timestamp', inplace=True)

    # Time-based analysis: count the occurrence of each hashtag per day
    daily_hashtag_counts = df.resample('D')['hashtags'].sum().apply(Counter)

    # Initialize trend scores
    trend_scores = {hashtag.lower(): [] for hashtag in hashtags}
    
    # Collect daily counts for each hashtag
    for day, counts in daily_hashtag_counts.items():
        for hashtag in trend_scores.keys():
            trend_scores[hashtag].append(counts.get(hashtag, 0))

    # Calculate mean and std deviation for each hashtag
    trend_summary = {hashtag: {'mean': np.mean(counts), 'std': np.std(counts)} for hashtag, counts in trend_scores.items()}

    # Predict next day's count using Linear Regression
    X = np.arange(len(daily_hashtag_counts)).reshape(-1, 1)
    predictions = {}
    for hashtag in trend_scores.keys():
        y = trend_scores[hashtag]
        model = LinearRegression()
        model.fit(X, y)
        predictions[hashtag] = model.predict(np.array([[len(daily_hashtag_counts)]]))[0]
    
    # Print results
    print("Top 10 Trending Hashtags:")
    sorted_trending = sorted(trend_summary.items(), key=lambda x: (x[1]['mean'], x[1]['std']), reverse=True)
    for tag, stats in sorted_trending[:10]:
        print(f"{tag}: Mean = {stats['mean']:.2f}, Std = {stats['std']:.2f}")
    
    print("\nPredicted Counts for Top Hashtags (Next Day):")
    for tag, prediction in predictions.items():
        print(f"{tag}: {prediction:.2f}")
    
    return trend_summary, predictions

# Example usage
hashtag_data = generate_hashtag_data()
trend_summary, predictions = analyze_hashtag_trends(hashtag_data)
