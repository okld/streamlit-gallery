import requests
import streamlit as st

from pathlib import Path
from streamlit_discourse import st_discourse


def main():
    st.markdown(requests.get("https://raw.githubusercontent.com/okld/streamlit-discourse/main/README.md").text)
    demo_container = st.beta_container()
    st.write("---")

    with st.beta_expander("USAGE"):
        st.help(st_discourse)
    
    with st.beta_expander("SOURCE"):
        st.code(Path(__file__).read_text())
    
    with demo_container:
        demo()


def demo():
    with st.beta_expander("DISCOURSE", expanded=True):
        st_discourse("discuss.streamlit.io", 8061, key="discourse")


if __name__ == "__main__":
    main()
