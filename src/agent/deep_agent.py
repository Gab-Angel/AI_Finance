import os
from deepagents import create_deep_agent
from langchain_groq import ChatGroq
from src.parser.ofx_parser import parse_ofx
from src.tools.tools import categorize_transactions
from dotenv import load_dotenv

load_dotenv()

# Configurar LLM
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.1,
    api_key=os.getenv("GROQ_API_KEY")
)

# System prompt
system_prompt = """
Você é um analista financeiro especializado em finanças pessoais.

Analise extratos bancários e forneça insights claros.

Suas responsabilidades:
- Categorizar transações
- Identificar padrões de gastos  
- Detectar anomalias
- Dar recomendações práticas
"""

# Criar Deep Agent
agent = create_deep_agent(
    model=llm,
    system_prompt=system_prompt,
    skills=["../skills/"] 
)

# Testar
if __name__ == "__main__":
    
    
    # Parse do OFX
    data = parse_ofx('/home/angel/python/AI_Finance/extrato.ofx')
    
    # Invocar agente
    result = agent.invoke({
        "messages": [{
            "role": "user",
            "content": f"Analise estas transações: {data['transactions']}"
        }]
    })
    
    resposta_final = result['messages'][-1]
    metadata = getattr(resposta_final, 'response_metadata', {})
    token_usage = metadata.get('token_usage', {})

    print("\n" + "="*50)
    print("ANÁLISE FINANCEIRA")
    print("="*50)
    print(resposta_final.content)
    print(
        f'   • Tokens entrada: {token_usage.get("prompt_tokens", "N/A")}'
    )
    print(
        f'   • Tokens saída: {token_usage.get("completion_tokens", "N/A")}'
    )
    print(
        f'   • Total tokens: {token_usage.get("total_tokens", "N/A")}'
    )