import pandas as pd 
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# importing data

df = pd.read_csv('mbtiData.csv')
print(df.head(10))
print("*"*40)
print(df.info())

df['words_per_comment'] = df['posts'].apply(lambda x: len(x.split()))

# exploratory data analysis

#sns.violinplot(x = 'type', y = 'words_per_comment', data = df, inner = None, color = 'lightgray')
#sns.stripplot(x='type', y='words_per_comment', data=df, size=4, jitter=True)
plt.ylabel("Words per comment")
#plt.show()

df["http per comment"] = df['posts'].apply(lambda x: x.count('http'))
df['music_per_comment'] = df['posts'].apply(lambda x: x.count('music')/50)
df['question_per_comment'] = df['posts'].apply(lambda x: x.count('?')/50)
df['img_per_comment'] = df['posts'].apply(lambda x: x.count('jpg')/50)
df['excl_per_comment'] = df['posts'].apply(lambda x: x.count('!')/50)
df['ellipsis_per_comment'] = df['posts'].apply(lambda x: x.count('...')/50)
#sns.jointplot(x = 'words_per_comment', y = 'ellipsis_per_comment', data = df, kind= 'kde') #heat map
print(df.head(10))
#plt.show()

i = df['type'].unique()
k = 0
TypeArray = []
PearArray = []
for m in range(0,15):
    df_2 = df[df['type'] == i[k]]
    #sns.jointplot(x='words_per_comment', y='ellipsis_per_comment', data=df_2, kind="hex")
    pearsonCoefficient = np.corrcoef(x = df_2['words_per_comment'], y = df_2['ellipsis_per_comment'])
    pear = pearsonCoefficient[1][0]
    TypeArray.append(i[k])
    PearArray.append(pear)
    plt.title(i[k])
    k+=1
    #plt.show()

TypeArray = [x for _,x in sorted(zip(PearArray,TypeArray))]
PearArray = sorted(PearArray, reverse = True)
plt.scatter(TypeArray, PearArray)
plt.ylabel("Pearson Coefficient")
plt.xlabel("Personality Type")
plt.title("Pearson Coefficient (for word count and ellipsis per comment) and Type")
plt.show()

map1 = {"I": 0, "E": 1}
map2 = {"N": 0, "S": 1}
map3 = {"T": 0, "F": 1}
map4 = {"J": 0, "P": 1}
df['I-E'] = df['type'].str[0]
df['I-E'] = df['I-E'].map(map1)
df['N-S'] = df['type'].str[1]
df['N-S'] = df['N-S'].map(map2)
df['T-F'] = df['type'].str[2]
df['T-F'] = df['T-F'].map(map3)
df['J-P'] = df['type'].str[3]
df['J-P'] = df['J-P'].map(map4)

print(df.head(10))