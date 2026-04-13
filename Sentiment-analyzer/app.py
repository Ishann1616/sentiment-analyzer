import plotly.express as px
import pandas as pd
import streamlit as st
from news_fetcher import NewsFetcher
from sentiment_analyzer import SentimentAnalyzer
from rss_fetcher import RSSFetcher

if "compare" not in st.session_state:
    st.session_state["compare"] = False

st.title("🔍 SentiScope")
st.subheader("Analyze public sentiment on any topic")

api_key = "5c805add9ccc4c93816e65bda43de9d7"

def fetch_and_analyze(topic, nf, sa, rf):
    articles = nf.fetch(topic)
    rss_articles = rf.fetch(topic)
    articles = articles + rss_articles
    results = []
    for article in articles:
        result = sa.analyze(article["title"])
        result["source"] = article["source"]
        results.append(result)
    return results

def show_results(results, topic):
    positive = len([r for r in results if "Positive" in r["sentiment"]])
    negative = len([r for r in results if "Negative" in r["sentiment"]])
    neutral = len([r for r in results if "Neutral" in r["sentiment"]])

    col1, col2, col3 = st.columns(3)
    col1.metric("Positive 😊", positive)
    col2.metric("Negative 😞", negative)
    col3.metric("Neutral 😐", neutral)

    chart_data = pd.DataFrame({
        "Sentiment": ["Positive", "Negative", "Neutral"],
        "Count": [positive, negative, neutral]
    })

    fig = px.pie(
        chart_data,
        values="Count",
        names="Sentiment",
        title=f"Sentiment Breakdown for '{topic}'",
        color="Sentiment",
        color_discrete_map={
            "Positive": "#00E676",
            "Negative": "#FF1744",
            "Neutral": "#90A4AE"
        }
    )
    st.plotly_chart(fig)

    total = positive + negative + neutral
    if total > 0:
        if positive > negative and positive > neutral:
            verdict = f"🟢 Public opinion on '{topic}' is mostly POSITIVE"
        elif negative > positive and negative > neutral:
            verdict = f"🔴 Public opinion on '{topic}' is mostly NEGATIVE"
        else:
            verdict = f"🟡 Public opinion on '{topic}' is mostly NEUTRAL"
        st.subheader(verdict)

    st.divider()

    positive_articles = [r for r in results if "Positive" in r["sentiment"]]
    negative_articles = [r for r in results if "Negative" in r["sentiment"]]

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🟢 Top Positive")
        if positive_articles:
            for r in positive_articles[:3]:
                st.success(r["text"])
        else:
            st.write("No positive articles found")

    with col2:
        st.subheader("🔴 Top Negative")
        if negative_articles:
            for r in negative_articles[:3]:
                st.error(r["text"])
        else:
            st.write("No negative articles found")

    st.divider()
    st.subheader("📰 All Articles")
    for r in results:
        st.write(f"{r['sentiment']} | Score: {r['score']} | {r['text']}")

topic = st.text_input("Enter a Topic", placeholder="e.g. Trump")

col_btn1, col_btn2 = st.columns(2)
with col_btn1:
    single_mode = st.button("🔍 Analyze Topic")
with col_btn2:
    compare_mode = st.button("⚔️ Compare Two Topics")

if compare_mode:
    st.session_state["compare"] = True

if single_mode:
    st.session_state["compare"] = False
    if topic:
        with st.spinner("Fetching and analyzing..."):
            nf = NewsFetcher(api_key)
            sa = SentimentAnalyzer()
            rf = RSSFetcher()
            results = fetch_and_analyze(topic, nf, sa, rf)
            show_results(results, topic)
    else:
        st.warning("Please enter a topic!")
if st.session_state["compare"]:
    topic2 = st.text_input("Enter second topic", placeholder="e.g. Modi")
    if topic and topic2:
        with st.spinner("Fetching and analyzing both topics..."):
            nf = NewsFetcher(api_key)
            sa = SentimentAnalyzer()
            rf = RSSFetcher()

            col1, col2 = st.columns(2)
            with col1:
                st.header(f"📊 {topic.upper()}")
                results1 = fetch_and_analyze(topic, nf, sa, rf)
                show_results(results1, topic)
            with col2:
                st.header(f"📊 {topic2.upper()}")
                results2 = fetch_and_analyze(topic2, nf, sa, rf)
                show_results(results2, topic2)

# streamlit run app.py