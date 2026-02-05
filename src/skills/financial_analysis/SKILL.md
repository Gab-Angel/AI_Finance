---
name: financial_analysis
description: Use esta skill para categorizar transações financeiras de extratos bancários OFX.
---

# financial_analysis

## Overview

Esta skill fornece instruções para categorizar transações financeiras baseado na descrição de cada transação.

## Instructions

### 1. Receber Dados

Você receberá um DataFrame com as seguintes colunas:
- `id`: Identificador único da transação
- `date`: Data da transação
- `type`: Tipo (credit ou debit)
- `amount`: Valor da transação
- `description`: Descrição da transação

### 2. Categorizar Transações

Sua única tarefa é **categorizar cada transação** baseado na descrição.

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
- Analise palavra por palavra a descrição para escolher a categoria correta

### 3. Output Esperado

Para cada transação, informe apenas a categoria atribuída.

**NÃO calcule métricas, totais ou percentuais - isso será feito por outra skill.**

Apenas categorize as transações de forma precisa.