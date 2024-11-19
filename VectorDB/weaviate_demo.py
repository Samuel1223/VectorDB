import weaviate
import time

def create_client():
    """Create and connect to the Weaviate client."""
    try:
        client = weaviate.Client(
            url="http://localhost:8080"
        )
        # Test the connection
        if client.is_ready():
            print("Successfully connected to Weaviate!")
        else:
            print("Weaviate is not ready yet.")
        return client
    except Exception as e:
        print(f"Error connecting to Weaviate: {e}")
        raise

def setup_collection(client):
    """Set up the 'Article' collection, deleting it first if it exists."""
    try:
        # Define the schema for the Article class
        schema = {
            "classes": [
                {
                    "class": "Article",
                    "description": "A news article about technology",
                    "vectorizer": "text2vec-transformers",
                    "properties": [
                        {
                            "name": "title",
                            "dataType": ["string"],
                            "description": "Title of the article"
                        },
                        {
                            "name": "content",
                            "dataType": ["text"],
                            "description": "Content of the article"
                        }
                    ]
                }
            ]
        }

        # Delete the existing Article class if it exists
        if client.schema.contains({"class": "Article"}):
            client.schema.delete_class("Article")
            print("Deleted existing Article collection.")
            time.sleep(2)  # Wait for deletion to complete

        # Add the new schema
        client.schema.create(schema)
        print("Collection created successfully!")
    except Exception as e:
        print(f"Error setting up collection: {e}")
        raise

def add_sample_data(client):
    """Add sample articles to the 'Article' collection."""
    try:
        articles = [
            {
                "title": "Python Programming",
                "content": "Python is a high-level programming language known for its simplicity and readability. It's great for beginners and professionals alike."
            },
            {
                "title": "Machine Learning Basics",
                "content": "Machine learning is a subset of AI that enables systems to learn from data. It's revolutionizing many industries."
            },
            {
                "title": "Data Science Overview",
                "content": "Data science combines statistics, programming, and domain expertise to extract meaningful insights from data."
            },
            {
                "title": "Artificial Intelligence Introduction",
                "content": "AI is the simulation of human intelligence by machines. It includes machine learning, natural language processing, and more."
            }
        ]

        for article in articles:
            client.data_object.create(
                data_object=article,
                class_name="Article"
            )
        print("Sample data added successfully!")
    except Exception as e:
        print(f"Error adding sample data: {e}")
        raise

def verify_collection(client):
    """Verify the contents of the 'Article' collection."""
    try:
        results = client.query.get("Article", ["title", "content"]).with_limit(10).do()

        print("\nCurrent articles in collection:")
        articles = results.get('data', {}).get('Get', {}).get('Article', [])
        if articles:
            for article in articles:
                print(f"\nTitle: {article.get('title')}")
                content_preview = article.get('content', '')[:100]
                print(f"Content: {content_preview}...")
        else:
            print("No articles found.")
    except Exception as e:
        print(f"Verification error: {e}")

def search_articles(client, query):
    """Search articles using semantic (near-text) search."""
    try:
        results = client.query.get("Article", ["title", "content"])\
            .with_near_text({
                "concepts": [query]
            })\
            .with_limit(2)\
            .do()

        print(f"\nSearch results for: '{query}'")
        articles = results.get('data', {}).get('Get', {}).get('Article', [])
        if articles:
            for article in articles:
                print(f"\nTitle: {article.get('title')}")
                content_preview = article.get('content', '')[:200]
                print(f"Content: {content_preview}...")
        else:
            print("No results found.")
    except Exception as e:
        print(f"Search error: {e}")
        print("Full error details:", str(e))

def interactive_search(client):
    """Interactive search interface."""
    print("\nEnter your search queries (type 'quit' to exit)")
    while True:
        query = input("\nSearch query: ").strip()
        if query.lower() == 'quit':
            break
        if query:
            search_articles(client, query)
        else:
            print("Please enter a valid query.")

def main():
    try:
        # Create and connect the client
        client = create_client()

        # Set up the collection and add data
        setup_collection(client)
        add_sample_data(client)

        # Verify the collection contents
        print("\nVerifying collection contents...")
        verify_collection(client)

        # Run some example searches
        print("\nRunning example searches...")
        example_queries = [
            "What is Python used for?",
            "Explain machine learning",
            "How does data science work?"
        ]

        for query in example_queries:
            search_articles(client, query)

        # Start interactive search
        print("\nStarting interactive search...")
        interactive_search(client)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'client' in locals():
            client.close()
            print("\nWeaviate connection closed.")

if __name__ == "__main__":
    main()