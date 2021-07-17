import streamlit as st
import streamlit_gallery as gallery
from streamlit_gallery.utils import st_query_radio


def main():
    st.sidebar.title("🎈 Okld's Gallery")
    st_query_radio("", "p", {
        "Home": gallery.home,
        "Ace Editor": gallery.ace,
        "Discourse": gallery.discourse,
        "Disqus": gallery.disqus,
        "Elements": gallery.elements,
        "Pandas Profiling": gallery.pandas_profiling,
        "Quill Editor": gallery.quill,
        "React Player": gallery.player,
    })()


if __name__ == "__main__":
    st.set_page_config(page_title="Okld's Gallery", page_icon="🎈", layout="wide")
    main()
