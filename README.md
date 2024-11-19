# VectorDB

VectorDB is a project that demonstrates the use of Weaviate, a vector search engine, to manage and search through a collection of articles. This project includes setting up a Weaviate instance, adding sample data, and performing semantic searches.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- **Docker**: Ensure Docker is installed and running on your machine. You can download it from [Docker's official website](https://www.docker.com/products/docker-desktop).
- **Python 3.8+**: Make sure Python is installed. You can download it from [Python's official website](https://www.python.org/downloads/).

### Setup

1. **Clone the Repository**

   Clone this repository to your local machine using:

   ```bash
   git clone git@github.com:Samuel1223/VectorDB.git
   cd VectorDB
   ```

2. **Start Docker Containers**

   Use Docker Compose to start the Weaviate and Transformer services:

   ```bash
   docker-compose up -d
   ```

   This command will start the services in detached mode.

3. **Install Python Dependencies**

   Create a virtual environment and install the required Python packages:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

1. **Ensure Docker Containers Are Running**

   Verify that the Weaviate and Transformer services are running:

   ```bash
   docker-compose ps
   ```

   You should see both services listed as "Up".

2. **Run the Python Script**

   Execute the main script to set up the collection, add data, and perform searches:

   ```bash
   python weaviate_demo.py
   ```

   This script will:
   - Connect to the Weaviate instance
   - Set up the "Article" collection
   - Add sample articles
   - Perform example searches
   - Allow interactive searches

3. **Interactive Search**

   After running the script, you can enter your own search queries. Type `quit` to exit the interactive search mode.

## Project Structure

- **docker-compose.yml**: Configuration file for Docker Compose to set up Weaviate and Transformer services.
- **weaviate_demo.py**: Main script to interact with Weaviate, including setting up collections and performing searches.
- **llama_weaviate.py**: Additional script for managing Weaviate interactions (if applicable).
- **data/**: Directory for storing any data files (if needed).
- **README.md**: This file, providing an overview and instructions for the project.

## Contributing

Contributions are welcome! Please fork the repository and use a feature branch. Pull requests are warmly welcome.
