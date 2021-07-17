import re
import requests
import streamlit as st

from contextlib import contextmanager
from pathlib import Path

_filter_share = re.compile(r"^.*\[share_\w+\].*$", re.MULTILINE)


@contextmanager
def readme(project, usage=None, source=None):
    content = requests.get(f"https://raw.githubusercontent.com/okld/{project}/main/README.md").text
    st.markdown(_filter_share.sub("", content))

    demo = st.beta_container()

    if usage or source:
        st.write("---")

    if usage:
        with st.beta_expander("USAGE"):
            st.help(usage)

    if source:
        with st.beta_expander("SOURCE"):
            st.code(Path(source).read_text())

    with demo:
        yield


def st_query_radio(label, param, options, key=None):
    key = f"st_query_radio.{key or param}"

    choice = st.experimental_get_query_params().get(param, ("",))[0]
    choice = choice.replace("-", " ").title()

    def on_change():
        params = st.experimental_get_query_params()
        params[param] = st.session_state[key].replace(" ", "-").lower()

        st.experimental_set_query_params(**params)

    st.session_state[key] = choice if choice in options else next(iter(options))
    st.sidebar.radio(label, tuple(options.keys()), on_change=on_change, key=key)

    return options[st.session_state[key]]
