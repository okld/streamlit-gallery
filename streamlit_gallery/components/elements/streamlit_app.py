import json
import streamlit as st

from streamlit import session_state as state
from streamlit_elements import elements, sync, event

from .dashboard import Dashboard, Editor, Card, DataGrid, Radar, Pie, Player


def main():
    st.header("✨ Streamlit Elements")

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
