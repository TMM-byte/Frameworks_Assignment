import zipfile
import pandas as pd

# Unzip and read the CSV
with zipfile.ZipFile('metadata.csv.zip', 'r') as zip_ref:
    zip_ref.extractall('unzipped_data')  # Extract to a folder

df = pd.read_csv('unzipped_data/metadata.csv', low_memory=False)

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Check DataFrame structure
print("\nDataFrame info:")
print(df.info())

# Check DataFrame dimensions
print("\nShape of DataFrame:")
print(df.shape)

# Check data types
print("\nData types:")
print(df.dtypes)

# Check for missing values
print("\nMissing values (top columns):")
print(df.isnull().sum().sort_values(ascending=False).head(20))

# Generate basic statistics
print("\nStatistics for numerical columns:")
print(df.describe())


# Show column names
print("\nColumn names:")
print(df.columns.tolist())

# Identify columns with lots of missing values
missing_percent = df.isnull().mean() * 100
print("Columns with >50% missing values:")
print(missing_percent[missing_percent > 50])

# Drop columns with excessive missing values (optional)
df_cleaned = df.drop(columns=missing_percent[missing_percent > 50].index)

# Drop rows where title or abstract is missing (important for NLP)
df_cleaned = df_cleaned.dropna(subset=['title', 'abstract'])

# Convert publish_time to datetime
df_cleaned['publish_time'] = pd.to_datetime(df_cleaned['publish_time'], errors='coerce')

# Extract year from publish_time
df_cleaned['year'] = df_cleaned['publish_time'].dt.year

# Create abstract word count
df_cleaned['abstract_word_count'] = df_cleaned['abstract'].apply(lambda x: len(str(x).split()))

# VISUALIZATION
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Count of papers by year
print(df_cleaned['year'].value_counts().sort_index())

# Top journals
top_journals = df_cleaned['journal'].value_counts().head(10)
print(top_journals)

# Publications over time
df_cleaned['year'].value_counts().sort_index().plot(kind='bar', figsize=(10,6), title='Publications per Year')
plt.xlabel('Year')
plt.ylabel('Number of Publications')
plt.tight_layout()
plt.show()

# Top publishing journals
top_journals.plot(kind='bar', figsize=(10,6), title='Top Journals')
plt.xlabel('Journal')
plt.ylabel('Number of Papers')
plt.tight_layout()
plt.show()

# Word Cloud of Titles
text = ' '.join(df_cleaned['title'].dropna().astype(str).tolist())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
plt.figure(figsize=(15, 7))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Most Common Words in Paper Titles')
plt.show()
