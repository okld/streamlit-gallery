import requests
import streamlit as st

from pathlib import Path
from streamlit_ace import st_ace, KEYBINDINGS, LANGUAGES, THEMES


def main():
    st.markdown(requests.get("https://raw.githubusercontent.com/okld/streamlit-ace/master/README.md").text)
    demo_container = st.beta_container()
    st.write("---")

    with st.beta_expander("USAGE"):
        st.help(st_ace)
    
    with st.beta_expander("SOURCE"):
        st.code(Path(__file__).read_text())
    
    with demo_container:
        demo()


def demo():
    st.sidebar.title("⚙️ Parameters")


    with st.beta_container():
        content = st_ace(
            placeholder=st.sidebar.text_input("Editor placeholder", value="Write your code here"),
            language=st.sidebar.selectbox("Language mode", options=LANGUAGES, index=121),
            theme=st.sidebar.selectbox("Theme", options=THEMES, index=35),
            keybinding=st.sidebar.selectbox("Keybinding mode", options=KEYBINDINGS, index=3),
            font_size=st.sidebar.slider("Font size", 5, 24, 14),
            tab_size=st.sidebar.slider("Tab size", 1, 8, 4),
            show_gutter=st.sidebar.checkbox("Show gutter", value=True),
            show_print_margin=st.sidebar.checkbox("Show print margin", value=False),
            wrap=st.sidebar.checkbox("Wrap enabled", value=False),
            auto_update=st.sidebar.checkbox("Auto update", value=False),
            readonly=st.sidebar.checkbox("Read-only", value=False),
            key="ace",
        )

    st.write(content)


if __name__ == "__main__":
    main()
