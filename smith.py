from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import Cassandra
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import cassio
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

os.environ['GOOGLE_API_KEY'] = os.getenv("GOOGLE_API_KEY")
LANGCHAIN_TRACING_V2="true"
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY="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"
LANGCHAIN_PROJECT="pr-enchanted-casserole-97"

# Define prompt
from langchain.prompts.chat import ChatPromptTemplate  
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user message only based on the given context."),
        ("user", "question:{question}\nContext:{context}")
    ]
)

# Sample inputs
question = "Can you summarize the speech?"
context = """There are a lot of things that I love about Hyderabad. But before I say anything, thanks for coming here. 
It’s a real pleasure sharing the stage with you. We are big fans of your work. So, thanks for coming. The moment you 
talk about Hyderabad, you know, biryani is the first thing that people talk about. And, when I started playing cricket, 
when I was playing first-class cricket, I think it was 2000 and we had a game over here. So, that was my first 
introduction to the Hyderabadi biryani. And after that, whenever we have come here, biryani is something that’s, we 
can’t really miss. Of course, we come here for cricket, but Biryani is something that we can’t miss along with the 
food. I feel the cuisine over here is great. Uh, another thing that I like is the biscuits, the bakery biscuits from 
here, they are fantastic. And along with it, it has its own specialties, the bangles for the ladies. So, I picked a 
few for my wife. But, also we have got very good support over here. As an Indian cricket team, whenever we come here, 
the people, they come out, they support us, and we have got a very good record in Hyderabad. You know, we have done 
very well as a cricket team, so it feels good to be here. It’s a pleasure being here. Thanks to all of you, you know, 
for coming over here and giving me a very warm reception."""

# Define the LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0.5,
    max_tokens=150,
    timeout=None,
    max_retries=2,
)

# Define the chain
chain = prompt | llm

# Run the chain
output = chain.invoke({"question": question, "context": context})
print(output)

