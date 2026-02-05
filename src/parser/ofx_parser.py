import ofxparse
import pandas as pd
from pathlib import Path
from typing import Dict, Any

def parse_ofx(file_path: str) -> Dict[str, Any]:
    """Parse OFX file to structured data"""
    
    with open(file_path, 'rb') as f:  # Modo binário
        ofx = ofxparse.OfxParser.parse(f)
    
    account = ofx.account
    statement = account.statement
    
    # Transações
    transactions = []
    for trn in statement.transactions:
        transactions.append({
            'id': trn.id,
            'date': trn.date.date(),
            'amount': float(trn.amount),
            'description': trn.memo,
            'type': trn.type.lower()
        })
    
    df = pd.DataFrame(transactions).set_index('id')
    
    # Metadata
    metadata = {
        'account_id': account.account_id,
        'bank_id': account.routing_number,
        'currency': statement.currency,
        'start_date': statement.start_date.date(),
        'end_date': statement.end_date.date(),
        'balance': float(statement.balance)
    }

    df['amount'] = df['amount'].apply(lambda x: f"R$ {x:,.2f}")
    df['date'] = pd.to_datetime(df['date'])

    return {'transactions': df, 'metadata': metadata}
