import requests
import pandas as pd
import pandas_profiling
import streamlit as st

from pathlib import Path
from streamlit_pandas_profiling import st_profile_report


def main():
    st.markdown(requests.get("https://raw.githubusercontent.com/okld/streamlit-pandas-profiling/master/README.md").text)

    dataset = "https://storage.googleapis.com/tf-datasets/titanic/train.csv"

    df = pd.read_csv(dataset)
    pr = df.profile_report(explorative=True)

    st.write(df)
    st.sidebar.write(f"🔗 [Titanic dataset]({dataset})")

    with st.beta_expander("REPORT", expanded=True):
        st_profile_report(pr)
    
    with st.beta_expander("USAGE"):
        st.help(st_profile_report)
    
    with st.beta_expander("SOURCE"):
        st.code(Path(__file__).read_text())


if __name__ == "__main__":
    main()
