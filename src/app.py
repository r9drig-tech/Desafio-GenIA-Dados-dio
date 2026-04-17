import json
import pandas as pd
import requests
import streamlit as st

# ============ CONFIGURAÇÃO ============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "llama3" # O Llama 3 é essencial para análise de dados complexos

# ============ CARREGAR DADOS ============
try:
    # Carregando as estatísticas detalhadas e lesões
    estatisticas = json.load(open('./data/Carreira e Lesões.json', encoding='utf-8'))
    # Carregando os títulos e prêmios individuais
    titulos = json.load(open('./data/Prêmio e Títulos.json', encoding='utf-8'))
    # Carregando o histórico financeiro e transferências
    transacoes = pd.read_csv('./data/transacoes.csv', encoding='utf-8')
    # Carregando o histórico de negociações e mercado
    historico = pd.read_csv('./data/historico_atendimento.csv', encoding='utf-8')

    # ============ MONTAR CONTEXTO ============
    contexto = f"""
    ATLETA: Neymar da Silva Santos Júnior
    DADOS TÉCNICOS POR CLUBE (Gols, Assistências, Lesões):
    {json.dumps(estatisticas, indent=2, ensure_ascii=False)}

    TÍTULOS E PREMIAÇÕES:
    {json.dumps(titulos, indent=2, ensure_ascii=False)}

    TRANSFERÊNCIAS E VALORES DE MERCADO:
    {transacoes.to_string(index=False)}

    NEGOCIAÇÕES E DECISÕES DE CARREIRA:
    {historico.to_string(index=False)}
    """
except Exception as e:
    st.error(f"Erro ao carregar a base de dados do Neymar: {e}")
    st.stop()

# ============ SYSTEM PROMPT ============
SYSTEM_PROMPT = """Você é o AgentBot Analytics, especialista em ciência de dados esportivos.
Sua missão é analisar a carreira de Neymar Jr. de forma técnica e baseada em fatos.

REGRAS:
- Use APENAS o CONTEXTO fornecido para responder;
- Se perguntarem sobre clubes que ele não jogou (ex: Real Madrid), cite as 'Recusas' que estão no histórico;
- Quando falar de lesões, seja preciso sobre os dias afastado;
- Se a informação não estiver nos arquivos, diga: 'Não possuo este dado na base atual';
- Responda de forma direta, preferencialmente usando bullet points para estatísticas.
"""

# ============ CHAMAR OLLAMA ============
def perguntar(msg):
    prompt_final = f"{SYSTEM_PROMPT}\n\nCONTEXTO DA CARREIRA:\n{contexto}\n\nPergunta: {msg}"
    
    try:
        # Timeout de 90s pois o contexto é grande
        r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt_final, "stream": False}, timeout=90)
        return r.json()['response']
    except Exception as e:
        return f"Erro de conexão: Verifique se o Ollama está rodando o modelo {MODELO}. (Erro: {e})"

# ============ INTERFACE ============

st.title("⚽ AgentBot Analytics: Neymar Jr.")
st.markdown("---")

if pergunta := st.chat_input("Perqunte sobre gols, títulos, lesões ou transferências..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("Analisando base de dados histórica..."):
        resposta = perguntar(pergunta)
        st.chat_message("assistant").write(resposta)
