import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
# --- 1. Synthetic Data Generation ---
np.random.seed(42) # for reproducibility
# Generate synthetic data for menu items, prices, and reviews
num_items = 50
data = {
    'MenuItem': [f'Item {i+1}' for i in range(num_items)],
    'Price': np.random.uniform(5, 30, num_items).round(2),
    'Review': [f'This {item} was {sentiment}' for item, sentiment in zip([f'Item {i+1}' for i in range(num_items)],
                                                                         ['amazing and delicious', 'okay but overpriced', 'terrible', 'good value', 'disappointing', 'excellent'] * 9 + ['great'])]
}
df = pd.DataFrame(data)
# --- 2. Sentiment Analysis ---
df['Polarity'] = df['Review'].apply(lambda review: TextBlob(review).sentiment.polarity)
df['Subjectivity'] = df['Review'].apply(lambda review: TextBlob(review).sentiment.subjectivity)
# --- 3. Data Cleaning (if needed) ---
# In a real-world scenario, this section would handle missing values, outliers, etc.
# For this example, we assume the synthetic data is clean.
# --- 4. Analysis ---
# Correlate price with sentiment
correlation = df['Price'].corr(df['Polarity'])
print(f"Correlation between Price and Polarity: {correlation}")
# Group by price ranges and analyze average sentiment
df['PriceRange'] = pd.cut(df['Price'], bins=[0, 10, 20, 30], labels=['Low', 'Medium', 'High'])
average_sentiment = df.groupby('PriceRange')['Polarity'].mean()
print("\nAverage Sentiment by Price Range:")
print(average_sentiment)
# --- 5. Visualization ---
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Price', y='Polarity', data=df)
plt.title('Price vs. Sentiment Polarity')
plt.xlabel('Price')
plt.ylabel('Polarity')
plt.grid(True)
plt.tight_layout()
# Save the plot to a file
output_filename = 'price_vs_polarity.png'
plt.savefig(output_filename)
print(f"Plot saved to {output_filename}")
plt.figure(figsize=(10, 6))
sns.barplot(x=average_sentiment.index, y=average_sentiment.values)
plt.title('Average Sentiment by Price Range')
plt.xlabel('Price Range')
plt.ylabel('Average Polarity')
plt.grid(True)
plt.tight_layout()
# Save the plot to a file
output_filename = 'average_sentiment_by_price_range.png'
plt.savefig(output_filename)
print(f"Plot saved to {output_filename}")