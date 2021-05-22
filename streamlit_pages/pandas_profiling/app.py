import pandas as pd
import streamlit as st

from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


def main():
    dataset = "https://storage.googleapis.com/tf-datasets/titanic/train.csv"

    df = pd.read_csv(dataset)
    pr = ProfileReport(df, explorative=True)

    st.write(df)
    st.sidebar.write(f"🔗 [Titanic dataset]({dataset})")

    with st.beta_expander("REPORT", expanded=True):
        st_profile_report(pr)


if __name__ == "__main__":
    main()
