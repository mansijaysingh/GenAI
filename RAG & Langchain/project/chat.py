from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

client=OpenAI()

load_dotenv()


#Vectore Embeddings

embedding_model=OpenAIEmbeddings(
  model="text-embedding-3-large"
)

vector_db=QdrantVectorStore.from_existing_collection(
  url="http://localhost:6333",
  collection_name="learning-Rag",
  embedding=embedding_model
)

#Take user input

user_query=input("👉Ask Something:")

search_results=vector_db.similarity_search(query=user_query)

context="\n\n\n".join([f"page content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}" for result in search_results])

SYSTEM_PROMPT="""
You are a helpful assistant for answering questions based on the following context retrieved from a PDF file along with page_contents and page number.

You should only answer the user based on the following context and navigate the user to open the right page number to konw more about the answer. If you don't know the answer, say you don't know. Do not make up an answer.

context:
{context}
"""

response=client.chat.completions.create(
  model="gpt-5",
  messages=[
    {"role":"system", "content":SYSTEM_PROMPT},
    {"role":"user", "content":user_query}
  ]
)

print(f"💡Answer: {response.choices[0].message.content}")