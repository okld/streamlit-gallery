import streamlit as st

from streamlit_discourse import st_discourse
from streamlit_gallery.utils.readme import readme


def main():
    with readme("streamlit-discourse", st_discourse, __file__):
        st_discourse("discuss.streamlit.io", 8061, key="discourse")


if __name__ == "__main__":
    main()
