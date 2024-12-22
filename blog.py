from langchain_groq import ChatGroq
import streamlit as st
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.prompts import PromptTemplate

# API Keys (Store securely in environment variables or a config file)
GOQ_API_KEY = "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"

from langchain_groq import ChatGroq
import streamlit as st



# Initialize LLM
llm = ChatGroq(groq_api_key=GOQ_API_KEY, model_name="Llama3-8b-8192")

# Function to Generate Blog Response
def get_response(input_text, no_words, blog_style):
    try:
        # Create the prompt template
        template = f"""
        You are a helpful assistant specialized in writing blogs. 
        Write a blog for {blog_style} on the topic "{input_text}" 
        within {no_words} words.
        """
        
        # Structure the input as messages
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": template.strip()},
        ]
        
        # Generate the response
        response = llm.invoke(messages)
        return response.content  # Use .content to access the AI's generated text
    except Exception as e:
        return f"Error generating response: {str(e)}"

# Streamlit Page Configuration
st.set_page_config(
    page_title="Generate Blog",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)
st.header("Generate Blogs 🤖")

# Blog Topic Input
input_text = st.text_input("Enter the Blog Topic")
col1, col2 = st.columns([5, 5])

# Input Fields for Blog Details
with col1:
    no_words = st.text_input("Number of Words", "500")
with col2:
    blog_style = st.selectbox(
        "Writing blog for:",
        ("Researchers", "Data Scientists", "Common People")
    )

submit = st.button("Generate")
if submit:
    if input_text.strip() and no_words.isdigit():
        response = get_response(input_text, int(no_words), blog_style)
        st.write(response)
    else:
        st.error("Please provide valid inputs for all fields.")
