
from src.langgraphagenticai.state.state import State
from langchain_core.messages import SystemMessage


class ChatbotWithToolNode:
    """
    Chatbot with tool node logic implementation
    """
    
    def __init__(self, model) -> None:
        self.llm = model
        
    def process(self, state:State) -> dict:
        """
        Process the input state and generate a chatbot response with tool integration
        """
        
        user_input = state["messages"][-1] if state["messages"] else ""
        llm_response = self.llm.invoke([{"role": "user", "content": user_input}])
        
        #simulate tool-specific logic
        tools_response = f"Tool integration for: '{user_input}'"
        
        return{"messages": [llm_response, tools_response]} 
    
    def create_chatbot(self, tools):
        '''
        Returns a chatbot node function
        '''
        
        # System prompt that instructs the LLM when to use tools
        system_prompt = """You are a helpful assistant. Use the Tavily Search tool ONLY when:
                            1. The user asks for current information (news, recent events, weather, etc.)
                            2. You don't have enough information in your knowledge base to answer accurately
                            3. The question requires real-time or up-to-date information

                            For general questions, common knowledge, math, reasoning, coding, and other tasks where you have sufficient knowledge, answer directly WITHOUT using tools.
                            Always try to answer from your existing knowledge first."""
        
        llm_with_tools = self.llm.bind_tools(tools)
        
        def chatbot_node(state: State):
            '''
            Chatbot logic for processing the input state and returning a response
            '''
            # Prepend system message to the conversation
            messages = state["messages"]
            system_message = SystemMessage(content=system_prompt)
            messages_with_system = [system_message] + messages
            
            return {"messages": [llm_with_tools.invoke(messages_with_system)]}
        
        return chatbot_node
    