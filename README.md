# 🤖 AI Finance Agent

> Sistema inteligente de análise financeira pessoal usando Deep Agents com LangChain e IA Generativa

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-Deep_Agents-green.svg)](https://python.langchain.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Sobre o Projeto

AI Finance Agent é um sistema de análise financeira pessoal que utiliza **Deep Agents** para transformar extratos bancários em insights acionáveis. O projeto implementa uma arquitetura de agentes especializados que categorizam transações, detectam riscos e geram relatórios padronizados automaticamente.

### 🎯 Principais Funcionalidades

- ✅ **Análise Automática de Extratos OFX**: Parse e estruturação de dados bancários
- 🏷️ **Categorização Inteligente**: Classificação automática de transações usando IA
- ⚠️ **Detecção de Riscos**: Identificação de padrões preocupantes e anomalias
- 📊 **Relatórios Padronizados**: Geração de análises completas em Markdown
- 🌐 **Interface Web**: Dashboard interativo com Streamlit
- 🔄 **Arquitetura Modular**: Sistema baseado em skills reutilizáveis

---

## 🏗️ Arquitetura

```
┌─────────────────────────────────────────────────┐
│                 Interface Web                   │
│              (Streamlit + UI)                   │
└────────────────┬────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────┐
│              Deep Agent Core                    │
│         (LangChain + Groq LLM)                  │
└──────┬──────────┬──────────┬───────────────────┘
       │          │          │
       ▼          ▼          ▼
┌──────────┐ ┌──────────┐ ┌──────────────┐
│Financial │ │   Risk   │ │   Report     │
│Analysis  │ │Detection │ │ Generation   │
│  Skill   │ │  Skill   │ │    Skill     │
└──────────┘ └──────────┘ └──────────────┘
       │          │          │
       └──────────┴──────────┘
                 │
                 ▼
       ┌─────────────────┐
       │  OFX Parser     │
       │  (ofxparse +    │
       │   pandas)       │
       └─────────────────┘
```

### 🧩 Componentes Principais

#### 1. **Deep Agent** 
Sistema de IA baseado em LangChain que orquestra múltiplas skills especializadas para análise financeira completa.

#### 2. **Skills System**
- **financial_analysis**: Categorização de transações
- **risk_detection**: Análise de riscos e padrões
- **report_generation**: Formatação de relatórios padronizados

#### 3. **OFX Parser**
Converte arquivos OFX (Open Financial Exchange) em DataFrames estruturados para processamento.

---

## 🚀 Tecnologias Utilizadas

### Core
- **Python 3.11+**: Linguagem principal
- **LangChain DeepAgents**: Framework para agentes de IA
- **Groq API**: Modelo LLM (openai/gpt-oss-120b)
- **Streamlit**: Interface web interativa

### Processamento de Dados
- **Pandas**: Manipulação de dados tabulares
- **ofxparse**: Parse de arquivos OFX

### IA e LLMs
- **LangChain**: Orquestração de agentes
- **langchain-groq**: Integração com Groq API

---

## 📦 Instalação

### Pré-requisitos
- Python 3.11 ou superior
- pip (gerenciador de pacotes Python)
- Conta Groq com API key ([obter aqui](https://console.groq.com))

### Passo a Passo

1. **Clone o repositório**
```bash
git clone https://github.com/Gab-Angel/AI_Finance.git
```

2. **Crie um ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente**
```bash
cp .env.example .env
# Edite o arquivo .env e adicione sua GROQ_API_KEY
```

Exemplo `.env`:
```env
GROQ_API_KEY=sua_chave_aqui
```

---

## 💻 Como Usar

### Interface Web (Streamlit)

```bash
streamlit run app.py
```

Acesse `http://localhost:8501` e faça upload de um arquivo `.ofx`

### Via Código Python

```python
from src.parser.ofx_parser import parse_ofx
from src.agent.deep_agent import analyze_transactions

# Parse do extrato OFX
data = parse_ofx('seu_extrato.ofx')
transactions = data['transactions'].to_dict(orient='records')

# Análise com IA
report = analyze_transactions(transactions)

print(report)
```

---

📂 Estrutura do Projeto
ai-finance-agent/
│
├── app.py                          # Interface Streamlit
├── requirements.txt                # Dependências Python
├── .env.example                    # Template de variáveis de ambiente
│
├── src/
│   ├── agent/
│   │   ├── __init__.py
│   │   └── deep_agent.py          # Deep Agent principal
│   │
│   ├── parser/
│   │   ├── __init__.py
│   │   └── ofx_parser.py          # Parser de arquivos OFX
│   │
│   ├── tools/
│   │   └── tools.py               # Tools auxiliares (legado)
│   │
│   └── skills/                    # Skills do Deep Agent
│       ├── financial_analysis/
│       │   └── SKILL.md
│       ├── risk_detection/
│       │   └── SKILL.md
│       └── report_generation/
│           ├── SKILL.md
│           └── report_template.md
│
└── README.md

---

## 🎓 Como Funciona

### 1️⃣ Upload do Extrato
Usuário faz upload de arquivo `.ofx` pela interface web

### 2️⃣ Parsing
Sistema converte OFX para DataFrame estruturado:
```python
{
    'id': UUID único,
    'date': Data da transação,
    'amount': Valor (R$),
    'description': Descrição,
    'type': credit/debit
}
```

### 3️⃣ Análise com Deep Agent
O agente executa sequencialmente:

**Skill 1: financial_analysis**
- Categoriza cada transação (transferência, investimento, compras, etc.)

**Skill 2: risk_detection**
- Analisa saldo e fluxo de caixa
- Identifica gastos concentrados
- Detecta anomalias e padrões de risco

**Skill 3: report_generation**
- Gera relatório em 5 seções padronizadas
- Fornece recomendações SMART

### 4️⃣ Output
Relatório completo em Markdown com:
- 📊 Resumo Executivo
- 💰 Análise por Categoria
- 🔍 Padrões Identificados
- ⚠️ Riscos e Alertas
- 💡 Recomendações

---

## 🔧 Configuração Avançada

### Customizar Skills

Você pode criar suas próprias skills seguindo o padrão:

```markdown
---
name: sua_skill
description: Descrição da skill
---

# sua_skill

## Instructions

[Instruções detalhadas para a IA]
```

Adicione a skill em `src/skills/` e ela será automaticamente carregada.

### Alterar Modelo LLM

Em `src/agent/deep_agent.py`:

```python
llm = ChatGroq(
    model="llama-3.3-70b-versatile",  # Trocar modelo aqui
    temperature=0.1,
    api_key=os.getenv("GROQ_API_KEY")
)
```

Modelos disponíveis: `llama-3.3-70b-versatile`, `openai/gpt-oss-120b`, `mixtral-8x7b-32768`

---

## 📊 Exemplo de Saída

```markdown
# Relatório de Análise Financeira

## 📊 Resumo Executivo
**Período:** 01/01/2026 a 31/01/2026  
**Receitas:** R$ 50,00  
**Despesas:** R$ 103,51  
**Saldo Líquido:** R$ -53,51  
**Status:** 🔴 Negativo

## 💰 Análise por Categoria
| Categoria | Valor (R$) | % | Transações |
|-----------|------------|---|------------|
| Transferências | 64,60 | 62.4% | 3 |
| Pagamentos | 28,91 | 27.9% | 1 |
| Investimento | 10,00 | 9.7% | 1 |

## 💡 Recomendações
1. **Reduzir Transferências**: Limite a 1 por mês (-R$ 40)
2. **Aumentar Receitas**: Buscar +R$ 50 extras
3. **Elevar Investimentos**: 20% da receita para RDB/CDB
```

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaSkill`)
3. Commit suas mudanças (`git commit -m 'Add: nova skill de previsão'`)
4. Push para a branch (`git push origin feature/NovaSkill`)
5. Abra um Pull Request

---

## 📝 Roadmap

- [ ] Suporte a múltiplos meses de análise
- [ ] Gráficos interativos no dashboard
- [ ] Exportação para PDF
- [ ] Integração com Open Banking
- [ ] Comparativo com meses anteriores
- [ ] Alertas automáticos por email
- [ ] Suporte a múltiplas contas

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👤 Autor

**Gabriel Angel**
- GitHub: [@Gab-Angel](https://github.com/Gab-Angel)
- LinkedIn: [Gabriel Angel](https://www.linkedin.com/in/gabriel-angel-9277663a0)

---

## 🙏 Agradecimentos

- [LangChain](https://python.langchain.com/) pela framework de Deep Agents
- [Groq](https://groq.com/) pela API de LLM ultra-rápida
- [Streamlit](https://streamlit.io/) pela interface web simplificada
- Comunidade Python por todas as bibliotecas utilizadas

---

<div align="center">

**Feito com ❤️ e IA**

⭐ Se este projeto foi útil, considere dar uma estrela!

</div>