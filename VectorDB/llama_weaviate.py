import weaviate
from weaviate.classes import Configure

# Initialize client with Llama configuration
client = weaviate.WeaviateClient(
    connection_params=weaviate.connect.ConnectionParams.from_url(
        url="http://localhost:8080"
    )
)

# Define schema with Llama configuration
schema = {
    "classes": [
        {
            "class": "Document",
            "description": "A document class with Llama embeddings",
            "vectorizer": "llama",  # Specify Llama as vectorizer
            "moduleConfig": {
                "llama": {
                    "model": "meta-llama/Llama-2-7b",
                    "modelDimension": 4096,
                    "pooling": "masked_mean"
                }
            },
            "properties": [
                {
                    "name": "title",
                    "dataType": ["string"],
                    "description": "The title of the document"
                },
                {
                    "name": "content",
                    "dataType": ["text"],
                    "description": "The content of the document",
                    "moduleConfig": {
                        "llama": {
                            "vectorizePropertyName": True
                        }
                    }
                }
            ],
        }
    ]
}

def setup_schema():
    """Create the schema in Weaviate"""
    try:
        client.schema.create(schema)
        print("Schema created successfully")
    except Exception as e:
        print(f"Error creating schema: {e}")

def add_documents(documents):
    """Add documents to Weaviate"""
    try:
        for doc in documents:
            client.data.creator()\
                .with_class_name("Document")\
                .with_properties(doc)\
                .do()
        print("Documents added successfully")
    except Exception as e:
        print(f"Error adding documents: {e}")

def semantic_search(query, limit=3):
    """Perform semantic search using Llama"""
    try:
        response = client.query.get(
            "Document", 
            ["title", "content"]
        ).with_near_text({
            "concepts": [query]
        }).with_limit(limit).do()
        
        print(f"\nSearch results for: '{query}'")
        for item in response.objects:
            print(f"\nTitle: {item.properties['title']}")
            print(f"Content: {item.properties['content'][:200]}...")  # Show first 200 chars
        
        return response.objects
    except Exception as e:
        print(f"Error during search: {e}")
        return []

def main():
    # Sample documents
    documents = [
        {
            "title": "Introduction to AI",
            "content": "Artificial Intelligence (AI) is the simulation of human intelligence by machines..."
        },
        {
            "title": "Machine Learning Basics",
            "content": "Machine Learning is a subset of AI that focuses on training models to learn from data..."
        },
        {
            "title": "Deep Learning Overview",
            "content": "Deep Learning is a type of machine learning based on artificial neural networks..."
        }
    ]

    # Setup and populate database
    setup_schema()
    add_documents(documents)

    # Perform searches
    queries = [
        "What is artificial intelligence?",
        "Explain machine learning concepts",
        "How do neural networks work?"
    ]

    for query in queries:
        semantic_search(query)

if __name__ == "__main__":
    main()