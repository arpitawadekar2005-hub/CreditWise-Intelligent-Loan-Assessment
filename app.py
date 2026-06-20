import streamlit as st
import os

st.set_page_config(page_title="CreditWise Debug")

st.title("🔍 CreditWise Debug")

st.write("Current working directory:")
st.write(os.getcwd())

st.write("Files available in repository:")
st.write(os.listdir("."))

st.success("Debug app loaded successfully!")
