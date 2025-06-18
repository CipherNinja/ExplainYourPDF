import streamlit as st
from src.extractor import extract_text
from src.summarizer import summarize_text


st.set_page_config(page_title="PDF Summarizer", layout="wide")

st.title("PDF Text Extractor & Summarizer")
st.write("Upload a PDF file to extract text and generate a summary.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    with st.spinner("Extracting text..."):
        extracted_text = extract_text(uploaded_file)
    
    st.subheader("Extracted Text")
    st.text_area("Raw Text", extracted_text, height=300)
    
    # Summarize button
    if st.button("Generate Summary"):
        with st.spinner("Summarizing..."):
            summary = summarize_text(extracted_text)
        st.subheader("Summary")
        st.write(summary)


st.markdown(
    """
    <style>
    .stApp {
        background-color: #1e1e1e;
        color: #ffffff;
    }
    .stTextArea textarea {
        background-color: #2c2c2c;
        color: #ffffff;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True
)
