# Third Party Libraries
from pydantic import BaseModel, Field
from typing import List
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from Models.validation import Validation
from Models.translation import Translation
from typing import Optional

class State(BaseModel):
    messages: List[BaseMessage] 
    validation: Optional[Validation] = None 
    translation: Optional[Translation] = None