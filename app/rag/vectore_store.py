from app.rag import Vectorizer
from app.database import db
from app.models import Chunk


class VectorStore:
    
    def __init__(self) -> None:
        self.vectorizer = Vectorizer()
        self.document_db = db

    def search(self, query: str, k=10) -> list[Chunk]:
        """
        Search nearest documents from a query. Embed the query, search for the nearest chunks
        and return the chunks

        Args:
            query (str): Query to search documents
            k (int, optional): Number of chunks to retrieve. Defaults to 5.

        Returns:
            list[Chunk]: List of document chunk
        """
        embeddings = self.vectorizer.generate_embeddings(query)

        # TODO: retrieve k nearest chunks
        chunks: list[Chunk] = []

        return chunks