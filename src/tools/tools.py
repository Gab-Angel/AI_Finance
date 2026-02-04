from langchain_core.tools import tool
from typing import List, Dict


# Regras de categorização
CATEGORY_RULES = {
    "investimento": ["aplicação", "rdb", "cdb", "tesouro", "ações"],
    "transferencia_recebida": ["transferência recebida", "pix recebido"],
    "transferencia_enviada": ["transferência enviada", "pix enviado"],
    "compras": ["mercado pago", "marketplace", "compra"],
    "pagamentos": ["pagamento de fatura", "boleto", "conta"],
    "outros": []
}


@tool(description="""
    Categoriza uma lista de transações baseado na descrição.
    
    Args:
        transactions: Lista de dicionários com transações
        
    Returns:
        Lista de transações com campo 'category' preenchido
    """)
def categorize_transactions(transactions: List[Dict]) -> List[Dict]:
    categorized = []
    
    for trn in transactions:
        description = trn.get('description', '').lower()
        category = "outros"  # Default
        
        # Aplicar regras
        for cat, keywords in CATEGORY_RULES.items():
            if any(keyword in description for keyword in keywords):
                category = cat
                break
        
        # Adicionar categoria
        trn_copy = trn.copy()
        trn_copy['category'] = category
        categorized.append(trn_copy)
    
    return categorized


if __name__ == "__main__":
    # Teste
    test_transactions = [
        {
            'id': '1',
            'description': 'Aplicação RDB',
            'amount': -10.0
        },
        {
            'id': '2', 
            'description': 'Transferência recebida pelo Pix',
            'amount': 50.0
        },
        {
            'id': '3',
            'description': 'PIX Marketplace - MERCADO PAGO',
            'amount': -24.6
        }
    ]
    
    result = categorize_transactions.invoke({"transactions": test_transactions})
    
    for t in result:
        print(f"{t['description'][:30]:30} -> {t['category']}")