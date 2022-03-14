from functools import partial
from streamlit_elements import mui, monaco, sync, lazy
from .dashboard import Dashboard


class Editor(Dashboard.Item):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._dark_theme = False
        self._index = 0
        self._tabs = {}
        self._editor_box_style = {
            "flex": 1,
            "minHeight": 0,
            "borderBottom": 1,
            "borderTop": 1,
            "borderColor": "divider"
        }

    def _change_tab(self, _, index):
        self._index = index

    def update_content(self, label, content):
        self._tabs[label]["content"] = content

    def add_tab(self, label, default_content, language):
        self._tabs[label] = { "content": default_content, "language": language }

    def get_content(self, label):
        return self._tabs[label]["content"]

    def __call__(self):
        with mui.paper(key=self._key, sx={"display": "flex", "flexDirection": "column"}, elevation=3):

            with self.title_bar("0px 15px 0px 15px"):
                mui.icon.terminal()
                mui.typography("Editor")

                with mui.tabs(value=self._index, on_change=self._change_tab, scroll_buttons=True, variant="scrollable", sx={"flex": 1}):
                    for label in self._tabs.keys():
                        mui.tab(label=label)

            for index, (label, tab) in enumerate(self._tabs.items()):
                with mui.box(sx=self._editor_box_style, hidden=(index != self._index)):
                    monaco.editor(
                        default_value=tab["content"],
                        language=tab["language"],
                        on_change=lazy(partial(self.update_content, label)),
                        theme="vs-dark" if self._dark_mode else "light",
                        options={
                            "wordWrap": True
                        }
                    )

            with mui.stack(direction="row", spacing=2, align_items="center", sx={"padding": "10px"}):
                mui.button("Apply", variant="contained", on_click=sync())
                mui.typography("Or press ctrl+s", sx={"flex": 1})
