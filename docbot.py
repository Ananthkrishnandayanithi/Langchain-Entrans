from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import Cassandra
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import cassio

# Constants
ASTRA_DB_APPLICATION_TOKEN = "AstraCS:YoACtXAGhPAsFHhMWCBnlrwk:8cdb274b2bfaa507c0dbdcde91af15cd53dc6f181f1f978ea8bc10b8b2886278"
ASTRA_DB_ID = "4d40dbe3-b826-4f58-9c58-b5c04e9da969"
# Initialize the Cassandra DB
ASTRA_DB_APPLICATION_TOKEN = "AstraCS:YoACtXAGhPAsFHhMWCBnlrwk:8cdb274b2bfaa507c0dbdcde91af15cd53dc6f181f1f978ea8bc10b8b2886278"
cassio.init(token=ASTRA_DB_APPLICATION_TOKEN, database_id=ASTRA_DB_ID)

# Initialize Google Generative AI (Gemini)
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# Initialize Embeddings
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Initialize Cassandra Vector Store
astra_vector = Cassandra(
    embedding=embeddings,
    table_name="qa_mini_demo",
    session=None,  # Automatically handled by cassio
    keyspace=None,  # Automatically handled by cassio
)

# Read and Process PDF
pdf_reader = PdfReader('Cricket.pdf')
raw_text = ''
for i, page in enumerate(pdf_reader.pages):
    content = page.extract_text()
    if content:
        raw_text += content

# Split Text into Chunks
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=800,
    chunk_overlap=200,
    length_function=len,
)
texts = text_splitter.split_text(raw_text)

# Add Texts to Vector Store
astra_vector.add_texts(texts[:50])

# Wrap the Vector Store in an Index
astra_vector_index = VectorStoreIndexWrapper(vectorstore=astra_vector)

# Default Questions
default_questions = [
    "What is cricket?",
    "How many players are there in a cricket team?",
    "What are the rules of cricket?",
    "Who are some famous cricket players?",
]

# Ask Default Questions
for question in default_questions:
    print(f"\nQUESTION: \"{question}\"")
    try:
        # Get Answer
        answer = astra_vector_index.query(question, llm=llm).strip()
        print("\nANSWER:")
        print(answer)

        # Retrieve Relevant Documents
        print("\nTop Relevant Documents:")
        for doc, score in astra_vector.similarity_search_with_score(question, k=4):
            print(f"Document (Score: {score}):")
            print(doc.page_content)
            print("-" * 80)
    except Exception as e:
        print("An error occurred while processing your query:", e)

# After Default Questions, Allow Manual Queries
while True:
    query_text = input("\nType another question or type 'quit' to exit: ").strip()
    if query_text.lower() == "quit":
        print("Exiting the program. Goodbye!")
        break

    if query_text == "":
        continue

    try:
        print(f"\nQUESTION: \"{query_text}\"")
        answer = astra_vector_index.query(query_text, llm=llm).strip()
        print("\nANSWER:")
        print(answer)

        # Retrieve Relevant Documents
        print("\nTop Relevant Documents:")
        for doc, score in astra_vector.similarity_search_with_score(query_text, k=4):
            print(f"Document (Score: {score}):")
            print(doc.page_content)
            print("-" * 80)
    except Exception as e:
        print("An error occurred while processing your query:", e)
