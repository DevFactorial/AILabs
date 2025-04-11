# AILabs
Playground for tinkering with AI related stuff.

# Projects
## Basic ChatBot App
<h>A simple Chat application which uses Groq provider behind the scenes to connect to a LLM.</h>
### Instructions
- Create a python env.
- pip install -r requirements.txt
- Go to https://console.groq.com/. Get an API key (Its free!).
- export GROQ_API_KEY=<API_KEY>
- Run ' streamlit run main.py'

## Basic AI Agent App
<h>A simple Agentic application with tool calling for getting details of food rich in various nutrients. Uses Groq provider behind the scenes to connect to a LLM.</h>
### Instructions
- Create a python env.
- pip install -r requirements.txt
- From the repository root folder, run export PYTHONPATH=$PWD
- Go to https://console.groq.com/. Get an API key (Its free!).
- export GROQ_API_KEY=<API_KEY>
- Navigate to frontend folder.
- Run ' streamlit run main.py'

Sample questions:
1. Provide me a list of food which is rich in calcium
2. Provide me a list of food which is rich in protein
