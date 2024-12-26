# QA Bot - Streamlit Application

## Overview

The QA Bot is a question-answering web application built with **LangChain** and **Streamlit**, integrating Google Generative AI (Gemini) to provide intelligent responses based on user input. This application allows users to interact with a chatbot by entering questions and receiving real-time answers.

### Features
- Interactive web interface powered by **Streamlit**.
- Backend powered by **LangChain** integration with Google Gemini (Generative AI) model.
- Seamless environment configuration using **dotenv** for API key management.

## Prerequisites

Before running the application, make sure you have the following:

- Python 3.8+
- Streamlit
- LangChain (with Google Generative AI integration)
- dotenv

### Install Dependencies

You can install the necessary dependencies via `pip`. First, ensure you have the required libraries by running the following command:
### requirements.txt
langchain-groq
langchain-google-genai
streamlit
python-dotenv
openai
###Project Structure
├── .env                  
├── app.py                
├── requirements.txt      
└── README.md             
# Blog Generation App - Streamlit Application

## Overview

The Blog Generation App is a Streamlit-based web application that allows users to generate blog posts based on a given topic. The app utilizes **LangChain** and **Groq** for generating content, with the ability to customize the blog's style and word count.

### Features
- Interactive web interface powered by **Streamlit**.
- Integration with **LangChain** and **Groq** for content generation.
- Customizable blog generation with parameters such as topic, style, and word count.

### Prerequisites

Before running the application, make sure you have the following:

- Python 3.8+
- Streamlit
- LangChain
- Groq API key
- dotenv (for managing API keys securely)

### Install Dependencies

To install the required dependencies, use the following command:
###requirements.txt
langchain-groq
streamlit
python-dotenv
### Project Structure
├── .env                  
├── app.py               
├── requirements.txt     
└── README.md 

### How it Works
User Input: The user provides the blog topic, desired word count, and target audience (e.g., researchers, data scientists, or common people).
Blog Generation: The app uses LangChain and Groq to generate a blog post based on the input.
Display Output: The generated blog content is displayed on the web page.
# Cricket Knowledge Base with Vector Search and Google Generative AI

## Overview

This application utilizes **Google Generative AI (Gemini)** and **Cassandra** for building a knowledge base around cricket. The application processes a PDF document, splits it into chunks, stores the chunks in a Cassandra vector store, and allows querying against it. The queries are answered using a combination of **Google Generative AI** and similarity search techniques.

### Features
- **PDF Processing**: Extracts text from a cricket-related PDF and processes it.
- **Text Splitting**: Splits extracted text into manageable chunks using **CharacterTextSplitter**.
- **Cassandra Integration**: Uses **Cassandra** as a vector store to store text chunks and supports efficient querying.
- **Google Generative AI**: Uses the **Gemini** model for answering questions based on the knowledge base.
- **Interactive Querying**: Allows users to ask both default and custom questions, retrieving relevant documents and answers.

## Prerequisites

Before running the application, ensure that you have the following:

- Python 3.8+
- Required Python libraries (listed in `requirements.txt`)
- **Cassandra DB** (ASTRA DB) credentials: `ASTRA_DB_APPLICATION_TOKEN` and `ASTRA_DB_ID`
- **Google API Key** for Google Generative AI (Gemini)



### requirements.txt includes

langchain
langchain-google-genai
langchain_community
PyPDF2
cassio

### Environment Setup

To connect to ASTRA DB (Cassandra), you need to set up the following environment variables:

ASTRA_DB_APPLICATION_TOKEN: Your Astra DB application token.
ASTRA_DB_ID: Your Astra DB instance ID.

### Project Structure
├── .env                 
├── app.py                
├── requirements.txt      
└── README.md    

###  How it Works
text from each page.
Text Splitting: The extracted text is split into manageable chunks using CharacterTextSplitter.
Vector Store: The text chunks are stored in a Cassandra vector store for efficient similarity search.
Querying: When a query is made, the application uses Google Generative AI (Gemini) to generate an answer. It also performs a similarity search to retrieve the most relevant documents from the vector store.
Interactive Querying: After the default questions, users can ask custom queries. The system responds with relevant documents and answers.

# LangSmith-Powered Chatbot for Contextual Question Answering

## Overview

This project demonstrates how to integrate **LangSmith** with **Google Generative AI (Gemini)** for contextual question answering. Using **LangChain**, **Cassandra**, and **Google Generative AI**, this chatbot application answers user queries based on a given context, offering intelligent responses with precision and efficiency.

The system is powered by LangChain's **LangSmith** integration for enhanced traceability and powerful API endpoints. LangSmith provides end-to-end insights into model workflows, helping track, manage, and optimize large language model (LLM) interactions.

### Features

- **LangSmith Integration**: Trace and optimize your LangChain workflows with LangSmith for easy debugging, insights, and monitoring.
- **Contextual Question Answering**: A chatbot capable of answering questions based on a predefined context.
- **Google Generative AI (Gemini)**: Uses **Google’s Gemini model** for generating responses to questions.
- **Vector Store**: Uses **Cassandra** as the vector store for storing and querying documents.
- **PDF Processing**: Process and extract text from PDFs using **PyPDF2** and split it into chunks for efficient querying.
- **Environment Configuration**: Easy setup using **dotenv** to load API keys and configuration settings.

## Prerequisites

Before running the application, ensure that you have the following:

- Python 3.8+
- Required Python libraries (listed in `requirements.txt`)
- **Google API Key** for Google Generative AI (Gemini)
- **LangChain API Key** for LangSmith integration
- **Cassandra Database** (ASTRA DB) for vector storage

### Environment Setup
Google API Key: Set up your Google API Key for Google Generative AI (Gemini).
LangChain API Key: Set up your LangChain API Key for LangSmith.
Cassandra DB Credentials: Set up your ASTRA DB application token and instance ID.
Create a .env file in the project directory with the following environment variables

### Project Structure 

├── .env                  
├── app.py                
├── requirements.txt     
└── README.md            

### How it works

Environment Setup: All the necessary API keys (Google API, LangChain, Cassandra) are loaded from environment variables, allowing you to securely manage credentials.
Contextual Question Answering:
The user asks a question (question), and the context is provided (context).
A LangChain PromptTemplate is used to generate a prompt for the Google Generative AI model, with the question and context as inputs.
LangSmith traces the workflow of the query to ensure accurate, repeatable results and traceability of model calls.
Google Generative AI (Gemini): Uses Google's Gemini-1.5-pro model to process the input and generate an answer based on the context.
Vector Store and Indexing: The application utilizes Cassandra as the vector store for managing text chunks, and relevant documents are retrieved based on similarity search.
LangSmith:
LangSmith provides end-to-end visibility of the workflow, helping to monitor and optimize the flow of data between the prompt generation and model inference.
With LangSmith's tracing, you can track how the context and question evolve through the pipeline and get insights into any errors or inefficiencies.


# LangGraph-Powered Conversational Workflow with External Tools

## Overview

This project demonstrates how to integrate **LangGraph** with **LangChain** and **Google Generative AI (Gemini)** to create an advanced conversational AI system. By leveraging **LangGraph**'s stateful workflows and **LangChain**'s language models, this system is designed to handle dynamic decision-making and tool usage based on user input.

The workflow dynamically routes messages through various processing steps, where external tools are invoked based on conditions, such as querying weather information. **LangGraph** helps orchestrate this flow with a state machine that can interact with both the LLM and external tools.

### Features

- **LangGraph Workflow**: Use **LangGraph** to build stateful workflows that dynamically route the flow of conversation based on message content.
- **LLM Integration**: Connect with **Google Generative AI (Gemini)** to generate responses based on user input.
- **External Tools Integration**: Define and use external tools (e.g., querying weather) within the conversation flow.
- **Conditional Routing**: Route the conversation dynamically to different workflow nodes (LLM or tool-based processing) based on the message content.

## Prerequisites

Before running the application, ensure that you have the following:

- Python 3.8+
- Required Python libraries (listed in `requirements.txt`)
- **Google API Key** for Google Generative AI (Gemini)
- **LangChain API Key** for LangChain integration

### Environment Setup
Google API Key: Set up your Google API Key for Google Generative AI (Gemini).
LangChain API Key: Set up your LangChain API Key for interacting with LangChain models

### Project Structure

├── .env                 
├── app.py                
├── requirements.txt      
└── README.md             
### How it Works

LangGraph State Machine
The core of this project is built around LangGraph's StateGraph. This allows the creation of workflows where each step in the process is represented as a node in the state machine. The flow between these nodes is controlled based on the user’s input, enabling dynamic and responsive interactions.

LLM Integration: At the "agent" node, the system invokes Google Generative AI (Gemini) to generate a response based on the user's message.
Tool Invocation: If the user query requires external processing (e.g., asking for weather information), the workflow routes to the "tools" node, where a predefined tool is invoked.
Dynamic Routing: The router_function inspects the message for tool calls and decides the next step (either invoking an external tool or ending the flow).


