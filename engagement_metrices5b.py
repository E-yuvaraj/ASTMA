import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def generate_user_data(num_users=4):
    np.random.seed(42)
    data = {
        'user_id': range(1, num_users + 1),
        'followers': np.random.randint(100, 1000000, num_users),
        'avg_likes': np.random.randint(10, 10000, num_users),
        'avg_comments': np.random.randint(1, 1000, num_users),
        'posts_per_week': np.random.randint(1, 50, num_users)
    }
    df = pd.DataFrame(data)
    df['engagement_rate'] = (df['avg_likes'] + df['avg_comments']) / df['followers'] * 100
    return df
def calculate_influence(df):
    df['influence_score'] = (
        np.log(df['followers']) * 0.5 +
        df['engagement_rate'] * 0.3 +
        np.log(df['posts_per_week']) * 0.2
    )
    return df
def analyze_top_users(df, top_n=4):
    return df.sort_values('influence_score', ascending=False).head(top_n)
def plot_influencers(df, top_users):
    plt.scatter(df['followers'], df['engagement_rate'], alpha=0.5)
    plt.scatter(top_users['followers'], top_users['engagement_rate'], color='red', label='Top Influencers')
    plt.xscale('log')
    plt.xlabel('Followers (log scale)')
    plt.ylabel('Engagement Rate (%)')
    plt.title('Followers vs Engagement Rate')
    plt.legend()
    plt.show()

df = generate_user_data()  # Generate sample user data
df = calculate_influence(df)  # Calculate influence scores
top_users = analyze_top_users(df)  # Analyze top users
print("Top 4 Influential Users:")
print(top_users[['user_id', 'followers', 'engagement_rate', 'posts_per_week', 'influence_score']])
plot_influencers(df, top_users)