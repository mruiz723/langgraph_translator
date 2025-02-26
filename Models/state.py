# Standard Libraries
import json

# Third Party Libraries
from pydantic import BaseModel, Field
from typing import List
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from Models.validation import Validation, parse_ai_message_to_validation
from Models.translation import Translation, parse_ai_message_to_translation
from typing import Optional
from helpers import to_markdown, display_message

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

    def display_no_translate_prompt_msg(self):
        """
        Displays a notice informing users that the assistant is for translation tasks only, 
        advising against non-translation queries. Uses emojis for clarity and engagement.
        """
        message = f""" 
        </br></br>Please remember, this assistant is designed **specifically for translation purposes** 🌍📝.  
        For the best experience, please ensure your queries are related to translating text between languages.  
        Other types of queries may not be processed correctly. ❌🤖</br></br>  
        ✅ Thank you for understanding! 😊🙏  
        ---
        """
        display_message("⚠️ **Notice:** ⚠️", message)

    def display_wrong_format_translator_prompt_msg(self):
        """
        Displays an error message guiding the user to correct their input format for translation requests,
        providing examples and using emojis for clarity. It helps improve user experience by ensuring valid requests.
        """
        error_message = f"""
        </br></br>🚨 Please use the format:</br>
        🔹 **How do you say [text] in [language]?**</br>
        🔹 **Translate [text] to [language]**</br>
        📝 Example: *How do you say 'hello' in Spanish?* 🌍</br>
        ⚠️ Incorrect formats may not be processed. Please try again! 🙏😊
        ---
        """
        display_message("❌ **Error Message:** ❌", error_message)