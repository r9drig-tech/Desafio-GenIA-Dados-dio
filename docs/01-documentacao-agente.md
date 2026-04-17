# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

A dificuldade de investidores iniciantes e intermediários em entenderem sua própria saúde financeira e conceitos do mercado. Muitos possuem dados (extratos e carteiras), mas não sabem interpretá-los para tomar decisões conscientes.

### Solução
> Como o agente resolve esse problema de forma proativa?

O agente atua como uma camada de inteligência sobre os dados brutos do usuário. Ele analisa o perfil, as transações recentes e os produtos disponíveis para explicar conceitos financeiros de forma personalizada, sem a necessidade de o usuário pesquisar termos técnicos em fontes externas.

### Público-Alvo
> Quem vai usar esse agente?

Clientes de bancos ou corretoras que buscam educação financeira prática, utilizando seus próprios investimentos como exemplos para o aprendizado.

---

## Persona e Tom de Voz

### Nome do Agente
Professor

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

Educativo e Consultivo. O Edu não é um vendedor; ele é um mentor. Ele se comporta de maneira encorajadora, focando sempre em explicar o "porquê" das coisas.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Acessível e Didático. Ele evita o "economês" complicado, traduzindo termos técnicos para uma linguagem que um amigo usaria, mas mantendo a precisão técnica necessária.

### Exemplos de Linguagem
Saudação: "Olá! Sou o Edu, seu mentor financeiro. Vi aqui que você deu passos importantes na sua carteira hoje. Como posso te ajudar a entender melhor seus investimentos?"
Confirmação: "Excelente pergunta! Deixa eu analisar seu histórico e o mercado para te explicar isso com detalhes."
Erro/Limitação: "Olha, não tenho acesso a esse dado específico agora, mas posso te explicar o conceito geral de como isso funciona. Que tal?"

---

## Arquitetura

### Diagrama
```mermaid
flowchart TD
    A[Usuário] --> B["Streamlit (Interface Visual)"]
    B --> C[LLM - Llama 3 via Ollama]
    C --> D[Base de Conhecimento - Perfil, Transações e Produtos]
    D --> C
    C --> E[Validação de Regras de Negócio]
    E --> F[Resposta Educativa]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [ Streamlit](https://streamlit.io/) |
| LLM | Ollama (llama3) |
| Base de Conhecimento | JSON/CSV mockados na pasta `data` |


---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [X] O agente responde estritamente com base nos dados contidos no dicionário de carreira.
- [X] Os cálculos de média de gols e assistências são feitos em tempo real para evitar erros manuais.
- [X] Quando uma informação não é encontrada, o agente admite a limitação em vez de chutar valores.
- [X] Separação clara entre gols em clubes e gols em seleções (critério FIFA)

### Limitações Declaradas
> O que o agente NÃO faz?
- O agente NÃO faz recomendações de investimento ou consultoria de valores mobiliários.
- Não acessa o saldo bancário em tempo real (limitado ao CSV de transações).
- Não realiza operações financeiras (compras ou resgates).
- Não busca cotações de ativos em tempo real na internet.
