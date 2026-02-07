import streamlit as st
import pandas as pd
import logging
from agent import get_pandas_agent

# ---------------------------
# Logging setup
# ---------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# ---------------------------
# Page config
# ---------------------------
st.set_page_config(
    page_title="CSV Analysis Copilot",
    layout="centered"
)

logger.info("CSV Analysis Copilot app started")

# ---------------------------
# Header
# ---------------------------
st.markdown(
    """
    <h1 style="text-align:center;">📊 CSV Analysis Copilot</h1>
    <p style="text-align:center; color: gray;">
        Upload a CSV and ask questions in plain English
    </p>
    """,
    unsafe_allow_html=True
)

st.write("")

# ---------------------------
# File upload
# ---------------------------
uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type="csv"
)

# ---------------------------
# Run only if file uploaded
# ---------------------------
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    logger.info("CSV file uploaded and read into DataFrame")
    logger.info(f"Dataset shape: {df.shape}")
    logger.info(f"Columns: {list(df.columns)}")

    st.success("CSV loaded successfully!")

    # ---------------------------
    # Data Overview
    # ---------------------------
    st.subheader("🔍 Data Overview")
    st.dataframe(df.head())

    # ---------------------------
    # Dataset Information
    # ---------------------------
    st.subheader("📌 Dataset Information")
    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**Rows:** {df.shape[0]}")
        st.write(f"**Columns:** {df.shape[1]}")

    with col2:
        st.write("**Column Names:**")
        st.write(list(df.columns))

    # ---------------------------
    # Data Quality
    # ---------------------------
    st.subheader("🧹 Data Quality")
    col1, col2 = st.columns(2)

    with col1:
        st.write("**Missing Values**")
        st.write(df.isna().sum())

    with col2:
        st.write("**Data Types**")
        st.write(df.dtypes)

    # ---------------------------
    # AI-powered Q&A
    # ---------------------------
    st.subheader("🤖 Ask a Question (AI Copilot)")

    user_query = st.text_input(
        "Ask anything about the data",
        placeholder="e.g. Which column has the highest average?"
    )

    if user_query:
        logger.info(f"AI query received: {user_query}")

        agent = get_pandas_agent(df)

        with st.spinner("Analyzing data with AI..."):
            try:
                response = agent.run(user_query)
                st.markdown("### ✅ Answer")
                st.write(response)
            except Exception as e:
                logger.error(f"AI error: {e}")
                st.error("AI failed to analyze the data.")

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; font-size:14px; color:gray;">
        Created by <b>Sarthak Singh</b>
    </div>
    """,
    unsafe_allow_html=True
)
