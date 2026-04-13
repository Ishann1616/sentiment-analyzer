# 🔍 SentiScope — AI Sentiment Analyzer

A real-time sentiment analysis tool that analyzes public opinion 
on any topic using AI and live news data from multiple sources.

## 🌐 Live Demo
[Click here to try it live](http://sentiment-analyzer-zpghzcndgk6zoxvz3d23bq.streamlit.app)

## 📸 Screenshot
<!-- After saving this, upload a screenshot of your app to GitHub 
and replace the line below with the actual image link -->
![SentiScope Screenshot](screenshot.png)

## 🚀 What it does
- Fetches up to 40 real-time articles per query from 6 sources
- Sources: BBC, NDTV, Times of India, The Hindu, NPR, NewsAPI
- Classifies sentiment using DistilBERT (fine-tuned on SST-2)
- Displays positive/negative breakdown with interactive pie chart
- Compare two topics side by side (e.g. Trump vs Modi)
- Shows top 3 positive and top 3 negative headlines per topic

## 🛠️ Tech Stack
- Python, Streamlit
- HuggingFace Transformers (DistilBERT)
- Plotly, Pandas
- NewsAPI, RSS Feeds

## 📦 Installation
git clone https://github.com/Ishann1616/sentiment-analyzer
cd sentiment-analyzer
pip install -r requirements.txt
streamlit run Sentiment-analyzer/app.py
