import streamlit as st
import os
import webbrowser

# Configuración más restrictiva de la página
st.set_page_config(
    page_title="Portfolio | Data Science & AI",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)

# Nuevo CSS más agresivo para ocultar la sidebar y el botón
st.markdown("""
<style>
    /* Ocultar completamente el sidebar y su botón */
    .css-1d391kg, .css-1siy2j7, .css-ccm30r {
        display: none !important;
    }
    
    /* Ocultar el botón de hamburguesa */
    .st-emotion-cache-h5rgaw, .st-emotion-cache-1egp75f {
        display: none !important;
        visibility: hidden !important;
        width: 0 !important;
        height: 0 !important;
        position: absolute !important;
        left: -9999px !important;
    }
    
    /* Remover cualquier espacio reservado para el sidebar */
    .main .block-container {
        max-width: 100%;
        padding-left: 1rem;
        padding-right: 1rem;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Asegurar que el contenido ocupe todo el ancho */
    .stApp {
        margin: 0;
        padding: 0;
        width: 100vw !important;
    }
    
    /* Ocultar otros elementos de Streamlit */
    #MainMenu, header, footer, [data-testid="stToolbar"] {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)

# CSS personalizado inspirado en el estilo de Jony Ive
st.markdown("""
<style>
    /* Ocultar elementos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Fondo y tipografía */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #d7d7d9 100%);
        font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Contenedor principal */
    .main-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 4rem 2rem;
        text-align: center;
    }
    
    /* Título principal */
    .hero-title {
        font-size: 4rem;
        font-weight: 200;
        letter-spacing: -0.02em;
        color: #1a1a1a;
        margin-bottom: 1rem;
        line-height: 1.1;
    }
    
    /* Subtítulo */
    .hero-subtitle {
        font-size: 1.5rem;
        font-weight: 300;
        color: #666;
        margin-bottom: 4rem;
        letter-spacing: 0.01em;
    }
    
    /* Grid de botones */
    .button-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 2rem;
        margin: 4rem 0;
        max-width: 900px;
        margin-left: auto;
        margin-right: auto;
    }
    
    /* Estilo de botones */
    .project-button {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 16px;
        padding: 1.8rem 1.5rem;  /* Reducido de 2.5rem 2rem */
        text-decoration: none;
        color: #1a1a1a;
        transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        cursor: pointer;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        margin-bottom: 1.5rem;  /* Añadido margen inferior */
        min-height: 200px;     /* Altura mínima fija */
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        justify-content: flex-start;
    }
    
    .project-button:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
        background: rgba(255, 255, 255, 0.95);
        text-decoration: none;
        color: #1a1a1a;
        z-index: 1;  /* Asegura que el botón hover aparezca por encima */
    }
    
    /* Estilos para los iconos */
    .project-icon {
        margin-bottom: 1.5rem;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: flex-start;
        width: 100%;
        align-self: flex-start; 
    }
    
    .project-icon svg {
        width: 40px;
        height: 40px;
        stroke: #1a1a1a;
        stroke-width: 2;
        stroke-linecap: round;
        stroke-linejoin: round;
        fill: none;
    }
    
    /* Títulos de proyectos */
    .project-title {
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        color: #1a1a1a;
    }
    
    /* Descripciones de proyectos */
    .project-description {
        font-size: 0.95rem;
        color: #666;
        line-height: 1.5;
        font-weight: 300;
    }
    
    /* Footer minimalista */
    .footer-section {
        margin-top: 6rem;
        padding-top: 3rem;
        border-top: 1px solid rgba(0, 0, 0, 0.1);
        color: #999;
        font-size: 0.9rem;
        font-weight: 300;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
        }
        
        .hero-subtitle {
            font-size: 1.2rem;
        }
        
        .button-grid {
            grid-template-columns: 1fr;
            gap: 1.5rem;
        }
        
        .project-button {
            padding: 2rem 1.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)


# Función load_lucide_icon

def load_lucide_icon(icon_name, size=24):
    # Ruta a la carpeta de iconos
    icons_dir = os.path.join(os.path.dirname(__file__), 'icons')
    icon_path = os.path.join(icons_dir, f"{icon_name}.svg")
    
    try:
        with open(icon_path, 'r') as f:
            svg_content = f.read()
            
        # Reemplazar los atributos de tamaño
        svg_content = svg_content.replace('width="24"', f'width="{size}"')
        svg_content = svg_content.replace('height="24"', f'height="{size}"')
        
        return svg_content
    except FileNotFoundError:
        print(f"Icon {icon_name} not found in {icons_dir}")
        return ""

# Función para crear botones de proyectos
def create_project_button(icon, title, description, key, url):
    icon_html = load_lucide_icon(icon, size=30)
    is_external = url.startswith('http')
    
    if is_external:
        link_url = url
        target = '_blank'
    else:
        # Para páginas internas, usa el formato correcto de Streamlit
        link_url = url if url.startswith('/') else f'{url}'
        target = '_self'
    
    button_html = f"""
    <div class="project-container">
        <a href="{link_url}" target="{target}" style="text-decoration: none; display: block;">
            <div class="project-button">
                <div class="project-icon">{icon_html}</div>
                <div class="project-title">{title}</div>
                <div class="project-description">{description}</div>
            </div>
        </a>
    </div>
    """
    return button_html

# JavaScript para manejar selección
#st.markdown("""
#<script>
#function selectProject(projectKey) {
#    // Esta función se puede expandir para navegar a diferentes páginas
#    console.log('Selected project:', projectKey);
#}
#</script>
#""", unsafe_allow_html=True)

# Contenido principal
st.markdown("""
<div class="main-container">
    <h1 class="hero-title">Data Science<br>& Artificial Intelligence</h1>
    <p class="hero-subtitle">Explorando el futuro a través de datos y algoritmos inteligentes. <br>Portafolio de posibilidades</p> 
       
</div>
""", unsafe_allow_html=True)


# Definir proyectos
projects = [
    {
        "icon": "chart-no-axes-combined",
        "title": "Visualizaciones Avanzadas",
        "description": "Dashboards interactivos con ECharts, gráficos dinámicos y análisis visual de datos complejos",
        "key": "charts",
        "url": "charts"
    },
    {
        "icon": "layout-dashboard",
        "title": "Dashboards Inteligentes",
        "description": "Panel de control integral con métricas en tiempo real y análisis predictivo",
        "key": "dashboard",
        "url": "dashboard"
    },
    {
        "icon": "telescope",
        "title": "Monitoreo de Tendencias",
        "description": "Seguimiento y análisis de tendencias en medios, redes y otras fuentes para decisiones informadas",
        "key": "portfolio",
        "url": "https://monitor-usa-latam.streamlit.app/"
    },
    {
        "icon": "bot-message-square",
        "title": "Chatbots & AI",
        "description": "Asistentes conversacionales inteligentes y soluciones de procesamiento de lenguaje natural",
        "key": "chatbots",
        "url": "chat"
    }
]


# Generar botones en 2 columnas
col1, col2 = st.columns(2)

# Dividir proyectos en dos grupos
half = len(projects) // 2
first_half = projects[:half + len(projects) % 2]  # Primera mitad + proyecto extra si impar
second_half = projects[half + len(projects) % 2:]

# Renderizar primera columna
with col1:
    for project in first_half:
        st.markdown(
            create_project_button(
                project["icon"],
                project["title"],
                project["description"],
                project["key"],
                project["url"]
            ),
            unsafe_allow_html=True
        )
        #st.switch_page(project["url"])  # Navegar a la página del proyecto al hacer clic

# Renderizar segunda columna
with col2:
    for project in second_half:
        st.markdown(
            create_project_button(
                project["icon"],
                project["title"],
                project["description"],
                project["key"],
                project["url"]
            ),
            unsafe_allow_html=True
        )


st.markdown("""
    </div>    
    <div class="footer-section">
        <p>Diseñado por @alebusta - 2025</p>
    </div>
</div>
""", unsafe_allow_html=True)


# CSS para ocultar los botones de Streamlit pero mantener funcionalidad
st.markdown("""
<style>
    .row-widget.stButton {
        display: none;
    }
</style>
""", unsafe_allow_html=True)

