import streamlit as st

from streamlit_pages.utils import readme
from streamlit_quill import st_quill


def main():
    with readme("streamlit-quill", st_quill, __file__):
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
