import streamlit as st
import time
import random
from orquestador import responder_agente


# CONFIGURACIÓN DE PÁGINA 
st.set_page_config(page_title="TEC-IA Asistente", page_icon="🧠", layout="centered")

#  ESTILO LIMPIO Y ESTABLE 
st.markdown("""
<style>
.stApp {
    background: #f4f6fa;
    font-family: 'Segoe UI', sans-serif;
}

/* Título */
h1 {
    text-align: center;
    font-size: 2.6rem;
    color: #002b5c;
    margin-bottom: 0.3rem;
    font-weight: 700;
}
.subtitle {
    text-align: center;
    color: #3b6ea8;
    font-size: 1.1rem;
    margin-bottom: 1.2rem;
}

/* Chat container */
.chat-box {
    background: white;
    padding: 18px;
    border-radius: 14px;
    max-height: 65vh;
    overflow-y: auto;
    border: 1px solid #d9e2ec;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    margin-bottom: 15px;
}

/* Mensajes */
.user-msg {
    background: #002b5c;
    color: white;
    padding: 10px 14px;
    border-radius: 16px 16px 4px 16px;
    margin-left: auto;
    max-width: 75%;
    margin-bottom: 12px;
}
.bot-msg {
    background: #e8f0fa;
    color: #002b5c;
    padding: 10px 14px;
    border-radius: 16px 16px 16px 4px;
    margin-right: auto;
    max-width: 75%;
    margin-bottom: 12px;
}

/* Input */
.stChatInput > div > div {
    background: white !important;
    border-radius: 18px !important;
    border: 1px solid #d9e2ec;
}
</style>
""", unsafe_allow_html=True)

#  ESTADO DEL CHAT 
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "¡Hola! Soy **TEC-IA** 🤖. Estoy aquí para ayudarte con teoría, práctica y conceptos de Inteligencia Artificial del TEC. Pregúntame algo 👇."}
    ]

# ENCABEZADO 
st.markdown("""
<div style="text-align:center;">
    <img src="https://cdn-icons-png.flaticon.com/512/14313/14313824.png" width="85">
    <h1 style="margin-top: 10px; margin-bottom: 4px; font-weight: 700; color:#002b5c;">
        TEC-IA
    </h1>
    <div style="color:#3b6ea8; font-size: 1.1rem; margin-bottom: 14px;">
        Asistente para el curso de Inteligencia Artificial — TEC
    </div>
</div>
<hr style="border: 0; height: 1px; background: #d9e2ec; margin-top: 4px; margin-bottom: 18px;">
""", unsafe_allow_html=True)
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='user-msg'>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-msg'>{msg['content']}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# RESPUESTA SIMULADA 
def reply(prompt):
    time.sleep(1.0)
    respuestas = [
        f"Interesante pregunta sobre **{prompt}**. ¿Quieres que lo explique paso a paso o con un ejemplo práctico?",
        f"**{prompt}** se estudia en IA porque ayuda a entender cómo los sistemas pueden aprender patrones.",
        f"Te explico **{prompt}** de manera sencilla: ..."
    ]
    return random.choice(respuestas)

# INPUT DEL CHAT
prompt = st.chat_input("Escribe tu pregunta...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    answer = responder_agente(prompt)
    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.rerun()
