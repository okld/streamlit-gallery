from streamlit_elements import media, mui, sync, lazy
from .dashboard import Dashboard

class Player(Dashboard.Item):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._url = "https://www.youtube.com/watch?v=CmSKVW1v0xM"

    def _set_url(self, event):
        self._url = event.target.value

    def __call__(self):
        with mui.paper(key=self._key, sx={"display": "flex", "flexDirection": "column"}, elevation=3):
            with self.title_bar(padding="10px 15px 10px 15px", dark_switcher=False):
                mui.icon.ondemand_video()
                mui.typography("Media player")

            with mui.stack(direction="row", spacing=2, justify_content="space-evenly", align_items="center", sx={"padding": "10px"}):
                mui.text_field(default_value=self._url, label="URL", variant="standard", sx={"flex": 0.97}, on_change=lazy(self._set_url))
                mui.icon_button(mui.icon.play_circle_filled, on_click=sync(), sx={"color": "primary.main"})

            media.player(self._url, controls=True, width="100%", height="100%")
