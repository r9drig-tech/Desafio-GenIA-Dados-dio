# Código da Aplicação

Esta pasta contém o código do seu agente financeiro.

## Estrutura Sugerida

```
src/
├── app.py              # Interface do Chat (Streamlit)
├── engine.py           # Lógica de RAG (Leitura de CSV/JSON e busca de contexto)
├── config.py           # Configurações de modelos e caminhos de dados
└── requirements.txt    # Dependências do projeto
```

## Exemplo de requirements.txt

```
streamlit       # Interface de usuário
pandas          # Manipulação dos dados (CSV/JSON)
ollama          # Conexão com modelo local (ou openai para nuvem)
python-dotenv   # Gestão de variáveis de ambiente
```

## Como Rodar

```bash
# Instalar dependências
pip install -r src/requirements.txt

#Preparar o Modelo:Se estiver usando o Ollama localmente
ollama run llama3

# Rodar a aplicação
streamlit run app.py
```
