import pandas as pd
import pandas_profiling
import streamlit as st

from streamlit_gallery.utils import readme
from streamlit_pandas_profiling import st_profile_report


def main():
    with readme("streamlit-pandas-profiling", st_profile_report, __file__):
        dataset = "https://storage.googleapis.com/tf-datasets/titanic/train.csv"

        df = pd.read_csv(dataset)
        pr = df.profile_report(explorative=True)

        st.write(f"🔗 [Titanic dataset]({dataset})")
        st.write(df)

        if st.button("Generate report"):
            with st.beta_expander("REPORT", expanded=True):
                st_profile_report(pr)


if __name__ == "__main__":
    main()
