import streamlit as st
import pandas as pd
import joblib
import os

# Cabeçalho e layout

st.set_page_config(page_title="Churn Prediction App", layout="centered")
st.title("🤖 Previsão de Cancelamento de Clientes")
st.markdown("Este app utiliza um modelo de Machine Learning para prever se um cliente vai cancelar ou não baseado em seus dados.")

# Carregar o modelo treinado

MODEL_PATH = "outputs/models/modelo_random_forest.pkl"

@st.cache_resource
def carregar_modelo():
    return joblib.load(MODEL_PATH)

modelo = carregar_modelo()

# Formulário de entrada manual (exemplo simplificado)

st.subheader("🔢 Informe os dados do cliente")

sexo = st.selectbox("Sexo", ["Masculino", "Feminino"])
tempo_como_cliente = st.slider("Tempo como cliente (meses)", 0, 100, 12)
frequencia_uso = st.slider("Frequência de uso (vezes/mês)", 0, 50, 10)
ligacoes_callcenter = st.slider("Ligações para o call center (30 dias)", 0, 10, 2)
dias_atraso = st.slider("Dias de atraso no pagamento", 0, 30, 0)
assinatura = st.selectbox("Plano de assinatura", ["Basic", "Standard", "Premium"])
duracao_contrato = st.selectbox("Duração do contrato", ["Monthly", "Quarterly", "Annual"])
total_gasto = st.number_input("Total gasto (R$)", 0.0, 5000.0, 1000.0)
meses_ultima_interacao = st.slider("Meses desde a última interação", 0, 36, 6)
idade = st.slider("Idade do cliente", 18, 100, 35)

# Processar a entrada e fazer previsão

if st.button("🔍 Prever cancelamento"):
    # Preparar input como o modelo espera
    input_dict = {
        'idade': idade,
        'sexo': 1 if sexo == "Masculino" else 0,
        'tempo_como_cliente': tempo_como_cliente,
        'frequencia_uso': frequencia_uso,
        'ligacoes_callcenter': ligacoes_callcenter,
        'dias_atraso': dias_atraso,
        'total_gasto': total_gasto,
        'meses_ultima_interacao': meses_ultima_interacao,
        'assinatura_Premium': 1 if assinatura == "Premium" else 0,
        'assinatura_Standard': 1 if assinatura == "Standard" else 0,
        'duracao_contrato_Monthly': 1 if duracao_contrato == "Monthly" else 0,
        'duracao_contrato_Quarterly': 1 if duracao_contrato == "Quaterly" else 0
    }

    input_df = pd.DataFrame([input_dict])
    input_df = input_df[modelo.feature_names_in_]
    pred = modelo.predict(input_df)[0]
    prob = modelo.predict_proba(input_df)[0][1]

    if pred == 1:
        st.error(f"⚠️ Esse cliente tem ALTA chance de cancelar. Probabilidade: {prob:.2%}")
    else:
        st.success(f"🚀 Cliente com boa chance de permanecer. Probabilidade de churn: {prob:.2%}")


# Upload de CSV para previsões em lote

st.subheader("📁 Upload de Arquivo CSV")

arquivo = st.file_uploader("Envie um arquivo .csv com os dados dos clientes", type=["csv"])

if arquivo is not None:
    df_csv = pd.read_csv(arquivo)

    # Verifica se todas as colunas estão presentes
    colunas_esperadas = list(modelo.feature_names_in_)
    colunas_faltando = [col for col in colunas_esperadas if col not in df_csv.columns]

    if colunas_faltando:
        st.error(f"Colunas faltando no CSV: {colunas_faltando}")
    else:
        df_csv = df_csv[colunas_esperadas]
        preds = modelo.predict(df_csv)
        probs = modelo.predict_proba(df_csv)[:, 1]
        df_csv['Churn_Predito'] = preds
        df_csv['Probabilidade_Churn'] = probs

        st.success("Previsões realizadas com sucesso!")
        st.dataframe(df_csv)

        # Download do resultado
        csv_resultado = df_csv.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="🔹 Baixar resultados como CSV",
            data=csv_resultado,
            file_name="resultado_churn.csv",
            mime="text/csv"
        )
