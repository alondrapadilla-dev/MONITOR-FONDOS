import streamlit as st
import pandas as pd
from datetime import datetime

with open("assets/estilos.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("<h2 class='titulo-principal'>Mapa Ejecutivo del Subejercicio 2025</h2>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='tarjeta'>", unsafe_allow_html=True)

    with st.expander("A ▸ Subejercicio 2025"):
        st.markdown("**A.1 Presupuesto Modificado**")
        st.markdown("**A.2 Presupuesto Devengado**")

    with st.expander("B ▸ Adecuaciones por revisar"):
        st.markdown("**B.1 Suplementos**")
        st.markdown("**B.2 Devoluciones**")

    with st.expander("C ▸ Subejercicio 2025 Estimado"):
        st.markdown("**C.1 Refrendos 2026**")
        with st.expander("C.2 Saldos por comprometer o reintegrar"):
            st.markdown("- FE por comprometer o reintegrar")
            st.markdown("- Deuda por comprometer")
            st.markdown("- LD y EE por comprometer")

        with st.expander("C.4 Saldo Neto"):
            st.markdown("- Etiquetado estatal")
            with st.expander("Libre disposición"):
                st.markdown("- Ramos Generales")
                st.markdown("- Otros Ramos")

    st.markdown("</div>", unsafe_allow_html=True)
