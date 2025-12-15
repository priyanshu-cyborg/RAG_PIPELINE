from embed_store import retrieve_docs

def generate_answer(query):
    retrieved_docs = retrieve_docs(query)

    context = " ".join(retrieved_docs)

    answer = f"""
    Question: {query}
    Context: {context}
    Answer: Based on the retrieved information, {context}
    """
    return answer