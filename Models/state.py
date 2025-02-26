# Standard Libraries
import json

# Third Party Libraries
from pydantic import BaseModel, Field
from typing import List
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from Models.validation import Validation, parse_ai_message_to_validation
from Models.translation import Translation, parse_ai_message_to_translation
from typing import Optional
from helpers import to_markdown

class State(BaseModel):
    messages: List[BaseMessage] 
    validation: Optional[Validation] = None 
    translation: Optional[Translation] = None

    def add_validation_state(self, ai_message):
        validation = parse_ai_message_to_validation(ai_message)
        self.messages.append(ai_message) 
        self.validation = validation
        display(to_markdown(f"---\n #### START\n ---"))
        self.display_state(f"#### Validator:\n ---")

    def add_translation_state(self, ai_message):
        translation = parse_ai_message_to_translation(ai_message)
        self.messages.append(ai_message)
        self.translation = translation
        self.display_state(f"#### Translator:\n ---")

    def display_state(self, title):
        display(to_markdown(title))
        self.display_state_in_json()

    def display_state_in_json(self):
        """
        Displays the state in a JSON way
        """
        state_dict_str = f"""
        ```json
        {json.dumps(self.model_dump(), indent=2)}
        ```
        """
        display(to_markdown(state_dict_str, code="json"))
        display(to_markdown("---"))