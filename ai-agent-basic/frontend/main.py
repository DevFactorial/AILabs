import streamlit as st
import os

st.set_page_config(
    page_title="Invoice Extractor Agent",
    page_icon="👋",
)


file_path = os.path.join("pages")
chat_app = st.Page(
     os.path.join(file_path, "agent_ui.py"), title="Nutrition Agent App", default=True
)

pg = st.navigation(
        {
            "Home": [chat_app]
        }
    )

pg.run()