import streamlit as st

# 1. CONFIGURACIÓN DE LA PÁGINA Y ESTILOS
st.set_page_config(page_title="MarketLogic RA2 - Validador", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 8px; height: 3em; background-color: #007bff; color: white; font-weight: bold; }
    .guide-box { background-color: #e9ecef; padding: 15px; border-radius: 10px; border-left: 5px solid #007bff; margin-bottom: 20px; }
    .step-header { color: #1f4e79; }
    </style>
""", unsafe_allow_html=True)

# 2. TÍTULO Y CONTEXTO
st.title("🚀 MarketLogic RA2: Validador de Negocios")
st.markdown("**Módulo:** Simulación Empresarial | **Evaluación:** RA2 - Análisis de Mercado")
st.divider()

# 3. NAVEGACIÓN POR PASOS (MEJORA: ANDAMIAJE Y WIZARD)
st.sidebar.header("📋 Fases de Evaluación")
paso = st.sidebar.radio("Progreso:", [
    "1. Idea de Negocio", 
    "2. Análisis del Entorno (PESTEL)", 
    "3. Competencia y Barreras", 
    "4. Resultado Final"
])

# Inicialización de la memoria de la sesión
if 'datos' not in st.session_state:
    st.session_state.datos = {'idea': '', 'entorno': '', 'competencia': '', 'feedback': ''}

# --- PASO 1: IDEA ---
if paso == "1. Idea de Negocio":
    st.header("1️⃣ Definición de la Idea")
    st.markdown("""
    <div class="guide-box">
    <strong>💡 Preguntas guía:</strong><br>
    ¿Qué necesidad específica has detectado? ¿Quién es tu público objetivo (target)? ¿Cuál es tu propuesta de valor única?
    </div>
    """, unsafe_allow_html=True)
    st.session_state.datos['idea'] = st.text_area("Describe tu propuesta de negocio:", value=st.session_state.datos['idea'], height=200)

# --- PASO 2: ENTORNO ---
elif paso == "2. Análisis del Entorno (PESTEL)":
    st.header("2️⃣ Factores del Entorno")
    st.markdown("""
    <div class="guide-box">
    <strong>💡 Preguntas guía:</strong><br>
    ¿Existen leyes que afecten a tu sector? ¿Cómo influye la situación económica actual (inflación, tipos de interés)? ¿Qué tendencias sociales o tecnológicas favorecen tu idea?
    </div>
    """, unsafe_allow_html=True)
    st.session_state.datos['entorno'] = st.text_area("Análisis PESTEL:", value=st.session_state.datos['entorno'], height=200)

# --- PASO 3: COMPETENCIA ---
elif paso == "3. Competencia y Barreras":
    st.header("3️⃣ Competencia y Barreras de Entrada")
    st.markdown("""
    <div class="guide-box">
    <strong>💡 Preguntas guía:</strong><br>
    ¿Quiénes son tus competidores directos? ¿Qué te diferencia de ellos? ¿Qué dificultades legales o económicas impiden que otros copien tu idea fácilmente?
    </div>
    """, unsafe_allow_html=True)
    st.session_state.datos['competencia'] = st.text_area("Estudio de mercado:", value=st.session_state.datos['competencia'], height=200)

# --- PASO 4: EVALUACIÓN ---
elif paso == "4. Resultado Final":
    st.header("4️⃣ Informe y Feedback de la IA")
    
    if st.button("Evaluar mi Proyecto"):
        if st.session_state.datos['idea'] and st.session_state.datos['competencia']:
            with st.spinner('La IA está analizando tu lógica de mercado...'):
                # Simulación de Feedback basado en el RA2[cite: 1]
                # En una versión con API conectada, aquí iría la respuesta dinámica
                st.session_state.datos['feedback'] = (
                    "✅ ANÁLISIS DE LA IA:\n\n"
                    "1. LÓGICA: Has seguido los pasos correctos para identificar tu nicho.\n"
                    "2. COHERENCIA: Las conclusiones sobre la competencia son razonables.\n"
                    "3. RECOMENDACIÓN: Para el RA2, deberías detallar más las barreras económicas (inversión inicial)."
                )
                st.success("Evaluación completada")
        else:
            st.warning("⚠️ Por favor, completa los campos de 'Idea' y 'Competencia' para poder evaluar.")

    if st.session_state.datos['feedback']:
        st.subheader("Feedback del Tutor Virtual:")
        st.info(st.session_state.datos['feedback'])
        
        # MEJORA: EXPORTACIÓN DE INFORME[cite: 1]
        reporte_texto = f"""
        INFORME DE EVALUACIÓN - SIMULACIÓN EMPRESARIAL (RA2)
        ----------------------------------------------------
        IDEA: {st.session_state.datos['idea']}
        ENTORNO: {st.session_state.datos['entorno']}
        COMPETENCIA: {st.session_state.datos['competencia']}
        ----------------------------------------------------
        FEEDBACK IA:
        {st.session_state.datos['feedback']}
        """
        st.download_button(
            label="📥 Descargar Informe Final (TXT)",
            data=reporte_texto,
            file_name="evaluacion_mercado_RA2.txt",
            mime="text/plain"
        )
