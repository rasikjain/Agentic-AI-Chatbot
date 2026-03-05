from src.langgraphagenticai.state.state import State

class BasicChatbotNode:
    """
    Basic Chatbot node logic implementation
    """

    def __init__(self, model) -> None:
        self.llm = model
        
    def processBasicChat(self, state:State) -> dict:
        """
        Process the input state and generate a chatbot response
        """
        
        return{"messages": self.llm.invoke(state['messages'])}