import requests
import streamlit as st

from pathlib import Path
from streamlit_quill import st_quill


def main():
    st.markdown(requests.get("https://raw.githubusercontent.com/okld/streamlit-quill/master/README.md").text)
    demo_container = st.beta_container()
    st.write("---")

    with st.beta_expander("USAGE"):
        st.help(st_quill)
    
    with st.beta_expander("SOURCE"):
        st.code(Path(__file__).read_text())
    
    with demo_container:
        demo()


def demo():
    st.sidebar.title("⚙️ Parameters")

    content = st_quill(
        placeholder=st.sidebar.text_input("Placeholder", "Placeholder text."),
        html=st.sidebar.checkbox("Return HTML", False),
        readonly=st.sidebar.checkbox("Read only", False),
        key="quill",
    )

    st.write(content)


if __name__ == "__main__":
    main()
