# Standard Libraries
import re
import json

# Third Party Libraries
from IPython.display import Markdown

def to_markdown(text):
    """
    Convert text to Markdown format:
    - Replace bullet points (•) with Markdown lists (* item)
    - Preserve Python code blocks correctly
    - Add blockquote formatting to non-code text

    Args:
        text (str): Input text to format

    Returns:
        Markdown: Formatted markdown-compatible text
    """
    # Replace bullet points (•) with Markdown-compatible lists (* item)
    text = text.replace('•', '  * ')

    # Function to preserve code blocks
    def preserve_code(match):
        return f"\n```xml\n{match.group(1)}\n```\n"

    # Extract and preserve Python code blocks
    text = re.sub(r"```xml\n(.*?)\n```", preserve_code, text, flags=re.DOTALL)

    # Split text into lines for better processing
    lines = text.split("\n")
    formatted_lines = []
    inside_code_block = False

    for line in lines:
        # Detect start and end of a code block
        if line.startswith("```"):
            inside_code_block = not inside_code_block
            formatted_lines.append(line)
            continue

        # Apply blockquote formatting **only** to non-code lines
        if not inside_code_block:
            line = line.strip() # Remove leading/trailing whitespace from each line
            if line:  # Only add non-empty lines
                formatted_lines.append(f"> {line}")
        else:
            formatted_lines.append(line)

    # Join lines back into a full formatted text
    formatted_text = "\n".join(formatted_lines)
    
    return Markdown(formatted_text)
