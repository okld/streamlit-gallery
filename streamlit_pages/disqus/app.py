import streamlit as st

from streamlit_disqus import st_disqus
from streamlit_pages.utils import readme


def main():
    with readme("streamlit-disqus", st_disqus, __file__):
        st_disqus("streamlit-disqus-demo")


if __name__ == "__main__":
    main()
