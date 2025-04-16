import streamlit as st
import os
from dotenv import load_dotenv
from financial_agent import multi_ai_agent

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Set up the page configuration
st.set_page_config(
    page_title="💰 Financial Chatbot",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject custom CSS to adjust the chat input's position and styling
st.markdown("""
    <style>
    /* Position the chat input at the top */
    .chat-input-container {
        position: fixed;
        top: 80px; /* Adjust this value as needed */
        left: 50%;
        transform: translateX(-50%);
        width: 50%; /* Reduce the width */
        z-index: 9999;
    }
    /* Style the chat input field */
    .chat-input-container input {
        height: 60px; /* Increase the height */
        font-size: 1.2em;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar content
with st.sidebar:
    st.title("Financial Chatbot")
    
    selected_page = st.radio("section:", ["Home"])
   
# Main content area
st.title("💰 Interactive Financial Chatbot")
st.markdown("Ask financial questions and receive insights powered by AI agents.")

# Create a container for the chat input at the top
chat_input_container = st.container()
with chat_input_container:
    # Create a placeholder for the chat input
    st.markdown('<div class="chat-input-container">', unsafe_allow_html=True)
    user_input = st.text_input("📤 Enter your question here:")
    st.markdown('</div>', unsafe_allow_html=True)

# Handle user input
if user_input:
    run_response = multi_ai_agent.run(user_input, stream=True)
    full_response = ""
   
    response_placeholder = st.empty()
    for chunk in run_response:
        # Extract text from the chunk
        chunk_text = getattr(chunk, "content", str(chunk))  # fallback to str(chunk) if no `.content`
        full_response += chunk_text
        response_placeholder.markdown(full_response)
