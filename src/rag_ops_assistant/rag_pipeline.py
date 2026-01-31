import os
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


class RAGOpsAssistant:
    """
    Retrieval-Augmented Assistant for Transaction Banking Operations.
    Read-only decision support for human operators.
    """

    def __init__(self, docs_path: str):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.documents = []
        self.doc_sources = []

        for file in os.listdir(docs_path):
            with open(os.path.join(docs_path, file), "r") as f:
                self.documents.append(f.read())
                self.doc_sources.append(file)

        embeddings = self.model.encode(self.documents)
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(np.array(embeddings))

    def query(self, question: str) -> dict:
        """
        Retrieve the most relevant operational document for a query.
        """
        query_embedding = self.model.encode([question])
        _, idx = self.index.search(np.array(query_embedding), k=1)

        return {
            "query": question,
            "source_document": self.doc_sources[idx[0][0]],
            "retrieved_text": self.documents[idx[0][0]]
        }


if __name__ == "__main__":
    assistant = RAGOpsAssistant("data/ops_knowledge")

    response = assistant.query("How should I handle a delayed payment?")
    print("=== OPS ASSISTANT RESPONSE ===")
    print(f"Source: {response['source_document']}")
    print(response["retrieved_text"])
