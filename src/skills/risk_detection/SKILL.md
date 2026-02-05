---
name: risk_detection
description: Use esta skill para identificar padrões de gastos, riscos financeiros e anomalias em transações bancárias.
---

# risk_detection

## Overview

Esta skill fornece instruções para detectar padrões preocupantes, riscos financeiros e anomalias que podem comprometer a saúde financeira do usuário.

## Instructions

### 1. Dados Recebidos

Você receberá um DataFrame já com métricas calculadas:
- Transações categorizadas
- Total de receitas
- Total de despesas
- Saldo líquido
- Totais por categoria
- Período analisado

**Seu trabalho é ANALISAR, não calcular.**

### 2. Análise de Saldo e Fluxo de Caixa

Baseado nos totais fornecidos, classifique o risco:

**Níveis de alerta:**
- 🟢 **Baixo**: Saldo positivo, receitas > despesas
- 🟡 **Médio**: Saldo próximo de zero (±10% das receitas)
- 🔴 **Alto**: Saldo negativo, receitas < despesas

### 3. Padrões de Gastos Preocupantes

Analise a distribuição de gastos por categoria:

**Gastos concentrados:**
- Se uma categoria representa >40% do total → Alerta de concentração
- Identifique qual categoria está dominando

**Ausência de investimentos:**
- Se investimentos = 0 ou <5% das receitas → Alerta de planejamento

**Transferências recorrentes:**
- Se "transferencia_enviada" é a maior categoria → Investigar
- Múltiplas transferências a terceiros → Possível descontrole

### 4. Detecção de Anomalias

Identifique transações que fogem do padrão:

**Critérios:**
- Valor individual muito superior aos demais (>2x a média)
- Descrições genéricas demais
- Categoria "outros" com valores altos

**Importante:** Não acuse sem contexto. Anomalia ≠ erro.

### 5. Análise de Frequência

Observe o número de transações:

**Alertas:**
- Muitas transações (>10) em período curto → Possível descontrole
- Poucas transações (<3) mas grandes valores → Investigar padrão
- Proporção receitas/despesas muito desbalanceada

### 6. Categorias de Risco Geral

Classifique o risco geral baseado em múltiplos fatores:

**🔴 Risco Alto:**
- Saldo negativo
- Gastos >120% das receitas
- Zero investimentos E gastos concentrados
- Múltiplas anomalias detectadas

**🟡 Risco Médio:**
- Saldo próximo de zero
- Gastos = 90-110% das receitas
- Investimentos <10% das receitas
- Gastos concentrados em 1-2 categorias

**🟢 Risco Baixo:**
- Saldo positivo
- Gastos <90% das receitas
- Algum investimento presente
- Diversificação razoável

### 7. Output Esperado

Forneça análise em Markdown:

```markdown
## ⚠️ Avaliação de Riscos

**Nível de Risco Geral:** 🟢/🟡/🔴 [Baixo/Médio/Alto]

### Alertas Identificados
- ⚠️ [Tipo]: [Descrição específica com números]
- ⚠️ [Tipo]: [Descrição específica com números]

### Padrões Observados
- [Padrão 1]: [Observação]
- [Padrão 2]: [Observação]
```

### 8. Observações Importantes

- **Contextualize:** Deixe claro se o período é curto (1 mês)
- **Seja específico:** Use valores reais ("R$ 350" não "muito")
- **Não alarme:** Prefira "atenção" a "perigo"
- **Foque no acionável:** Sempre vincule alerta a ação corretiva
- **NÃO invente números:** Use apenas os dados fornecidos