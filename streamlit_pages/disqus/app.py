import requests
import streamlit as st

from pathlib import Path
from streamlit_disqus import st_disqus


def main():
    st.markdown(requests.get("https://raw.githubusercontent.com/okld/streamlit-disqus/main/README.md").text)
    demo_container = st.beta_container()
    st.write("---")

    with st.beta_expander("USAGE"):
        st.help(st_disqus)
    
    with st.beta_expander("SOURCE"):
        st.code(Path(__file__).read_text())
    
    with demo_container:
        demo()


def demo():
    with st.beta_expander("DISQUS", expanded=True):
        st_disqus("streamlit-disqus-demo")


if __name__ == "__main__":
    main()
