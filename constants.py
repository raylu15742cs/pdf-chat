from typing import Final


from dotenv import load_dotenv
import streamlit as st

load_dotenv()

PINECONE_API_KEY: Final[str] = st.secrets["API_KEYS"]["pinecone"]
PINECONE_API_ENV: Final[str] = "asia-southeast1-gcp-free"
OPENAI_API_KEY: Final[str] = st.secrets["API_KEYS"]["openai"]
INDEX_NAME: Final[str] = 'salesforcedocs'
