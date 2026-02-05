import os
import logging
from deepagents import create_deep_agent
from langchain_groq import ChatGroq
from src.parser.ofx_parser import parse_ofx
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.1,
    api_key=os.getenv("GROQ_API_KEY")
)

system_prompt = """
Você é um analista financeiro especializado em finanças pessoais.

Analise estas transações seguindo TODAS as skills disponíveis:

1. **financial_analysis**: Categorize 
2. **risk_detection**: Identifique padrões e riscos
3. **report_generation**: Gere relatório estruturado em 5 seções

IMPORTANTE: Siga exatamente o formato do report_template.md
"""

agent = create_deep_agent(
    model=llm,
    system_prompt=system_prompt,
    skills=["../skills/"] 
)


def analyze_transactions(transactions: list) -> str:
    logging.info(f"Analisando {len(transactions)} transações...")
    
    result = agent.invoke({
        "messages": [{
            "role": "user",
            "content": f"""
Analise estas Transações: {transactions}
"""
        }]
    })

    resposta_final = result["messages"][-1]
    logging.info("Análise concluída!")
    return resposta_final.content


if __name__ == "__main__":

    data = parse_ofx('/home/angel/python/AI_Finance/extrato.ofx')
    df = data['transactions']
    metadata = data['metadata']
    
    logging.info(f"Total de transações: {len(df)}")
    logging.info(f"Período: {metadata['start_date']} até {metadata['end_date']}")
    logging.info(f"Saldo final: R$ {metadata['balance']:.2f}")
    
    # Invocar agente
    result = agent.invoke({
        "messages": [{
            "role": "user",
            "content": f"""
Analise estas transações financeiras:

PERÍODO: {metadata['start_date']} a {metadata['end_date']}
SALDO FINAL: R$ {metadata['balance']:.2f}
CONTA: {metadata['account_id']}

TRANSAÇÕES:
{df.to_string()}

Forneça análise de gastos, categorização e insights.
"""
        }]
    })
    
    resposta_final = result['messages'][-1]
    tokens = getattr(resposta_final, 'response_metadata', {})
    token_usage = tokens.get('token_usage', {})

    print("\n" + "="*50)
    print("ANÁLISE FINANCEIRA")
    print("="*50)
    print(resposta_final.content)
    print("\n" + "="*50)
    print("ESTATÍSTICAS")
    print("="*50)
    print(f'   • Tokens entrada: {token_usage.get("prompt_tokens", "N/A")}')
    print(f'   • Tokens saída: {token_usage.get("completion_tokens", "N/A")}')
    print(f'   • Total tokens: {token_usage.get("total_tokens", "N/A")}')