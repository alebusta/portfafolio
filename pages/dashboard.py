import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configuración de la página
st.set_page_config(
    page_title="Dashboard Organizacional",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
<style>
    /* Ocultar específicamente la navegación de páginas en el sidebar */
    [data-testid="stSidebarNav"] {
        display: none !important;
    }
    
    /* Mantener el resto del sidebar visible */
    [data-testid="stSidebar"] {
        display: flex;
    }
    
    /* Asegurar que el contenido personalizado del sidebar sea visible */
    [data-testid="stSidebar"] .element-container {
        display: block !important;
    }
</style>
""", unsafe_allow_html=True)

# CSS personalizado para hacer el dashboard más atractivo
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
    }
    .metric-card {
        background: linear-gradient(45deg, #f093fb 0%, #f5576c 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    .stSelectbox > div > div {
        background-color: #f0f2f6;
    }
</style>
""", unsafe_allow_html=True)

# Título principal
st.markdown("""
<div class="main-header">
    <h1>🚀 Dashboard Organizacional TheQaiCompany</h1>
    <p>Análisis en tiempo real de métricas empresariales</p>
</div>
""", unsafe_allow_html=True)

# Sidebar para filtros
st.sidebar.header("🎛️ Filtros")
fecha_inicio = st.sidebar.date_input("Fecha inicio", datetime(2024, 1, 1))
fecha_fin = st.sidebar.date_input("Fecha fin", datetime(2024, 12, 31))
departamento = st.sidebar.selectbox("Departamento", ["Todos", "Ventas", "Marketing", "IT", "RRHH", "Finanzas"])

# Generar datos ficticios
@st.cache_data
def generar_datos():
    # Datos de ventas mensuales
    meses = pd.date_range(start='2024-01-01', end='2024-12-31', freq='M')
    ventas_data = {
        'Fecha': meses,
        'Ventas': np.random.normal(100000, 20000, len(meses)),
        'Objetivo': [120000] * len(meses)
    }
    df_ventas = pd.DataFrame(ventas_data)
    df_ventas['Ventas'] = np.maximum(df_ventas['Ventas'], 50000)  # Evitar valores negativos
    
    # Datos de empleados por departamento
    departamentos = ['Ventas', 'Marketing', 'IT', 'RRHH', 'Finanzas', 'Operaciones']
    empleados_data = {
        'Departamento': departamentos,
        'Empleados': [45, 32, 28, 15, 22, 38],
        'Satisfaccion': [4.2, 4.5, 4.8, 4.1, 4.3, 4.0]
    }
    df_empleados = pd.DataFrame(empleados_data)
    
    # Datos de productos más vendidos
    productos = ['Producto A', 'Producto B', 'Producto C', 'Producto D', 'Producto E']
    productos_data = {
        'Producto': productos,
        'Ventas': [230000, 180000, 150000, 120000, 90000],
        'Margen': [25, 30, 20, 35, 28]
    }
    df_productos = pd.DataFrame(productos_data)
    
    # Datos de performance regional
    regiones = ['Norte', 'Sur', 'Este', 'Oeste', 'Centro']
    regiones_data = {
        'Region': regiones,
        'Ventas': [320000, 280000, 350000, 240000, 300000],
        'Clientes': [450, 380, 520, 320, 420]
    }
    df_regiones = pd.DataFrame(regiones_data)
    
    return df_ventas, df_empleados, df_productos, df_regiones

df_ventas, df_empleados, df_productos, df_regiones = generar_datos()

# Métricas principales
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <h3>💰 Ventas Totales</h3>
        <h2>$1.2M</h2>
        <p>↗️ +15% vs mes anterior</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h3>👥 Empleados</h3>
        <h2>180</h2>
        <p>↗️ +5 nuevos este mes</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <h3>🎯 Satisfacción</h3>
        <h2>4.3/5</h2>
        <p>↗️ +0.2 vs trimestre anterior</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <h3>📈 Crecimiento</h3>
        <h2>23%</h2>
        <p>↗️ Anual proyectado</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Primera fila de gráficos
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Evolución de Ventas vs Objetivo")
    fig_ventas = go.Figure()
    
    fig_ventas.add_trace(go.Scatter(
        x=df_ventas['Fecha'],
        y=df_ventas['Ventas'],
        mode='lines+markers',
        name='Ventas Reales',
        line=dict(color='#ff6b6b', width=3),
        marker=dict(size=8)
    ))
    
    fig_ventas.add_trace(go.Scatter(
        x=df_ventas['Fecha'],
        y=df_ventas['Objetivo'],
        mode='lines',
        name='Objetivo',
        line=dict(color='#4ecdc4', width=2, dash='dash')
    ))
    
    fig_ventas.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#2c3e50'),
        height=400,
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    fig_ventas.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)')
    fig_ventas.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)')
    
    st.plotly_chart(fig_ventas, use_container_width=True)

with col2:
    st.subheader("👥 Distribución de Empleados por Departamento")
    fig_empleados = px.pie(
        df_empleados, 
        values='Empleados', 
        names='Departamento',
        color_discrete_sequence=px.colors.qualitative.Set3,
        hole=0.4
    )
    
    fig_empleados.update_traces(
        textposition='inside', 
        textinfo='percent+label',
        hovertemplate='<b>%{label}</b><br>Empleados: %{value}<br>Porcentaje: %{percent}<extra></extra>'
    )
    
    fig_empleados.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#2c3e50'),
        height=400,
        showlegend=True,
        legend=dict(orientation="v", yanchor="middle", y=0.5, xanchor="left", x=1.05)
    )
    
    st.plotly_chart(fig_empleados, use_container_width=True)

# Segunda fila de gráficos
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏆 Top Productos por Ventas")
    fig_productos = px.bar(
        df_productos,
        x='Ventas',
        y='Producto',
        orientation='h',
        color='Margen',
        color_continuous_scale='Viridis',
        text='Ventas'
    )
    
    fig_productos.update_traces(
        texttemplate='$%{text:,.0f}',
        textposition='outside',
        hovertemplate='<b>%{y}</b><br>Ventas: $%{x:,.0f}<br>Margen: %{marker.color}%<extra></extra>'
    )
    
    fig_productos.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#2c3e50'),
        height=400,
        yaxis={'categoryorder':'total ascending'},
        coloraxis_colorbar=dict(title="Margen (%)")
    )
    
    fig_productos.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)')
    fig_productos.update_yaxes(showgrid=False)
    
    st.plotly_chart(fig_productos, use_container_width=True)

with col2:
    st.subheader("🌍 Performance por Región")
    fig_regiones = go.Figure()
    
    # Barras para ventas
    fig_regiones.add_trace(go.Bar(
        name='Ventas ($)',
        x=df_regiones['Region'],
        y=df_regiones['Ventas'],
        yaxis='y',
        marker_color='rgba(55, 83, 109, 0.7)',
        text=df_regiones['Ventas'],
        texttemplate='$%{text:,.0f}',
        textposition='outside'
    ))
    
    # Línea para clientes
    fig_regiones.add_trace(go.Scatter(
        name='Clientes',
        x=df_regiones['Region'],
        y=df_regiones['Clientes'],
        yaxis='y2',
        mode='lines+markers',
        marker=dict(color='rgba(255, 107, 107, 0.8)', size=10),
        line=dict(color='rgba(255, 107, 107, 0.8)', width=3)
    ))
    
    fig_regiones.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#2c3e50'),
        height=400,
        yaxis=dict(
            title="Ventas ($)",
            side="left"
        ),
        yaxis2=dict(
            title="Número de Clientes",
            side="right",
            overlaying="y"
        ),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    fig_regiones.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)')
    fig_regiones.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)')
    
    st.plotly_chart(fig_regiones, use_container_width=True)

# Sección de insights
st.markdown("---")
st.subheader("💡 Insights Clave")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("🎯 **Objetivo de Ventas**: Estamos un 15% por encima del objetivo mensual, con una tendencia positiva sostenida.")

with col2:
    st.success("🚀 **Mejor Departamento**: IT lidera en satisfacción con 4.8/5, seguido de Marketing con 4.5/5.")

with col3:
    st.warning("📊 **Oportunidad**: La región Oeste tiene el menor rendimiento y podría beneficiarse de estrategias focalizadas.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p>Dashboard con datos ficitios para efectos demostrativos</p>
    <p>Última actualización: {} 📅</p>
</div>
""".format(datetime.now().strftime("%d/%m/%Y %H:%M")), unsafe_allow_html=True)