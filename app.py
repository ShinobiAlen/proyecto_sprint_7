import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Análisis de Vehículos", layout="wide")

# Título
st.title("🚗 Análisis del Mercado de Vehículos Usados")
st.markdown("""
Explora tendencias de precios, kilometraje y condiciones de vehículos en el mercado.
""")

# Cargar datos
df = pd.read_csv('vehicles_us.csv')

# =========================
# 🎛️ FILTROS
# =========================
st.subheader("🎛️ Filtros")

price_range = st.slider(
    "Rango de precio",
    int(df['price'].min()),
    int(df['price'].max()),
    (5000, 30000)
)

condition = st.multiselect(
    "Condición del vehículo",
    options=df['condition'].dropna().unique(),
    default=df['condition'].dropna().unique()
)

# Aplicar filtros
filtered_df = df[
    (df['price'] >= price_range[0]) &
    (df['price'] <= price_range[1]) &
    (df['condition'].isin(condition))
]

# Mostrar cantidad de datos
st.write(f"Mostrando {len(filtered_df)} vehículos filtrados")

# =========================
# 📊 MÉTRICAS
# =========================
st.metric("Precio promedio", f"${int(filtered_df['price'].mean())}")

# =========================
# 📈 GRÁFICA PRINCIPAL
# =========================
fig = px.scatter(
    filtered_df,
    x="odometer",
    y="price",
    color="condition",
    title="Precio vs Kilometraje"
)

st.plotly_chart(fig)

# =========================
# 📊 GRÁFICA EXTRA
# =========================
fig_box = px.box(
    filtered_df,
    x="condition",
    y="price",
    title="Distribución de precios por condición"
)

st.plotly_chart(fig_box)

st.divider()

# =========================
# 📌 INSIGHTS
# =========================
st.subheader("📌 Insights clave")

st.markdown("""
- Los vehículos con menor kilometraje tienden a tener precios más altos.
- Las condiciones "like new" concentran los precios premium.
- Existe alta dispersión de precios en vehículos usados.
""")

# =========================
# 📋 DATASET
# =========================
st.write("Vista previa del dataset filtrado")
st.dataframe(filtered_df.head())

# =========================
# 🔍 EXTRAS INTERACTIVOS
# =========================
if st.checkbox("Mostrar histograma del odómetro"):
    fig_hist = px.histogram(filtered_df, x="odometer")
    st.plotly_chart(fig_hist)

if st.checkbox("Relación precio vs odómetro (extra)"):
    fig_scatter = px.scatter(filtered_df, x="odometer", y="price")
    st.plotly_chart(fig_scatter)
