import streamlit as st
import pandas as pd
from datetime import datetime

# -------------------------------------------------
# CONFIGURACIÓN GENERAL
# -------------------------------------------------
st.set_page_config(
    page_title="Tarjeta Ejecutiva – Seguimiento al Gasto Público",
    layout="wide"
)

# -------------------------------------------------
# ESTILOS INSTITUCIONALES (AZUL / BLANCO)
# -------------------------------------------------
st.markdown("""
<style>
    .block-container { padding-top: 2rem; }
    h1, h2, h3 { color: #0B3C5D; }
    .stMetric { background-color: #F5F9FC; padding: 15px; border-radius: 10px; }
    .stExpander { border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# BARRA LATERAL – CONTROL EJECUTIVO
# -------------------------------------------------
with st.sidebar:
    st.header("⚙️ Configuración Ejecutiva")

    ejercicio = st.selectbox("Ejercicio fiscal", [2025])
    corte = st.selectbox("Corte de información", ["Diciembre", "Noviembre"])
    fuente = st.selectbox(
        "Fuente de datos",
        ["SQL Institucional", "API SHCP", "Archivo Excel"]
    )

    st.button("🔄 Actualizar información")

    st.divider()
    st.caption("Secretaría de Finanzas – Gobierno del Estado")

# -------------------------------------------------
# ENCABEZADO PRINCIPAL
# -------------------------------------------------
st.markdown("## Tarjeta Informativa Ejecutiva")
st.markdown("### Seguimiento al Gasto Público – Ejercicio 2025")

st.caption(
    f"Última actualización: {datetime.now().strftime('%d/%m/%Y %H:%M')}"
)

st.divider()

# -------------------------------------------------
# DATOS CONSOLIDADOS (SIMULADOS – luego reales)
# -------------------------------------------------
data = {
    "A": {
        "total": 1250,
        "A.1": 4800,
        "A.2": 3550
    },
    "B": {
        "total": 430,
        "B.1": 300,
        "B.2": 130
    },
    "C": {
        "total": 1680,
        "C.1": 620,
        "C.2": 820,
        "C.2.1": 300,
        "C.2.2": 220,
        "C.2.3": 300,
        "C.4": 240,
        "C.4.1": 140,
        "C.4.3": 100,
        "C.4.3.1": 60,
        "C.4.3.2": 40
    }
}

# -------------------------------------------------
# FUNCIÓN SEMÁFORO EJECUTIVO
# -------------------------------------------------
def semaforo(monto):
    if monto < 500:
        return "🟢 Riesgo bajo"
    elif monto < 1200:
        return "🟡 Riesgo medio"
    else:
        return "🔴 Riesgo alto"

# -------------------------------------------------
# TARJETAS EJECUTIVAS – NIVEL 1
# -------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "A. Subejercicio 2025",
        f"$ {data['A']['total']:,} MDP",
        "Brecha Modificado vs Devengado"
    )
    st.caption(semaforo(data["A"]["total"]))

with col2:
    st.metric(
        "B. Adecuaciones por revisar",
        f"$ {data['B']['total']:,} MDP",
        "Impacto potencial en el cierre"
    )
    st.caption("🟡 Riesgo administrativo")

with col3:
    st.metric(
        "C. Subejercicio estimado 2025",
        f"$ {data['C']['total']:,} MDP",
        "Presión presupuestaria futura"
    )
    st.caption(semaforo(data["C"]["total"]))

with col4:
    comprobacion = (
        data["A"]["total"]
        - data["C"]["C.1"]
        - data["C"]["C.2"]
        - data["C"]["C.4"]
    )
    st.metric(
        "Comprobación",
        f"$ {comprobacion:,} MDP",
        "Validación de cierre"
    )

st.divider()

# -------------------------------------------------
# NAVEGACIÓN POR RUBRO
# -------------------------------------------------
tabs = st.tabs([
    "A. Subejercicio 2025",
    "B. Adecuaciones",
    "C. Subejercicio estimado"
])

# -------------------------------------------------
# RUBRO A
# -------------------------------------------------
with tabs[0]:
    st.subheader("A. Subejercicio 2025")

    st.success(
        "El subejercicio observado corresponde a la diferencia efectiva "
        "entre el presupuesto modificado y el devengado."
    )

    with st.expander(f"A.1 Presupuesto Modificado | $ {data['A']['A.1']:,} MDP"):
        st.caption("Presupuesto ajustado vigente del ejercicio.")

    with st.expander(f"A.2 Presupuesto Devengado | $ {data['A']['A.2']:,} MDP"):
        st.caption("Ejecución presupuestaria reconocida.")

# -------------------------------------------------
# RUBRO B
# -------------------------------------------------
with tabs[1]:
    st.subheader("B. Adecuaciones por revisar")

    st.warning(
        "Adecuaciones pendientes de validación que pueden alterar "
        "el resultado final del ejercicio."
    )

    with st.expander(f"B.1 Suplementos | $ {data['B']['B.1']:,} MDP"):
        st.caption("Más detalles")

    with st.expander(f"B.2 Devoluciones | $ {data['B']['B.2']:,} MDP"):
        st.caption("Más detalles")

# -------------------------------------------------
# RUBRO C
# -------------------------------------------------
with tabs[2]:
    st.subheader("C. Subejercicio estimado 2025")

    st.error(
        "Estimación preliminar de recursos susceptibles de refrendo "
        "o reintegro al cierre del ejercicio."
    )

    with st.expander(f"C.1 Refrendos 2026 | $ {data['C']['C.1']:,} MDP"):
        st.caption("Más detalles")

    with st.expander(f"C.2 Saldos por comprometer o reintegrar | $ {data['C']['C.2']:,} MDP"):
        st.markdown(f"- **FE**: $ {data['C']['C.2.1']:,} MDP")
        st.markdown(f"- **Deuda**: $ {data['C']['C.2.2']:,} MDP")
        st.markdown(f"- **LD y EE**: $ {data['C']['C.2.3']:,} MDP")

    with st.expander(f"C.4 Saldo Neto | $ {data['C']['C.4']:,} MDP"):
        st.markdown(f"- **Etiquetado estatal**: $ {data['C']['C.4.1']:,} MDP")
        st.markdown(f"- **Libre disposición**: $ {data['C']['C.4.3']:,} MDP")
        st.markdown(f"  - Ramos Generales: $ {data['C']['C.4.3.1']:,} MDP")
        st.markdown(f"  - Otros Ramos: $ {data['C']['C.4.3.2']:,} MDP")

# -------------------------------------------------
# ANÁLISIS EJECUTIVO CONSOLIDADO
# -------------------------------------------------
st.divider()
st.subheader("Análisis Ejecutivo Consolidado")

with st.expander("Ver síntesis ejecutiva"):
    st.write(
        """
        El ejercicio fiscal 2025 presenta un subejercicio relevante,
        concentrado principalmente en recursos de libre disposición y
        fondos etiquetados estatales. La atención prioritaria debe centrarse
        en la validación de adecuaciones pendientes y en la definición
        oportuna de los recursos sujetos a refrendo o reintegro, con el fin
        de fortalecer la disciplina financiera y la planeación del ejercicio
        subsecuente.
        """
    )

# -------------------------------------------------
# EXPORTABLES EJECUTIVOS
# -------------------------------------------------
st.divider()
st.subheader("Productos ejecutivos")

c1, c2, c3 = st.columns(3)

with c1:
    st.button("📄 Generar ficha PDF")

with c2:
    st.button("📝 Nota ejecutiva Word")

with c3:
    st.button("📊 Descargar Excel consolidado")

