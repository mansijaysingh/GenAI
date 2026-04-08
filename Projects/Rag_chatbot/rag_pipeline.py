from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI

def create_rag_pipeline(file_path):
	#Load PDF
	loader=PyPDFLoader(file_path)
	documents=loader.load()
	
  #Chunking
	splitter=RecursiveCharacterTextSplitter(
		chunk_size=500,
		chunk_overlap=50
  )
	docs=splitter.split_documents(documents)
	
  #Embeddings
	embeddings=OpenAIEmbeddings()
  
  #Vector db
	db=FAISS.from_documents(docs,embeddings)
	return db
  

def ask_questions(db, query):
	#Retrieval
	docs=db.similarity_search(query,k=3)
	context="\n".join([doc.page_content for doc in docs])
	
  #LLM
	llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
	response=llm.invoke(f"Answer based on this: \n{context}\n\nQuestion: {query}")
	return response.content
