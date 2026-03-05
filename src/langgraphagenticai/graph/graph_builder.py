

from langgraph.graph import StateGraph, START, END
from langgraph.graph import StateGraph
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.state.state import State


class GraphBuilder:
    
    def __init__(self, model):
        self.llm_model = model
        self.graph_builder = StateGraph(State)
        
    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using LangGraph.
        This method initializes a chatbot node using the `BasicChatbotNode` class 
        and integrates it into the graph. The chatbot node is set as both the 
        entry and exit point of the graph.
        """
        self.basic_chatbot_node = BasicChatbotNode(self.llm_model)
        
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.processBasicChat)
        self.graph_builder.add_edge("chatbot", END)
    
    def setup_graph(self, usecase: str):
        """
            Set up the graph for selected usecase
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
            
        # if usecase == "Chatbot With Web":
        #     self.chatbot_with_tools_build_graph()
        
        # if usecase == "AI News":
        #     self.ai_news_builder_graph()
        
        return self.graph_builder.compile()