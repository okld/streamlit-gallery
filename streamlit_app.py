import requests
import inspect
import streamlit as st
import streamlit_pages as pages

from pathlib import Path

PAGES = {
    "Home": {
        "readme": None,
        "source": lambda: st.markdown(Path("README.md").read_text()),
    },
    "Ace Editor": {
        "readme": "https://raw.githubusercontent.com/okld/streamlit-ace/master/README.md",
        "source": pages.ace,
    },
    "Elements": {
        "readme": "https://raw.githubusercontent.com/okld/streamlit-elements/main/README.md",
        "source": pages.elements,
    },
    "Pandas Profiling": {
        "readme": "https://raw.githubusercontent.com/okld/streamlit-pandas-profiling/master/README.md",
        "source": pages.pandas_profiling,
    }
}


def main():
    params = st.experimental_get_query_params()
    page_names = tuple(PAGES.keys())
    page_lower = [page.replace(" ", "_").lower() for page in PAGES.keys()]

    try:
        page_default = page_lower.index(params["p"][0])
    except (KeyError, ValueError):
        page_default = 0

    with st.sidebar:
        st.title("🖼️ Streamlit Gallery")
        page_name = st.radio("", page_names, page_default)
        st.write("---")
    
    page = PAGES[page_name]
    page["source"]()

    if page_name != "Home":
        st.write("---")

        with st.beta_expander("README"):
            st.markdown(requests.get(page["readme"]).text)
    
        with st.beta_expander("SOURCE"):
            st.code(Path(inspect.getsourcefile(page["source"])).read_text())




if __name__ == "__main__":
    st.set_page_config(page_title="Showcase", layout="wide")
    main()
