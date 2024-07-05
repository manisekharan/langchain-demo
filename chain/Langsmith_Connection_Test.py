from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
print(os.getenv("LANGCHAIN_TRACING_V2"))
#os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2")


llm = ChatOpenAI(model="gpt-3.5-turbo-16k")
llm.invoke("Hello, world!")