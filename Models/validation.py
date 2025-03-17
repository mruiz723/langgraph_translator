# Standard Libraries
import json
import re

# Third Party Libraries
from pydantic import BaseModel, Field
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from helpers import str_to_json

class Validation(BaseModel):
    source_language: str = Field(..., description = "The Detected language") # "unknown" by default 
    target_language: str = Field(..., description = "The Target language") # "unknown" by default
    translate: bool = Field(..., description = "Whether translation is required") # False by default
    text: str = Field(..., description = "Text to be translated")

    def text_to_translate(self):
         # Patterns to match the two sentence structures
        pattern1 = r"say\s+([A-Za-z\s]+)\s+in"
        pattern2 = r"Translate\s+([A-Za-z\s]+)\s+to"

        # Try to match the first pattern
        match = re.search(pattern1, self.text)
        if match:
            given_text = match.group(1)
        else:
            # If the first pattern doesn't match, try the second pattern
            match = re.search(pattern2, self.text)
            if match:
                given_text = match.group(1)
            else:
                given_text = None
        return given_text


def parse_ai_message_to_validation(ai_message: AIMessage) -> Validation:
    """
    Parses the content of an AIMessage into a Validation Pydantic object.
    
    Args:
        ai_message (AIMessage): The AIMessage containing structured data in its content.
        
    Returns:
        Validation: A Pydantic model populated with the parsed data.
    """
    
    # Extract content from AIMessage
    content = ai_message.content

    # JSON data
    data = str_to_json(content)

    # Create the Validation model using extracted data
    validation_response = Validation(
        source_language=data.get("source_language", "unknown"),
        target_language=data.get("target_language", "unknown"),
        translate = data.get("translate", False) in ["true", "True", True],
        text=data.get("text", "")
    )

    return validation_response