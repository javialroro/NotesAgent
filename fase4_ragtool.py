from langchain.tools import BaseTool
from typing import Any, Type
from pydantic import BaseModel, Field, PrivateAttr
import chromadb
from chromadb.config import Settings
from openai import OpenAI
import os

# ======== MODELO DE INPUT ========
class RAGInput(BaseModel):
    query: str = Field(..., description="Pregunta o frase a buscar en los apuntes")

# ======== TOOL ========
class RAGTool(BaseTool):
    name: str = "RAG_Tool"
    description: str = "Busca información en la base vectorial local de apuntes de Inteligencia Artificial"
    args_schema: Type[BaseModel] = RAGInput

    _client: Any = PrivateAttr()
    _collection: Any = PrivateAttr()
    _oai_client: Any = PrivateAttr()

    def __init__(self, collection_name: str, persist_dir: str, **kwargs):
        super().__init__(**kwargs)
        self._client = chromadb.PersistentClient(path=persist_dir, settings=Settings(is_persistent=True))
        self._collection = self._client.get_collection(collection_name)
        self._oai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def _run(self, query: str):
        """Consulta la base vectorial usando embeddings OpenAI"""
        embedding = self._oai_client.embeddings.create(
            model="text-embedding-3-small",
            input=query
        ).data[0].embedding

        results = self._collection.query(
            query_embeddings=[embedding],
            n_results=5,
            include=["documents",  "distances", "metadatas"]
        )
        docs = results["documents"][0]
        metas = results["metadatas"][0]

        combined = [
            f"Documento: {m.get('filename_base','')} | Fragmento: {d[:600]}..."
            for d, m in zip(docs, metas)
        ]
        return "\n".join(combined)

    async def _arun(self, query: str):
        raise NotImplementedError("RAGTool no soporta ejecución asíncrona.")
