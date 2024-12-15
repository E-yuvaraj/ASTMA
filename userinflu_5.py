import pandas as pd
import matplotlib.pyplot as plt

data = {
    'user': ['User1', 'User2', 'User3', 'User4', 'User5', 'User6', 'User7', 'User8', 'User9', 'User10', 'User11', 'User12'],
    'followers': [1000, 5000, 3000, 10000, 2000, 8000, 15000, 6000, 4000, 12000, 7000, 9000],
    'engagement_rate': [0.05, 0.02, 0.03, 0.01, 0.04, 0.02, 0.01, 0.03, 0.05, 0.02, 0.03, 0.02]
}

df = pd.DataFrame(data)
df['influence_score'] = df['followers'] * df['engagement_rate']

df.nlargest(10, 'influence_score').plot(kind='bar', x='user', y='influence_score', legend=False, color='skyblue', figsize=(12, 6))
plt.show()
