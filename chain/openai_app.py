# Integrate OpenAI API

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from langchain_community.llms import ollama
# from langchain.schema import HumanMessage,SystemMessage,AIMessage

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
#LangSmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "True"
os.environ["LANGCHAIN_ENDPOINT"] ="https://api.smith.langchain.com"

print(f'OPENAI_API_KEY : {os.getenv("OPENAI_API_KEY")}')
print(f'LANGCHAIN_API_KEY : {os.getenv("LANGCHAIN_API_KEY")}')
print(f'LANGCHAIN_TRACING_V2 : {os.getenv("LANGCHAIN_TRACING_V2")}')

## Prompt Template
prompt = ChatPromptTemplate().from_messages(
    [
        ("system", "You are a helpful assistant. Please responde to the user queries."),
        ("user", "Question:{question}")
    ]
)

## streamlit framework
st.title('Langchain Demo with OpenAI API using Streamlit UI')
input_text = st.text_input("Search the topic you want")

## OpenAI LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))

## To run the script : streamlit run yourscript.py

