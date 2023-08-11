from typing import Final

from os import environ

from dotenv import load_dotenv
import streamlit as st

load_dotenv()

PINECONE_API_KEY: Final[str] = st.secrets["API_KEYS"]["pinecone"]
PINECONE_API_ENV: Final[str] = "asia-southeast1-gcp-free"
OPENAI_API_KEY: Final[str] = environ["OPENAI_API_KEY"]
INDEX_NAME: Final[str] = 'salesforcedocs'
