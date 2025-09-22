CORD-19 Metadata Dashboard Report

Project Overview
This dashboard explores COVID-19-related research metadata from the CORD-19 dataset. It provides interactive visualizations to help users understand publication trends, journal prominence, and thematic focus across years.

  Dataset
-	Source:  (extracted from Kraggle )
-	Contents: Metadata on thousands of COVID-19 research papers

  Data Cleaning & Enrichment
-	Removed entries missing  
- 	Converted  to datetime format
- 	Extracted  from 
- 	Calculated  for semantic analysis

Key Findings
- Publication Trends: Research output peaked during the early pandemic years, with thousands of papers published in rapid succession.
- Top Journals: A small group of journals dominated publication volume, reflecting centralized dissemination of COVID-19 research.
- Title Semantics: Word cloud analysis revealed frequent use of terms like COVID, SARS-CoV-2 and pandemic

 Visualizations
-	Bar chart of publications per year
-	Bar chart of top publishing journals

  Streamlit Features
- 	Year slider for dynamic filtering
- 	Interactive data sample viewer
-	Real-time updates to charts and word cloud

 Reflection: Challenges & Learning
 Technical Challenges
-	ZIP Handling: Initial errors occurred when trying to read a CSV that hadn’t been extracted.

- 	The streamlit app had initially given me trouble in launching but worked my way around the situation through research.
-	Visualization Backend: Matplotlib’s non-interactive backend caused display issues until switching to VS Code with the Python extension.

 Learning Outcomes
- 	Familiarized pandas for data cleaning, filtering, and enrichment
- 	Built an interactive dashboard using Streamlit with caching and dynamic widgets
-	Gained confidence in modularizing code and preparing it for public sharing
