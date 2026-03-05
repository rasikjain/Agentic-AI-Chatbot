import streamlit as st
import os
from src.langgraphagenticai.ui.uiconfigfile import UIConfig


class LoadStreamlitUI:
    def __init__(self):
        self.ui_config =  UIConfig()
        self.user_controls = {}

    def load_streamlit_ui(self):
        
        st.set_page_config(page_title=self.ui_config.get_page_title(), page_icon="🤖", layout="wide")
        st.header("🤖 " + self.ui_config.get_page_title())

        with st.sidebar:
            llm_options = self.ui_config.get_llm_options()
            usecase_options = self.ui_config.get_usecase_options()
            
            self.user_controls['selected_llm'] = st.selectbox("Select LLM", llm_options)
            
            if self.user_controls['selected_llm'] == "Groq":
                
                #Model Selection
                model_options = self.ui_config.get_groq_model_options()
                self.user_controls['selected_groq_model'] = st.selectbox("Select Groq Model", model_options)
                self.user_controls['GROQ_API_KEY'] = st.session_state["GROQ_API_KEY"] = st.text_input("Enter Groq API Key", type="password")
                
                
                if not self.user_controls['GROQ_API_KEY']:
                    st.warning("Please enter your Groq API Key to proceed.")
                    st.stop()
             
            #Usecase selection       
            self.user_controls['selected_usecase'] = st.selectbox("Select Use Case", usecase_options)
            
            if self.user_controls['selected_usecase'] == "Chatbot With Web(Tool)":
                os.environ["TAVILY_API_KEY"] = self.user_controls['TAVILY_API_KEY'] = st.session_state["TAVILY_API_KEY"] = st.text_input("Enter Tavily API Key for Web Search", type="password")
                
                if not self.user_controls['TAVILY_API_KEY']:
                    st.warning("Please enter your Tavily API Key to proceed.")
                    st.stop()
                    
        return self.user_controls