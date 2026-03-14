import json
import pandas as pd
import streamlit as st
import requests
import os

# ========== CONFIGURAÇÃO ==========
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss:120b-cloud"

# ======== CAMINHO BASE DO PROJETO ========
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data")

# ======== FUNÇÕES DE CARREGAMENTO ========

def carregar_json(nome):
    caminho = os.path.join(DATA_PATH, nome)
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)

def carregar_csv(nome):
    caminho = os.path.join(DATA_PATH, nome)
    return pd.read_csv(caminho)

# ======== CARREGAR DADOS ========

perfil_data = carregar_json("perfil_pagador.json")
perfil = perfil_data["clientes"][0]   # pega primeiro cliente

transacoes = carregar_csv("transacoes.csv")
historico = carregar_csv("historico_atendimento.csv")
clientes = carregar_csv("tabela_de_clientes.csv")
produtos = carregar_json("produtos_financeiros.json")

# ========== MONTAR CONTEXTO ==========

contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, score {perfil['score_credito']}

RENDA MENSAL: R$ {perfil['renda_mensal']}  
EMPREGADO COMO: {perfil['tipo_emprego']}

PERFIL FINANCEIRO
Comprometimento de renda: {perfil['comprometimento_renda']}
Histórico de atrasos: {perfil['historico_atrasos']}
Tempo no emprego: {perfil['tempo_emprego_anos']} anos

TRANSAÇÕES RECENTES:
{transacoes.head(10).to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.head(10).to_string(index=False)}

PRODUTOS DE CRÉDITO DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ========== SYSTEM PROMPT ==========

SYSTEM_PROMPT = """
Você é o CredIA, um agente inteligente de análise de crédito amigável e didático.

OBJETIVO:
Ajudar clientes a entender seu perfil financeiro, avaliar risco de crédito
e indicar qual tipo de empréstimo pode ser mais adequado.

REGRAS:
- Nunca invente produtos ou taxas
- Não responda perguntas fora de crédito ou finanças
- Use os dados do cliente
- Linguagem simples
- Sempre explique a recomendação
- Considere risco de endividamento
- Respostas curtas (máx 3 parágrafos)
"""

# ========== CHAMAR OLLAMA ==========

def perguntar(msg):

    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

Pergunta: {msg}
"""

    try:
        r = requests.post(
            OLLAMA_URL,
            json={
                "model": MODELO,
                "prompt": prompt,
                "stream": False
            }
        )

        return r.json()["response"]

    except Exception as e:
        return f"Erro ao acessar modelo: {e}"

# ========== INTERFACE STREAMLIT ==========

st.title("💳 CredIA — Assistente Inteligente de Crédito")

st.subheader("📊 Dashboard Financeiro do Cliente")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Score de Crédito",
    perfil["score_credito"]
)

col2.metric(
    "Renda Mensal",
    f'R$ {perfil["renda_mensal"]}'
)

col3.metric(
    "Comprometimento",
    f'{perfil["comprometimento_renda"]*100:.0f}%'
)

col4.metric(
    "Atrasos",
    perfil["historico_atrasos"]
)


st.write("Pergunte sobre seu perfil financeiro, crédito ou empréstimos.")

if pergunta := st.chat_input("Digite sua pergunta..."):

    st.chat_message("user").write(pergunta)

    with st.spinner("Analisando seu perfil..."):

        resposta = perguntar(pergunta)

        st.chat_message("assistant").write(resposta)

if "historico_chat" not in st.session_state:
    st.session_state.historico_chat = []

st.session_state.historico_chat.append({"user": pergunta})

