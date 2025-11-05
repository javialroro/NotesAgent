from langchain_core.tools import Tool
from langchain_tavily import TavilySearch

#funcion para obtener la herramienta de busqueda web
def get_websearch_tool():
    search = TavilySearch(max_results=5)
    return Tool(
        name="WebSearch_Tool",
        description="Busca información en Internet usando Tavily",
        func=search.run
    )
