import json

from streamlit_elements import mui, nivo
from .dashboard import Dashboard


class Radar(Dashboard.Item):

    DEFAULT_DATA = [
        { "taste": "fruity", "chardonay": 93, "carmenere": 61, "syrah": 114 },
        { "taste": "bitter", "chardonay": 91, "carmenere": 37, "syrah": 72 },
        { "taste": "heavy", "chardonay": 56, "carmenere": 95, "syrah": 99 },
        { "taste": "strong", "chardonay": 64, "carmenere": 90, "syrah": 30 },
        { "taste": "sunny", "chardonay": 119, "carmenere": 94, "syrah": 103 },
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._theme = {
            "dark": {
                "background": "#252526",
                "textColor": "#FAFAFA",
                "tooltip": {
                    "container": {
                        "background": "#3F3F3F",
                        "color": "FAFAFA",
                    }
                }
            },
            "light": {
                "background": "#FFFFFF",
                "textColor": "#31333F",
                "tooltip": {
                    "container": {
                        "background": "#FFFFFF",
                        "color": "#31333F",
                    }
                }
            }
        }

    def __call__(self, json_data):
        data = json.loads(json_data)

        with mui.paper(key=self._key, sx={"display": "flex", "flexDirection": "column"}, elevation=3):
            with self.title_bar():
                mui.icon.radar()
                mui.typography("Radar chart", sx={"flex": 1})

            with mui.box(sx={"flex": 1, "minHeight": 0}):
                nivo.radar(
                    data=data,
                    theme=self._theme["dark" if self._dark_mode else "light"],
                    keys=[ "chardonay", "carmenere", "syrah" ],
                    index_by="taste",
                    value_format=">-.2f",
                    margin={ "top": 70, "right": 80, "bottom": 40, "left": 80 },
                    border_color={ "from": "color" },
                    grid_label_offset=36,
                    dot_size=10,
                    dot_color={ "theme": "background" },
                    dot_border_width=2,
                    motion_config="wobbly",
                    legends=[
                        {
                            "anchor": "top-left",
                            "direction": "column",
                            "translateX": -50,
                            "translateY": -40,
                            "itemWidth": 80,
                            "itemHeight": 20,
                            "itemTextColor": "#999",
                            "symbolSize": 12,
                            "symbolShape": "circle",
                            "effects": [
                                {
                                    "on": "hover",
                                    "style": {
                                        "itemTextColor": "#000"
                                    }
                                }
                            ]
                        }
                    ]
                )
