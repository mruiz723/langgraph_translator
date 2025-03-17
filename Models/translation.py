# Standard Libraries
import json
import re

# Third Party Libraries
from pydantic import BaseModel, Field
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from helpers import str_to_json

class Translation(BaseModel):
    given_text: str = Field(..., description = "Text to be translated")
    translated_text: str = Field(..., description= "Text translated")

def parse_ai_message_to_translation(ai_message: AIMessage) -> Translation:
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
    
    # Create the Translation model using extracted data
    translation_response = Translation(
        given_text=data.get("given_text"),
        translated_text=data.get("translated_text")
    )

    return translation_response