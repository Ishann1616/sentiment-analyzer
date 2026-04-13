# 🔍 SentiScope — AI Sentiment Analyzer

A real-time AI-powered sentiment analysis tool that analyzes 
public opinion on any topic using news from multiple sources.

## 🌐 Live Demo
[Click here to try it live](http://sentiment-analyzer-zpghzcndgk6zoxvz3d23bq.streamlit.app)

## 🚀 What it does
- Enter any topic (Trump, Modi, iPhone, etc.)
- Fetches real-time news from BBC, NDTV, Times of India, 
  The Hindu, NPR and NewsAPI
- Analyzes sentiment using HuggingFace AI (DistilBERT)
- Shows breakdown — Positive, Negative, Neutral
- Compare two topics side by side (e.g. Trump vs Modi)
- Displays top positive and negative headlines

## 🛠️ Tech Stack
- Python
- Streamlit
- HuggingFace Transformers (DistilBERT)
- Plotly
- NewsAPI
- RSS Feeds
- Pandas

## 📦 Installation
git clone https://github.com/Ishann1616/sentiment-analyzer
cd sentiment-analyzer
pip install -r requirements.txt
streamlit run Sentiment-analyzer/app.py

## 📸 Features
- Real-time sentiment analysis
- Multi-source news fetching
- AI-powered accuracy (9/10)
- Topic comparison mode
- Interactive pie charts
- Top positive/negative headlines
