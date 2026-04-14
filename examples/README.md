# Exemplos e Referências

Esta pasta contém as referências conceituais e técnicas que serviram de base para a criação do especialista em dados da carreira de Neymar Jr.

## Vídeos de Referência

> 🎬Nota: Como este projeto é uma adaptação do desafio original da DIO para o contexto de Sports Data Analytics, as referências abaixo focam no raciocínio de transformar dados brutos em inteligência artificial.

| Etapa | Descrição | Link |
|-------|-----------|------|
| Documentação | Definição do Neymar Jr. como "Ativo de Mercado | [Concluído] |
| Base de Conhecimento | Estruturação de JSON/CSV para evitar alucinações. | [Concluído] |
| Prompts | Criação de persona de Analista Técnico e Guardrails. | [Concluído] |
| Aplicação | Desenvolvimento do protótipo em Streamlit + RAG. | [Concluído] |
| Métricas | Validação de assertividade estatística e segurança. | [Concluído] |
| Pitch | Apresentação da solução de inteligência esportiva. | [Concluído] |

## Exemplo de Implementação Simples
Para entender como o agente processa a informação, confira a estrutura lógica na pasta `src`/. O diferencial deste exemplo é a Injeção de Contexto Dinâmica:
Input: O usuário pergunta sobre uma lesão.
Processamento: O script busca a data e o tipo de lesão no `Carreira e Lesões.json`.
Prompt: O sistema envia para o LLM: "Com base no registro de 2023 [DADOS DO JSON], responda ao usuário sobre o tempo de recuperação."
Output: Resposta precisa e livre de invenções.

Confira na pasta `src/` um exemplo básico de estrutura de aplicação usando Streamlit.
