import inspect
import textwrap

import streamlit as st

from demo_echarts import ST_DEMOS
from demo_pyecharts import ST_PY_DEMOS



def main():
    st.title("Demo de visualización de datos")

    with st.sidebar:
        st.header("Configuración")
        api_options = ("echarts", "pyecharts")
        selected_api = st.selectbox(
            label="Selecciona el demo de interés:",
            options=api_options,
        )

        page_options = (
            list(ST_PY_DEMOS.keys())
            if selected_api == "pyecharts"
            else list(ST_DEMOS.keys())
        )
        selected_page = st.selectbox(
            label="Choose an example",
            options=page_options,
        )
        demo, url = (
            ST_DEMOS[selected_page]
            if selected_api == "echarts"
            else ST_PY_DEMOS[selected_page]
        )

        if selected_api == "echarts":
            st.caption(
                """ECharts demos are extracted from https://echarts.apache.org/examples/en/index.html, 
            by copying/formattting the 'option' json object into st_echarts.
            Definitely check the echarts example page, convert the JSON specs to Python Dicts and you should get a nice viz."""
            )
        if selected_api == "pyecharts":
            st.caption(
                """Pyecharts demos are extracted from https://github.com/pyecharts/pyecharts-gallery,
            by copying the pyecharts object into st_pyecharts. 
            Pyecharts is still using ECharts 4 underneath, which is why the theming between st_echarts and st_pyecharts is different."""
            )

    demo()

    sourcelines, _ = inspect.getsourcelines(demo)
    with st.expander("Source Code"):
        st.code(textwrap.dedent("".join(sourcelines[1:])))
    st.markdown(f"Credit: {url}")


if __name__ == "__main__":
    st.set_page_config(
        page_title="Streamlit ECharts Demo", page_icon=":chart_with_upwards_trend:"
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
    main()
    with st.sidebar:
        st.markdown("---")
        st.markdown(
            '<h6>Elaborado con &nbsp<img src="https://streamlit.io/images/brand/streamlit-mark-color.png" alt="Streamlit logo" height="16">&nbsp adaptado de <a href="https://twitter.com/andfanilo">@andfanilo</a></h6>',
            unsafe_allow_html=True,
        )

