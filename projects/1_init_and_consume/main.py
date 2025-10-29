from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain_ollama.chat_models import ChatOllama
import streamlit as st

from langchain_core.messages import HumanMessage


def main():
    
    load_dotenv()

    with st.sidebar:
        st.title("Model Selection")
        model_choice = st.radio(
            "Choose a model:",
            ("OpenAI", "Gemini", "Ollama"),
            index=0
        )
    if model_choice == "OpenAI":
        llm = ChatOpenAI(model="gpt-4o")
    elif model_choice == "Gemini":
        llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
    elif model_choice == "Ollama":
        llm = ChatOllama(model="gemma3:1b")

    ## Uncomment to use a model
    # OpenAI
    # llm = ChatOpenAI(model="gpt-4o")

    # Gemini
    # llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

    # Ollama
    # llm = ChatOllama(model="gemma3:1b")
    if "messages" not in st.session_state:
        st.session_state["messages"] = []


    for message in st.session_state["messages"]:
        with st.chat_message(message.type):
            st.markdown(message.content)
    
    if prompt := st.chat_input():
        st.chat_message("user").write(prompt)
        st.session_state["messages"].append(HumanMessage(prompt))
        response = llm.invoke(st.session_state["messages"])
        st.session_state.messages.append(response)
        st.rerun()
        

if __name__ == "__main__":
    main()