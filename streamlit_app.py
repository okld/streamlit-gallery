import streamlit as st
import streamlit_pages as pages

PAGES = {
    "Home": pages.home,
    "Ace Editor": pages.ace,
    "Discourse": pages.discourse,
    "Disqus": pages.disqus,
    "Elements": pages.elements,
    "Pandas Profiling": pages.pandas_profiling,
    "Quill Editor": pages.quill,
    "React Player": pages.player,
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
        st.title("🎈 Streamlit Gallery")
        page_name = st.selectbox("", page_names, page_default)
    
    PAGES[page_name]()


def google_analytics():
    st.sidebar.markdown(unsafe_allow_html=True, body=f"""
        <iframe height=0 srcdoc="
            <!-- Global site tag (gtag.js) - Google Analytics -->
            <script async src='https://www.googletagmanager.com/gtag/js?id=G-CGSM9DTBK8'></script>
            <script>
            window.parent.dataLayer = window.parent.dataLayer || [];
            function gtag() {{ window.parent.dataLayer.push(arguments); }}
            gtag('js', new Date());
            gtag('config', 'G-CGSM9DTBK8');
            </script>
        " />
    """)


if __name__ == "__main__":
    st.set_page_config(page_title="🎈 Okld's Gallery", layout="wide")
    google_analytics()
    main()
