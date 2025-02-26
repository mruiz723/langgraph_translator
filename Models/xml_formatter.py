from Models.state import State
import xml.etree.ElementTree as ET
from xml.dom import minidom
from helpers import to_markdown, display_message

def to_xml(state) -> dict:
    """ convert the Translation object to XML format """
    # XML format for the translation
    translation = state.translation
    text = state.validation.text
    
    if state.validation.text_to_translate() is None:
        error_message = "Please use the format: **How do you say [text] in [language]?**, or **Translate [text] to [language]**"
        display_message("Error Message", error_message)
        return
    
    # Create the XML structure
    content = ET.Element("content")
    original = ET.SubElement(content, "original")
    original.text = text
    translated = ET.SubElement(content, "translation")
    translated.text = translation.translated_text
    
    # Convert the XML structure to a string (compact format without newlines)
    xml_string = ET.tostring(content, encoding="unicode", method="xml")
    
    # Use minidom to format the XML with indentation
    xml_string_pretty = f"""
        ```xml
        {minidom.parseString(xml_string).toprettyxml(indent="    ")}
        ```
    """
    
    display(to_markdown(f"#### Formatter:\n ---"))
        
    str_format = f"""
        ```xml
        <content>
            <original>{text}</original>
            <translation>{translation.translated_text}</translation>
        </content>
        ```
    """
    display(to_markdown(str_format, code="xml"))
    display(to_markdown(xml_string_pretty, code="xml"))
    # Return a dictionary instead of a string
    return {
        "content": {
            "original": text,
            "translation": translation.translated_text
        }
    } 
    