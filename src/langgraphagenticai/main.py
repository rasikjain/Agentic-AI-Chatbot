import streamlit as st
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMs.groqllm import GroqLLM
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit


def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while 
    implementing exception handling for robustness.
    """
    
    ##Load UI
    ui = LoadStreamlitUI()
    user_controls_input = ui.load_streamlit_ui()
    
    if not user_controls_input:
        st.warning("User input is required to proceed.")
        return
    
    user_message = st.chat_input("Enter your message here:")
    
    if user_message:
        try:
            ## Coffigure LLM's
            obj_groq = GroqLLM(user_controls_input)
            llm_model = obj_groq.get_llm_model()
            
            if not llm_model:
                st.error("Error: Failed to initialize the LLM model.")
                return
            
            
            #Initialize Graph Builder and Build Graph based on usecase
            usecase = user_controls_input.get('selected_usecase')
            
            if not usecase:
                st.error("Please select a use case to proceed.")
                return
            
            #Graph Builder
            graph_builder = GraphBuilder(llm_model)
            
            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()
            
            except Exception as e:      
                st.error(f"Error setting up the graph: {e}")
                return
                
            
        except Exception as e:
            st.error(f"An error occurred: {e}")
            return
        
    