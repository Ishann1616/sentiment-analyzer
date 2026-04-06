import plotly.express as px
import pandas as pd
import streamlit as st
from news_fetcher import NewsFetcher
from sentiment_analyzer import SentimentAnalyzer

st.title("SentiScope")
st.subheader("Analyze public sentiment on any topic")

api_key="5c805add9ccc4c93816e65bda43de9d7"

topic =st.text_input("Enter a Topic", placeholder="e.g. Trump stand on WW3")

if st.button("Analyze"):
    if topic:
        with st.spinner("Fetching and analyzing..."):
            nf = NewsFetcher(api_key)
            sa = SentimentAnalyzer()

            articles = nf.fetch(topic)

            results = []

            for article in articles:
                result = sa.analyze(article["title"])
                result["source"] = article["source"]
                results.append(result)

            positive=len([r for r in results if "Positive" in r["sentiment"]])
            negative = len([r for r in results if "Negative" in r["sentiment"]])
            neutral = len([r for r in results if "Neutral" in r["sentiment"]])

            col1, col2, col3 = st.columns(3)
            col1.metric("Positive 😊", positive)
            col2.metric("Negative 😞", negative)
            col3.metric("Neutral 😐", neutral)

            chart_data= pd.DataFrame({
            "Sentiment": ["Positive", "Negative", "Neutral"],
            "Count": [positive, negative, neutral]
            })
            
            fig =px.pie(
                chart_data,
                values="Count",
                names="Sentiment",
                title=f"Sentiment Breakdown for '{topic}'",
                color_discrete_map={
                    "Positive": "#00C853",
                    "Negative": "#D50000",
                    "Neutral": "#FFD600"
                }

            )
            st.plotly_chart(fig)

            st.divider()
            
            for r in results:
                st.write(f"{r['sentiment']} | Score: {r['score']} | {r['text']}")
    else:
        st.warning("Please enter a topic!")