import os
from collections import deque
from langchain_openai import ChatOpenAI
from agente import AGENTE_PERFIL
from fase4_ragtool import RAGTool   
from fase4_webtool import get_websearch_tool
from dotenv import load_dotenv

load_dotenv()

# Inicializar modelo principal (orquestador) 
llm_orq = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0.3)

# Inicializar las herramientas con la carpeta donde están los vectores
collection_name = "ai_apuntes_sliding_openai_v1"
persist_dir = "data/vectorstores/chroma_sliding_openai_v1"
rag_tool = RAGTool(collection_name=collection_name, persist_dir=persist_dir)
web_tool = get_websearch_tool()

# Memoria de contexto limitada
MEMORIA = deque(maxlen=6)

def formatear_contexto():
    contexto = ""
    for rol, msg in MEMORIA:
        contexto += f"[{rol.upper()}]: {msg}\n"
    return contexto.strip()

# Detección de uso de web
def usuario_pide_web(pregunta: str) -> bool:
    gatillos = ["buscar en web:", "web:", "internet:", "tavily:",
                 "buscar en internet:", "consulta en web:", "consulta en internet:", 
                 "investiga en web:", "investiga en internet:"]
    return any(g in pregunta.lower() for g in gatillos)

# Función principal del agente 
def responder_agente(pregunta: str):
    usar_web = usuario_pide_web(pregunta)

    # 1. Recuperar contexto de memoria
    contexto = formatear_contexto()

    # 2. Consultar herramienta adecuada
    if usar_web:
        tool_output = web_tool.run(pregunta)
        tool_text = "\n".join([
            f"- {r.get('title','(sin título)')} — {r.get('url','')}\n{r.get('content','')[:350]}..."
            for r in tool_output.get("results", [])
        ])
    else:
        tool_text = rag_tool._run(pregunta)

    # 3. Construir prompt final
    system_prompt = AGENTE_PERFIL
    user_prompt = f"""
Contexto previo:
{contexto}

Usuario pregunta:
{pregunta}

Información recuperada:
{tool_text}

Responde en español de manera clara y técnica.
Si la información viene de apuntes, cita el documento o autor.
Si la información viene de la web, cita la fuente (URL o medio).
"""

    completion = llm_orq.invoke([
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ])
    respuesta = completion.content

    # 4. Actualizar memoria
    MEMORIA.append(("user", pregunta))
    MEMORIA.append(("assistant", respuesta))

    return respuesta
