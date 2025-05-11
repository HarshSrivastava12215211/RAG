from retrieval import retrieve_top_chunks
from transformers import pipeline

qa_model = pipeline("text-generation", model="gpt2") 

def rag_pipeline(query: str) -> str:
    context_chunks = retrieve_top_chunks(query)
    context = "\n".join(context_chunks)
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
    response = qa_model(prompt, max_new_tokens=100, do_sample=True)[0]['generated_text']
    return response
