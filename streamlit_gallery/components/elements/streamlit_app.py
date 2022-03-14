import json
import streamlit as st

from pathlib import Path
from streamlit import session_state as state
from streamlit_elements import elements, sync, event

from .dashboard import Dashboard, Editor, Card, DataGrid, Radar, Pie, Player


def main():
    st.write(
        """
        ✨ Streamlit Elements &nbsp; [![GitHub][github_badge]][github_link] [![PyPI][pypi_badge]][pypi_link]
        =====================

        Create a draggable and resizable dashboard in Streamlit, featuring Material UI widgets,
        Monaco editor (Visual Studio Code), Nivo charts, and more!

        [github_badge]: https://badgen.net/badge/icon/GitHub?icon=github&color=black&label
        [github_link]: https://github.com/okld/streamlit-elements

        [pypi_badge]: https://badgen.net/pypi/v/streamlit-elements?icon=pypi&color=black&label
        [pypi_link]: https://pypi.org/project/streamlit-elements
        """
    )

    with st.expander("GETTING STARTED"):
        st.write((Path(__file__).parent/"README.md").read_text())

    st.title("")

    if "dashboard" not in state:
        state.dashboard = Dashboard()

        state.editor = Editor(0, 0, 6, 11, min_w=3, min_h=3)
        state.editor.add_tab("Card content", Card.DEFAULT_CONTENT, "plaintext")
        state.editor.add_tab("Data grid", json.dumps(DataGrid.DEFAULT_ROWS, indent=2), "json")
        state.editor.add_tab("Radar chart", json.dumps(Radar.DEFAULT_DATA, indent=2), "json")
        state.editor.add_tab("Pie chart", json.dumps(Pie.DEFAULT_DATA, indent=2), "json")

        state.player = Player(0, 12, 6, 10, min_h=5)
        state.pie = Pie(6, 0, 6, 7, min_w=3, min_h=4)
        state.radar = Radar(12, 7, 3, 7, min_w=2, min_h=4)
        state.card = Card(6, 7, 3, 7, min_w=2, min_h=4)
        state.data_grid = DataGrid(6, 13, 6, 7, min_h=4)

    with elements("demo"):
        event.on_hotkey("ctrl+s", sync(), bind_inputs=True, override_default=True)

        with state.dashboard(row_height=57):
            state.editor()
            state.player()
            state.pie(state.editor.get_content("Pie chart"))
            state.radar(state.editor.get_content("Radar chart"))
            state.card(state.editor.get_content("Card content"))
            state.data_grid(state.editor.get_content("Data grid"))


if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()
