import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv(r'C:\Users\Sum28-04\Desktop\python\Datalar\netflix_titles.csv')

result = data.info()

data['director'] = data['director'].fillna('Unknown')
data['cast'] = data['cast'].fillna('Unknown')
data['country'] = data['country'].fillna('Unknown')

data.dropna(subset=('date_added' , 'rating' , 'duration') , inplace=True)
data['date_added'] = pd.to_datetime(data['date_added'].str.strip())
data['year_added'] = data['date_added'].dt.year
data['month_added'] = data['date_added'].dt.month_name()

plt.figure(figsize=(14,6))
plt.subplot(1,2,1)
ax = sns.countplot(x = 'type' , data=data , palette='Set2')
plt.title('Icerik turu dagilimi')
for p in ax.patches:
    ax.annotate(f'{p.get_height()}' , (p.get_x() + 0.35, p.get_height() + 50))

plt.subplot(1,2,2)
sns.countplot(x = "year_added" , data=data, palette='viridis')
plt.title('yillara gore eklenen icerik sayisi')
plt.xticks(rotation = 45)
plt.tight_layout()
plt.savefig("netflix_year_month.png", dpi=300)
plt.show()


# plt.figure(figsize=(14,6))
# top_countries = data['country'].value_counts().head(10)
# plt.subplot(1,2,1)
# sns.barplot(x = top_countries.values, y=top_countries.index, palette='magma')
# plt.title('Netflixte En Çok İçeriği Olan 10 Ülke')
# plt.xlabel('İçerik Sayısı')

# movies = data[data['type'] == 'Movie'].copy()
# movies['duration_numeric'] = movies['duration'].str.replace('min' , '').astype(float)
# plt.subplot(1,2,2)
# sns.histplot(data=movies , x = 'duration_numeric' , bins=30 ,kde=True,color='green')
# plt.title('Film Sürelerinin Dağılımı (Dakika)')
# plt.xlabel('Süre (Dakika)')
# plt.tight_layout()
# plt.savefig("netflix_duration_distribution.png", dpi=300)
# plt.show()
# print(data.info())
# # print(result)
# print(data[['year_added', 'month_added']].head())