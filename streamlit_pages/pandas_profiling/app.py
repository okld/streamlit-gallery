import requests
import pandas as pd
import pandas_profiling
import streamlit as st

from pathlib import Path
from streamlit_pandas_profiling import st_profile_report


def main():
    st.markdown(requests.get("https://raw.githubusercontent.com/okld/streamlit-pandas-profiling/main/README.md").text)
    demo_container = st.beta_container()
    st.write("---")

    with st.beta_expander("USAGE"):
        st.help(st_profile_report)
    
    with st.beta_expander("SOURCE"):
        st.code(Path(__file__).read_text())

    with demo_container:
        demo()


def demo():
    dataset = "https://storage.googleapis.com/tf-datasets/titanic/train.csv"

    df = pd.read_csv(dataset)
    pr = df.profile_report(explorative=True)

    st.write(df)
    st.sidebar.write(f"🔗 [Titanic dataset]({dataset})")

    if st.button("Generate report"):
        with st.beta_expander("REPORT", expanded=True):
            st_profile_report(pr)


if __name__ == "__main__":
    main()
