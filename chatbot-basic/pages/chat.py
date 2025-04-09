import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage, HumanMessage
import streamlit as st

st.title("Chat App")
st.caption("🚀 A Streamlit chatbot powered by Groq")
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

def get_model(model_name: str, **kwargs):
    
    return ChatGroq(
        model = model_name,
        temperature = kwargs.get("temperature", 1.0),
        max_tokens = kwargs.get("max_tokens", 3000),
        timeout = None,
        max_retries = kwargs.get("max_retries", 2)
        # other params...
    )
    
def generate_response(human_input, chat_history):
    model = get_model("llama-3.2-90b-vision-preview")
    template = """
    You are a helpful assistant. 
    Answer the following questions using the following chat history:
    
    Chat history: {chat_history}
    
    User question: {user_question}
    """
    prompt = ChatPromptTemplate.from_messages([("human", human_input)])
    chain = prompt | model
    
    return model.stream(template.format(chat_history=chat_history, user_question=human_input))
    
def stream_response(response):
    for chunk in response:
        yield chunk.content

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_input := st.chat_input("How can I help you?"):
    st.session_state.messages.append({"role": "Human", "content": user_input})
    st.session_state.chat_history.append(HumanMessage(user_input))
    with st.chat_message("Human"):
        st.markdown(user_input)

    with st.chat_message("Assistant"):
        message = st.write_stream(stream_response(generate_response(user_input, st.session_state.chat_history)))
        
        st.session_state.messages.append({"role": "assistant", "content": message})