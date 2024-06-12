from langchain.llms import OpenAI
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
def get_openai_response(question):
    llm=OpenAI(openai_api_key=os.environ["OPENAI_API_KEY"],temperature=0.6)
    response=llm(question)
    return response
st.set_page_config(page_title="Q&A Demo")
st.header("LangChain Application")
input=st.text_input("Input :",key="input")
response=get_openai_response(input)
submit=st.button("ASK THE QUESTION")

if submit:
    st.subheader("The Response is")
    st.write(response)

