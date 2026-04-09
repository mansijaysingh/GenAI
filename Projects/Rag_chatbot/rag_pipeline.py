from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

embeddings=OpenAIEmbeddings(
	api_key=os.getenv("OPENAI_API_KEY")
)


def create_rag_pipeline(file_path):
	db_path="faiss_db"

	if os.path.exists(db_path):
		db=FAISS.load_local(
			db_path,
			embeddings,
			allow_dangerous_deserialization=True
		)
		return db
	
	loader=PyPDFLoader(file_path)
	documents=loader.load()
	print("total documents:", len(documents))
	splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
	docs=splitter.split_documents(documents)
	print("total chunks:", len(docs))
	db=FAISS.from_documents(docs,embeddings)
	
	db.save_local(db_path)

	return db



# def create_rag_pipeline(file_path):
# 	#Load PDF
# 	loader=PyPDFLoader(file_path)
# 	documents=loader.load()
	
#   #Chunking
# 	splitter=RecursiveCharacterTextSplitter(
# 		chunk_size=500,
# 		chunk_overlap=50
#   )
# 	docs=splitter.split_documents(documents)
	
#   #Embeddings
# 	embeddings=OpenAIEmbeddings()
  
#   #Vector db
# 	db=FAISS.from_documents(docs,embeddings)
# 	return db
  

# def ask_questions(db, query):
# 	#Retrieval
# 	docs=db.similarity_search(query,k=3)
# 	context="\n".join([doc.page_content for doc in docs])
	
#   #LLM
# 	llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
# 	response=llm.invoke(f"Answer based on this: \n{context}\n\nQuestion: {query}")
# 	return response.content




def ask_question(db, query):
    docs = db.similarity_search(query, k=3)

    print("RETRIEVED DOCS:", len(docs))

    for d in docs:
        print("----")
        print(d.page_content[:200])

    context = "\n".join([doc.page_content for doc in docs])

    if not context.strip():
        return "PDF se context nahi mil raha 😅"

    prompt = f"""
    Answer ONLY from this context:

    {context}

    Question: {query}
    """

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=os.getenv("OPENAI_API_KEY")
    )

    response = llm.invoke(prompt)

    return response.content