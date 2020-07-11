import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

# importing data

df = pd.read_csv('mbtiData.csv')
print(df.head(10))
print("*"*40)
print(df.info())

df['words_per_comment'] = df['posts'].apply(lambda x: len(x.split()))
print(df.head())

# exploratory data analysis

plt.figure(figsize = (15,10))
sns.violinplot(x = 'type', y = 'words_per_comment', data = df, inner = None, color = 'lightgray')
sns.stripplot(x='type', y='words_per_comment', data=df, size=4, jitter=True)
plt.ylabel("Words per comment")
plt.show()