import re
import json
from datetime import datetime
from typing import Dict, List, Any


def parse_ofx(file_path: str) -> Dict[str, Any]:
    """Parse OFX file to structured JSON"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract account info
    account_id = re.search(r'<ACCTID>(.*?)</ACCTID>', content).group(1)
    bank_id = re.search(r'<BANKID>(.*?)</BANKID>', content).group(1)
    currency = re.search(r'<CURDEF>(.*?)</CURDEF>', content).group(1)
    
    # Extract period
    start_date = re.search(r'<DTSTART>(.*?)\[', content).group(1)
    end_date = re.search(r'<DTEND>(.*?)\[', content).group(1)
    
    # Extract balance
    balance = float(re.search(r'<BALAMT>(.*?)</BALAMT>', content).group(1))
    
    # Extract transactions
    transactions = []
    trn_pattern = r'<STMTTRN>(.*?)</STMTTRN>'
    
    for match in re.finditer(trn_pattern, content, re.DOTALL):
        trn = match.group(1)
        
        trn_type = re.search(r'<TRNTYPE>(.*?)</TRNTYPE>', trn).group(1)
        date = re.search(r'<DTPOSTED>(.*?)\[', trn).group(1)
        amount = float(re.search(r'<TRNAMT>(.*?)</TRNAMT>', trn).group(1))
        fitid = re.search(r'<FITID>(.*?)</FITID>', trn).group(1)
        memo = re.search(r'<MEMO>(.*?)</MEMO>', trn).group(1)
        
        transactions.append({
            'id': fitid,
            'date': _format_date(date),
            'type': trn_type.lower(),
            'amount': amount,
            'description': memo,
            'category': None  # To be filled by categorization tool
        })
    
    return {
        'account': {
            'id': account_id,
            'bank_id': bank_id,
            'currency': currency
        },
        'period': {
            'start': _format_date(start_date),
            'end': _format_date(end_date)
        },
        'balance': {
            'final': balance
        },
        'transactions': transactions,
        'metadata': {
            'total_transactions': len(transactions),
            'parsed_at': datetime.now().isoformat()
        }
    }


def _format_date(ofx_date: str) -> str:
    """Convert OFX date format to ISO"""
    # OFX format: 20260110000000
    year = ofx_date[:4]
    month = ofx_date[4:6]
    day = ofx_date[6:8]
    return f"{year}-{month}-{day}"


if __name__ == "__main__":
    # Test parser
    result = parse_ofx('/home/angel/python/AI_Finance/extrato.ofx')
    print(json.dumps(result, indent=2, ensure_ascii=False))
