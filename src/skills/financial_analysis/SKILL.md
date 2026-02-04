---
name: financial_analysis
description: Use esta skill para analisar transações financeiras de extratos bancários OFX. Categoriza gastos, identifica padrões e calcula métricas essenciais.
---

# financial_analysis

## Overview

Esta skill fornece instruções para analisar extratos bancários no formato JSON estruturado, categorizando transações e calculando métricas financeiras.

## Instructions

### 1. Receber e Validar Dados

Quando receber um JSON com transações, primeiro valide:
- Cada transação tem: id, date, type, amount, description
- Valores monetários são numéricos
- Datas estão no formato YYYY-MM-DD

### 2. Categorizar Transações

Categorize cada transação baseado na descrição:

**Categorias de receita:**
- `transferencia_recebida`: Pix recebido, transferências de entrada
- `rendimento`: Rendimentos de investimentos

**Categorias de despesa:**
- `investimento`: Aplicações (RDB, CDB, Tesouro, Ações)
- `transferencia_enviada`: Pix enviado, transferências de saída para pessoas
- `compras`: Mercado Pago, marketplace, compras online
- `pagamentos`: Faturas, boletos, contas fixas
- `alimentacao`: Restaurantes, supermercados, delivery
- `transporte`: Uber, combustível, transporte público
- `outros`: Quando não se encaixar nas categorias acima

**Regras importantes:**
- Seja conservador: se em dúvida, use "outros"
- Para Pix, veja se é para pessoa física (transferencia) ou empresa (compra/pagamento)
- "Pagamento de fatura" sempre é categoria "pagamentos"

### 3. Calcular Métricas

Calcule as seguintes métricas:

**Totais:**
- Total de receitas (soma de valores positivos)
- Total de despesas (soma de valores negativos, em módulo)
- Saldo líquido (receitas - despesas)

**Por categoria:**
- Total gasto em cada categoria
- Percentual de cada categoria sobre o total de despesas
- Número de transações por categoria

**Temporais:**
- Média de gastos por dia
- Identificar dias com mais movimentação

### 4. Estruturar Output

Organize a análise em:

```json
{
  "resumo_geral": {
    "total_receitas": 0.00,
    "total_despesas": 0.00,
    "saldo_liquido": 0.00,
    "periodo": "YYYY-MM-DD a YYYY-MM-DD"
  },
  "por_categoria": [
    {
      "categoria": "nome",
      "total": 0.00,
      "percentual": 0.0,
      "transacoes": 0
    }
  ],
  "transacoes_categorizadas": [
    {
      "id": "...",
      "date": "...",
      "amount": 0.00,
      "description": "...",
      "category": "..."
    }
  ]
}
```

### 5. Observações Importantes

- Valores de despesa devem ser apresentados em módulo (positivo) nos resumos
- Percentuais devem ter 1 casa decimal
- Ordenar categorias por total gasto (maior para menor)
- Incluir apenas categorias que tiveram transações