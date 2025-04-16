# 💰 Financial Chatbot

## Overview
The Financial Chatbot is an interactive web application built using Streamlit that allows users to ask financial questions and receive insights powered by AI agents. The chatbot utilizes multiple AI agents to provide accurate and relevant information based on user queries.

## Features
- Interactive chatbot interface for asking financial questions.
- Integration with AI agents for web search and financial data retrieval.
- Customizable UI with CSS for better user experience.

## Requirements
- Python 3.7 or higher
- Streamlit

- Other dependencies as specified in `requirements.txt`

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory of the project and add your OpenAI API key:
   ```plaintext
  PHI_API_KEY=phi-7etjYP6BIUdedrtyuioaX14IvZqcoZNohNX7E_gSbsXRM8FrZAc #sample key
  GROQ_API_KEY=gsk_9YMajNGea0hUM3ONrtyuiopp6AnWGdyb3FYhAE0wQ2i7j0zyKFEKFepPz7B #sample key
   ```

## Usage

1. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

2. **Open your web browser and navigate to:**
   ```
   http://localhost:8501
   ```

3. **Interact with the chatbot:**
   - Enter your financial questions in the input field and press "Enter" or click the submit button.
   - The chatbot will respond with insights powered by the integrated AI agents.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.


## Acknowledgments
- [Streamlit](https://streamlit.io/) for the web framework.

- [Phi](https://phi.ai/) for the agent framework.