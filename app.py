import os

import streamlit as st
import tempfile

from src.parser.ofx_parser import parse_ofx
from src.agent.deep_agent import analyze_transactions

st.set_page_config(
    page_title="Análise Financeira IA",
    layout="centered"
)

st.title("📊 Análise de Extrato Bancário com IA")

uploaded_file = st.file_uploader(
    "Faça upload do seu extrato bancário (.ofx)",
    type=["ofx"]
)

if uploaded_file:
    with st.spinner("Processando extrato e analisando com IA..."):
        # Salva arquivo temporário
        with tempfile.NamedTemporaryFile(delete=False, suffix=".ofx") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        try:
            # Parse OFX
            data = parse_ofx(tmp_path)

            # IA analisa
            markdown_report = analyze_transactions(data["transactions"])

            st.success("Análise concluída!")

            # Renderiza Markdown
            st.markdown("---")
            st.markdown(markdown_report)

            # Botão para download
            st.download_button(
                label="⬇️ Baixar relatório (.md)",
                data=markdown_report,
                file_name="relatorio_financeiro.md",
                mime="text/markdown"
            )

        finally:
            os.remove(tmp_path)
