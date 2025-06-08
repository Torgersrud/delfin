import chromadb
import csv

chroma_client = chromadb.PersistentClient(path="./chroma_db")  # Save database to ./chroma_db folder
collection = chroma_client.get_or_create_collection(name="quotes")

def add_laws(file_path): # Function to add laws from a CSV file to the ChromaDB collection, without duplicates
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        next(reader) # Skip the header row

        ids = []
        documents = []
        id_set = []

        try:
            id_set = collection.get()["ids"] # Get existing IDs in the collection
            print(id_set)
        except:
            print("No previous embeds in collection")

        for n, row in enumerate(reader):
            if f"ID{n}" in id_set:
                continue # Skip if ID already exists in the collection


            ids.append(f"ID{n}")
            documents.append(row[1])
            print(n)
        if len(documents) == 0:
            print("No new data to add to collection.")
            return
        
        print("Data formatted, going on to add to collection..")
        collection.add(
            documents=documents, 
            ids=ids,
        )
        print("Data added to collection..")
        
        
def get_rag(query : str):
    #print(quote)
    result = collection.query(query_texts=query, n_results=1)
    result_formatted = (f"{result['documents'][0][0]}")
    return result_formatted

