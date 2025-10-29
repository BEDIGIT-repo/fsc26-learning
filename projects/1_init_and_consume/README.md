# Configuration d'un Environnement Gen AI

Ce guide vous accompagne dans la configuration complète d'un environnement de développement pour l'intelligence artificielle générative, incluant Python, LangChain, LangGraph, et différents fournisseurs de modèles (OpenAI, Gemini, Ollama, LM Studio).

## Prérequis

- Système d'exploitation : Windows, macOS, ou Linux
- Accès administrateur pour l'installation des outils
- Connexion internet stable

## 1. Installation d'uv (Gestionnaire de packages Python)

Pour plus de détails sur l'installation, consultez la [documentation officielle](https://docs.astral.sh/uv/getting-started/installation/).

### Sur macOS/Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Sur Windows (PowerShell)
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Vérification de l'installation
```bash
uv --version
```

## 2. Configuration de l'environnement Python

### Créer un nouveau projet avec uv
```bash
# Initialiser un projet Python avec uv
uv init example-app
cd example-app

# Installer les librairies python
uv add langgraph langchain-openai langchain-google-genai langchain-ollama python-dotenv streamlit
```

### Activer l'environnement virtuel

#### Sur macOS/Linux
```bash
source .venv/bin/activate
```

#### Sur Windows
```bash
.venv\Scripts\activate
```

## 3. Installation d'Ollama

Installer [Ollama](https://ollama.com/download/)

### Démarrer Ollama
```bash
# Démarrer le service Ollama
ollama serve

# Modèles recommandés pour commencer
ollama pull gemma3:1b

# Chat sur Ollama
ollama run gemma3:1b
```

## 5. Configuration des variables d'environnement


Ajouter vos clés API dans le fichier `.env.example` et le renommer `.env` :

- [Obtenir clé API Google](https://aistudio.google.com/app/apikey) (gratuit)
- [Obtenir clé API OpenAI](https://platform.openai.com/settings/organization/api-keys) (payant)

## 6. Test de l'installation


### Test de Gemini

```bash
source .env
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent" \
  -H 'Content-Type: application/json' \
  -H "X-goog-api-key: $GOOGLE_API_KEY" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

### Test d'OpenAI

```bash
source .env
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-4.1",
    "messages": [
      {
        "role": "developer",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Hello!"
      }
    ]
  }'
```

### Utiliser les modèles avec python
Créer un fichier `test_setup.py` :

```python
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
            model="gemini-pro",
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
```

```bash
source .venv/bin/activate
python test_setup.py
```

### Lancer le chatbot :
```bash
source .venv/bin/activate
streamlit run main.py
```

## 8. Structure de projet recommandée

```
genai-project/
├── .env                    # Variables d'environnement
├── .gitignore             # Fichiers à ignorer par Git
├── pyproject.toml         # Configuration uv/Python
├── README.md              # Documentation
├── src/                   # Code source
│   ├── __init__.py
│   ├── agents/            # Agents LangGraph
│   ├── chains/            # Chaînes LangChain
│   ├── tools/             # Outils personnalisés
│   └── utils/             # Utilitaires
├── notebooks/             # Jupyter notebooks
├── tests/                 # Tests unitaires
└── data/                  # Données et documents
```

## 9. Commandes utiles

### Gestion des dépendances avec uv
```bash
# Ajouter une nouvelle dépendance
uv add package-name

# Supprimer une dépendance
uv remove package-name

# Mettre à jour toutes les dépendances
uv lock --upgrade

# Installer toutes les dépendances depuis pyproject.toml
uv sync
```

### Ollama
```bash
# Lister les modèles installés
ollama list

# Supprimer un modèle
ollama rm model-name

# Mettre à jour un modèle
ollama pull model-name
```

## 10. Ressources utiles

- [Documentation LangChain](https://python.langchain.com/)
- [Documentation LangGraph](https://langchain-ai.github.io/langgraph/)
- [Documentation uv](https://docs.astral.sh/uv/)
- [Hub de modèles Ollama](https://ollama.ai/library)
- [Documentation OpenAI](https://platform.openai.com/docs)
- [Documentation Gemini](https://ai.google.dev/docs)

## Dépannage

### Problème avec uv
Si uv n'est pas reconnu après l'installation, redémarrez votre terminal ou ajoutez manuellement le chemin à votre PATH.

### Problème avec Ollama
Si Ollama ne se connecte pas, vérifiez que le service est démarré avec `ollama serve`.

### Problème avec les clés API
Vérifiez que vos clés API sont correctement définies dans le fichier `.env` et que vous avez des crédits suffisants sur les plateformes payantes.

---

Votre environnement Gen AI est maintenant prêt ! Vous pouvez commencer à développer des applications d'IA générative avec LangChain et LangGraph.