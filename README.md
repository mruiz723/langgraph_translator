# langgraph-translator
AI agent that takes a given input, translates it into any language, and formats the output as XML.

### 🛠️ Setup Instructions

### 1️⃣ **System Dependencies**

### 2️⃣ **Python Version Management (Recommended)**

Using `pyenv` is highly recommended for managing Python versions.

*   **Install pyenv:** Follow the instructions on the pyenv GitHub page: [https://github.com/pyenv/pyenv](https://github.com/pyenv/pyenv)
*   **Install Python 3.12.x:**
    ```bash
    pyenv install 3.12.7  # Or your preferred 3.12.x version
    ```
*   **Set Local Python Version:**
    ```bash
    pyenv local 3.12.7
    pyenv rehash  # Important!
    ```

### 3️⃣ **Clone the Repository**

```bash
git clone git@github.com:mruiz723/event_crowd_management_assistant.git
cd event_crowd_management_assistant
```

### 4️⃣ **Activate the Virtual Environment**

Ensure Python 3.12 is selected (see above)

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate  # Windows
```

### 6️⃣ **Install Dependencies**  
```bash
pip install -r requirements.txt
```

### 7️⃣ **Set Up OpenAI API Key**

Create a .env file in the project root directory and add your API key:

```bash
OPENAI_API_KEY=your_api_key_here
```

### 8️⃣ **Run the Application**

Open `langgraph_translator.ipynb` in VS Code or Jupyter Lab.  

Make sure the correct Python interpreter (from your virtual environment) is selected in VS Code.

