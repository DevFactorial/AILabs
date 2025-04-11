import streamlit as st

from app.core.agent import execute_agent

def click_button():
    
    st.write_stream(execute_agent(input))


input = st.text_input('Provide a prompt')

st.button('Submit', on_click=click_button)


