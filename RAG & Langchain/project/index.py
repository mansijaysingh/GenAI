from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv

load_dotenv()

pdf_path=Path(__file__).parent/"MISOGI.pdf"

#Load this file in python program
loader=PyPDFLoader(file_path=pdf_path)
docs=loader.load()

# print(docs[1])

#Split the document into smaller chunks

text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)

chunks=text_splitter.split_documents(documents=docs)
# print(chunks)

#Vectore Embeddings

embedding_model=OpenAIEmbeddings(
  model="text-embedding-3-large"
)

vectore_store=QdrantVectorStore.from_documents(
  documents=chunks,
  embedding=embedding_model,
  url="http://localhost:6333",
  collection_name="learning-collection"
)

print("Indexing of documents is completed")
