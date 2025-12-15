from rag_pipeline import generate_answer
while True : 
    query = input("\n Ask a question (or type exit.) : ")
    if query.lower()=="exit":
        break

    response = generate_answer(query)
    print(response)