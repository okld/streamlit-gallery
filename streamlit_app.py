import streamlit as st
from typing import Callable
from streamlit_gallery import apps, components

PAGE_PARAM = "p"
CONTENT = {
    "Applications": {
        "Streamlit gallery": apps.gallery,
    },
    "Components": {
        "Ace editor": components.ace_editor,
        "Discourse": components.discourse,
        "Disqus": components.disqus,
        "Pandas profiling": components.pandas_profiling,
        "Quill editor": components.quill_editor,
        "React player": components.react_player,
    },
}


def main():
    query_params = st.experimental_get_query_params()
    page_param = query_params[PAGE_PARAM][0] if PAGE_PARAM in query_params else "streamlit-gallery"
    page_selected = None

    with st.sidebar:
        st.title("🎈 Okld's Gallery")
        st.write("")

        for category_name, pages in CONTENT.items():
            category_expander = st.sidebar.expander(category_name.upper(), expanded=True)

            for page_name, page_function in pages.items():
                page_key = page_name.replace(" ", "-").lower()

                st.session_state[page_key] = (page_key == page_param)

                if category_expander.checkbox(
                    page_name, False,
                    key=page_key,
                    on_change=select_page,
                    args=[page_key]
                ):
                    page_selected = page_function

    if isinstance(page_selected, Callable):
        page_selected()


def select_page(page_key):
    if page_key in st.session_state and st.session_state[page_key]:
        query_params = st.experimental_get_query_params()
        query_params[PAGE_PARAM] = page_key

        st.experimental_set_query_params(**query_params)


if __name__ == "__main__":
    st.set_page_config(page_title="Streamlit Gallery by Okld", page_icon="🎈", layout="wide")
    main()
