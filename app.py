import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import zipfile
import os

# Load and clean data
@st.cache_data
def load_data():
    # Unzip metadata.zip if not already extracted
    if not os.path.exists('unzipped_data/metadata.csv'):
        with zipfile.ZipFile('metadata.zip', 'r') as zip_ref:
            zip_ref.extractall('unzipped_data')

    # Load CSV
    df = pd.read_csv('unzipped_data/metadata.csv', low_memory=False)

    # Clean and enrich
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    df['abstract_word_count'] = df['abstract'].astype(str).apply(lambda x: len(x.split()))

    # Drop rows missing title or abstract
    return df.dropna(subset=['title', 'abstract'])

# Load data
df = load_data()

# App title and intro
st.title("📊 CORD-19 Metadata Dashboard")
st.write("Explore COVID-19-related research metadata interactively.")

# Sidebar filter
selected_year = st.slider("📅 Select Year", int(df['year'].min()), int(df['year'].max()), step=1)
filtered_df = df[df['year'] == selected_year]

# Sample data
st.subheader(f"🔍 Sample Papers from {selected_year}")
st.dataframe(filtered_df[['title', 'journal', 'publish_time']].head(10))

# Top journals
st.subheader("🏛️ Top Publishing Journals")
top_journals = filtered_df['journal'].value_counts().head(10)
st.bar_chart(top_journals)

# Word Cloud of Titles
st.subheader("🧠 Word Cloud of Paper Titles")
text = ' '.join(filtered_df['title'].astype(str).tolist())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
st.image(wordcloud.to_array())