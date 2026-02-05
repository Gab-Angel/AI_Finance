import os
import tempfile
import streamlit as st


from src.parser.ofx_parser import parse_ofx
from src.agent.deep_agent import analyze_transactions

st.set_page_config(
    page_title="Análise Financeira IA",
    layout="centered"
)

st.title("📊 Análise de Extrato Bancário com IA")

uploaded_file = st.file_uploader(
    "Faça upload do extrato bancário (.ofx)",
    type=["ofx"]
)

if uploaded_file:
    with st.spinner("Lendo extrato e analisando com IA..."):
       
        with tempfile.NamedTemporaryFile(delete=False, suffix=".ofx") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        try:
            parsed = parse_ofx(tmp_path)

            df_transactions = parsed["transactions"]
            metadata = parsed["metadata"]

            st.subheader("📌 Informações da Conta")
            st.json(metadata)

            with st.expander("📄 Ver transações"):
                st.dataframe(df_transactions, use_container_width=True)

            transactions_for_ai = df_transactions.reset_index().to_dict(
                orient="records"
            )

            markdown_report = analyze_transactions(transactions_for_ai)

            st.success("Análise concluída!")

            st.markdown("---")
            st.markdown(markdown_report)

            st.download_button(
                label="⬇️ Baixar relatório (.md)",
                data=markdown_report,
                file_name="relatorio_financeiro.md",
                mime="text/markdown"
            )

        finally:
            os.remove(tmp_path)
