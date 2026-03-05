from configparser import ConfigParser
import os

class UIConfig:
    def __init__(self, config_file='./src/langgraphagenticai/ui/uiconfig.ini') -> None:
        
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_page_title(self):
        return self.config.get('DEFAULT', 'PAGE_TITLE')

    def get_llm_options(self):
        return [option.strip() for option in self.config.get('DEFAULT', 'LLM_OPTIONS').split(',')]

    def get_usecase_options(self):
        return [option.strip() for option in self.config.get('DEFAULT', 'USECASE_OPTIONS').split(',')]

    def get_groq_model_options(self):
        return [option.strip() for option in self.config.get('DEFAULT', 'GROQ_MODEL_OPTIONS').split(',')]