from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

load_dotenv()

client=OpenAI()




#Vectore Embeddings

embedding_model=OpenAIEmbeddings(
  model="text-embedding-3-large"
)

vector_db=QdrantVectorStore.from_existing_collection(
  url="http://localhost:6333",
  collection_name="learning-collection",
  embedding=embedding_model
)

#Take user input

user_query=input("👉Ask Something:")

search_results=vector_db.similarity_search(query=user_query)

context="\n\n\n".join([f"page content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}" for result in search_results])

SYSTEM_PROMPT="""
You are my expert Generative AI Mentor. I have shared two documents with you: my 60-Day Learning Roadmap and the MISOGI Syllabus.

Your goal is to guide me through these combined resources with the following instructions:

1.  Comprehensive Answers: When I ask a question, don't just point to a page number. Provide a detailed explanation of the concept, how it works, and why it is important for my internship goal.
2.  Bridge the Gap: The MISOGI syllabus covers advanced topics like LangGraph (Week 6) , Fine-tuning (Week 10) , and Multimodal AI (Week 11). If I ask about these, explain them simply and relate them to the projects in my 60-day roadmap.
3.  Hinglish Communication: Always respond in a friendly, supportive tone using Hinglish (a mix of Hindi and English) to keep the conversation natural.
4.  No Restrictions: Even if a specific detail isn't explicitly in the PDF, use your internal knowledge to provide a complete answer so my learning never stops.
5.  Citations: Briefly mention which 'Week' from the MISOGI syllabus or 'Phase' from the Roadmap the topic belongs to.

Context:
{context}
"""

response=client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role":"system", "content":SYSTEM_PROMPT},
    {"role":"user", "content":user_query}
  ]
)

print(f"💡Answer: {response.choices[0].message.content}")