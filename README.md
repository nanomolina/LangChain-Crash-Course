# LangChain Project - Setup Instructions

### Prerequisites

Ensure you have Python and pip installed on your machine.

### Installation

1. Clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/langchain-project.git
cd langchain-project
```
2. Install the required dependencies using the provided requirements.txt file:
```bash
pip install -r requirements.txt
```
3. Set up the necessary environment variables, including your OpenAI API key. You can do this by creating a file named .env in the project directory and adding the following line:
```bash
OPENAI_API_KEY=your_openai_api_key
```
  Replace your_openai_api_key with your actual OpenAI API key.

### Running the Application

To run the application locally, use the following command:

```bash
streamlit run app.py
```
This command will launch the Streamlit application, and you can access it through your web browser at http://localhost:8501.

### Usage

1. Enter a topic in the provided text input.
2. LangChain will generate a YouTube title, perform Wikipedia research on the topic, and generate a corresponding video script.
3. The generated title, script, and memory history will be displayed in the Streamlit interface.

Feel free to experiment with different prompts and observe how LangChain dynamically adapts to user input, creating engaging and context-aware content. Contributions and feedback are welcome!
