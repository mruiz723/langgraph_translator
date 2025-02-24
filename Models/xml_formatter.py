from Models.state import State
import xml.etree.ElementTree as ET
from xml.dom import minidom
#from helpers import to_mardown

def to_xml(state) -> dict:
    """ convert the Translation object to XML format """
    # XML format for the translation
    translation = state.translation
    text = state.validation.text
    print(f"text: {state.validation.text}")
    # Create the XML structure
    content = ET.Element("content")
    original = ET.SubElement(content, "original")
    original.text = text
    translated = ET.SubElement(content, "translation")
    translated.text = translation.translated_text
    
    # Convert the XML structure to a string (compact format without newlines)
    xml_string = ET.tostring(content, encoding="unicode", method="xml")
    
    # Use minidom to format the XML with indentation
    xml_string_pretty = minidom.parseString(xml_string).toprettyxml(indent="    ")
    
    # Print the pretty-printed XML string
    print(xml_string_pretty)
        
    str_format = f"""
        ```xml
        <content>
            <original>{text}</original>
            <translation>{translation.translated_text}</translation>
        </content>
        ```
    """
    #display(to_markdown(str_format))
    #display(to_markdown(xml_string_pretty))
    # Return a dictionary instead of a string
    return {
        "content": {
            "original": text,
            "translation": translation.translated_text
        }
    } 
    