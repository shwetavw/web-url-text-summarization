import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.schema import Document
from langchain_community.document_loaders import WebBaseLoader
import validators

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_prompt():
    prompt_template = """Provide a concise summary of the web page in 500 words with the following details:
    Add a Title
    Add a concise summary of the content
    "{text}"
    CONCISE SUMMARY:"""
    return PromptTemplate.from_template(prompt_template)

def load_web_page_content(page_url):
    loader = WebBaseLoader(page_url)
    return loader.load()[0].page_content

def initialize_model_and_chain(prompt):
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0)
    chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
    return chain

def main():
    st.set_page_config(page_title="Web Page Text Summarization App", page_icon="")
    st.title("Web Page Text Summarization")
    page_url = st.text_input("Enter Web Page URL")

    # Get prompt
    prompt = get_prompt()

    if st.button("Summarize Content from Web Page"):
        if not page_url.strip():
            st.error("Please provide a web page URL.")
        elif not validators.url(page_url):
            st.error("Please enter a valid web URL.")
        else:
            try:
                with st.spinner("Fetching and summarizing web page content..."):
                    # Load the web page content
                    content = load_web_page_content(page_url)

                    # Create a document object for summarization
                    document = Document(page_content=content)

                    llm=ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0)

                    # Chain for summarization
                    chain = initialize_model_and_chain(prompt)
                    result = chain.invoke({"input_documents": [document]})

                    # Get the output summary
                    output_summary = result.get("output_text", "No summary available.")
                    st.success(output_summary)
            except Exception as e:
                st.exception(f"Exception: {e}")

if __name__ == "__main__":
    main()