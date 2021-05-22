import streamlit as st
import streamlit_pages as pages

from pathlib import Path

PAGES = {
    "Home": lambda: st.markdown(Path("README.md").read_text()),
    "Ace Editor": pages.ace,
    "Elements": pages.elements,
    "Pandas Profiling": pages.pandas_profiling,
}


def main():
    params = st.experimental_get_query_params()
    page_names = tuple(PAGES.keys())
    page_lower = [page.replace(" ", "-").lower() for page in PAGES.keys()]

    try:
        page_default = page_lower.index(params["p"][0])
    except (KeyError, ValueError):
        page_default = 0

    with st.sidebar:
        st.title("🖼️ Streamlit Gallery")
        page_name = st.radio("", page_names, page_default)
        st.write("---")
    
    PAGES[page_name]()


if __name__ == "__main__":
    st.set_page_config(page_title="Okld Gallery", layout="wide")
    main()
