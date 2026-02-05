---
name: report_generation
description: Use esta skill para gerar relatórios financeiros estruturados, padronizados e acionáveis baseados na análise de transações.
---

# report_generation

## Overview

Esta skill define as regras para gerar o relatório final de análise financeira. O formato exato está definido no arquivo `report_template.md`.

## Dados Recebidos

Você receberá:
- DataFrame com transações categorizadas
- Métricas já calculadas (totais, percentuais, etc.)
- Análise de riscos já feita
- Período analisado

**Seu trabalho é ORGANIZAR e COMUNICAR seguindo o template, não calcular.**

## Instructions

### 1. Estrutura Obrigatória

O relatório deve ter **EXATAMENTE** 5 seções nesta ordem:

1. 📊 Resumo Executivo
2. 💰 Análise por Categoria
3. 🔍 Padrões Identificados
4. ⚠️ Riscos e Alertas
5. 💡 Recomendações

**Veja `report_template.md` para o formato EXATO de cada seção.**

### 2. Tom e Linguagem

**Características:**
- **Profissional**, mas acessível
- **Direto** e objetivo
- **Empático**, não alarmista
- **Acionável**, não apenas descritivo

**Evite:**
- Jargões técnicos excessivos
- Tom condescendente ou julgador
- Generalizações vagas ("você gasta muito")
- Repetição de informações

**Prefira:**
- Dados concretos ("R$ 350 em compras online")
- Comparações úteis ("35% do total")
- Sugestões práticas ("reduzir em R$ 100/mês")

### 3. Regras de Formatação

**Valores monetários:**
- Sempre em reais: R$ X.XXX,XX
- Despesas sem sinal negativo nas tabelas
- Use emojis para status: 🟢🟡🔴

**Percentuais:**
- 1 casa decimal: XX.X%
- Sempre com contexto

**Datas:**
- Formato brasileiro: DD/MM/YYYY

**Tabelas:**
- Ordenar por valor (maior → menor)
- Limitar a top 5-7 categorias

### 4. Recomendações SMART

Cada recomendação deve ser:
- **S**pecífica: qual categoria/ação?
- **M**ensurável: quanto/quantas?
- **A**tingível: realista?
- **R**elevante: alto impacto?
- **T**emporal: quando?

**Exemplo correto:**
✅ "Reduza gastos com marketplace em 30% (de R$ 240 para R$ 170), limitando compras a 2x/mês"

**Exemplo errado:**
❌ "Gaste menos"

### 5. Regras Críticas

**NUNCA:**
- Invente números ou cálculos
- Mude a estrutura das 5 seções
- Use linguagem técnica demais
- Seja alarmista sem dados

**SEMPRE:**
- Use EXATAMENTE os dados fornecidos
- Siga o formato do `report_template.md`
- Seja empático e construtivo
- Forneça ações práticas

### 6. Checklist Obrigatório

Antes de finalizar, confirme:
- ✅ Seguiu o formato exato do `report_template.md`
- ✅ Todas as 5 seções presentes na ordem correta
- ✅ Valores dos dados fornecidos (não inventados)
- ✅ Recomendações específicas e mensuráveis
- ✅ Tom profissional e empático
- ✅ Emojis corretos (📊💰🔍⚠️💡🟢🟡🔴)