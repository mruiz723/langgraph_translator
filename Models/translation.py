# Standard Libraries
import json
import re

# Third Party Libraries
from pydantic import BaseModel, Field
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage

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

    # Regular expression to capture key-value pairs
    pattern = r"given_text:\s*([A-Za-z\s]+)\ntranslated_text:\s*([A-Za-z\s]+)"

    # Find all matches using regex
    matches = re.findall(pattern, content)
    
    if matches:
        given_text, translated_text = matches[0]
    else:
         given_text, translated_text = "", ""
    
    
    # Create the Validation model using extracted data
    translation_response = Translation(
        given_text=given_text,
        translated_text=translated_text,
    )

    return translation_response