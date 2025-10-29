import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama

# Charger les variables d'environnement
load_dotenv()

def test_openai():
    try:
        llm = ChatOpenAI(model="gpt-4o")
        response = llm.invoke("Hello, world!")
        print("✅ OpenAI fonctionne")
        return True
    except Exception as e:
        print(f"❌ OpenAI: {e}")
        return False

def test_gemini():
    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
        )
        response = llm.invoke("Hello, world!")
        print("✅ Gemini fonctionne")
        return True
    except Exception as e:
        print(f"❌ Gemini: {e}")
        return False

def test_ollama():
    try:
        llm = ChatOllama(model="gemma3:1b")
        response = llm.invoke("Hello, world!")
        print("✅ Ollama fonctionne")
        return True
    except Exception as e:
        print(f"❌ Ollama: {e}")
        return False

if __name__ == "__main__":
    print("Test de l'environnement Gen AI...")
    test_openai()
    test_gemini()
    test_ollama()