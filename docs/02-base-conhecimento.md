# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Garante que o agente saiba de dúvidas anteriores do cliente. |
| `perfil_investidor.json` | JSON | Define o patrimônio, objetivos e tolerância ao risco. |
| `produtos_financeiros.json` | JSON | Catálogo de produtos usado para dar exemplos educativos. |
| `transacoes.csv` | CSV | Analisa o fluxo de caixa (aportes, saques e dividendos). |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Campos extras no perfil do investidor (objetivos de curto/médio/longo prazo).
Categorias de produtos com risco e liquidez.
Indicadores financeiros (ex.: CDI, IPCA, Selic) para contextualizar recomendações.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os arquivos CSV/JSON são lidos no início da sessão e ficam disponíveis no contexto.

### Como os dados são usados no prompt?
O perfil do investidor é usado para filtrar produtos.
As transações ajudam a calcular liquidez e sugerir alocação.
O histórico de atendimento evita redundância.
Os produtos financeiros são consultados dinamicamente conforme o perfil.

[Sua descrição aqui]

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: Daniel Lopes
- Perfil: Moderado
- Saldo disponível: R$ 15.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
