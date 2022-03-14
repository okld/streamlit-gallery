import json

from streamlit_elements import nivo, mui
from .dashboard import Dashboard


class Pie(Dashboard.Item):

    DEFAULT_DATA = [
        { "id": "java", "label": "java", "value": 465, "color": "hsl(128, 70%, 50%)" },
        { "id": "rust", "label": "rust", "value": 140, "color": "hsl(178, 70%, 50%)" },
        { "id": "scala", "label": "scala", "value": 40, "color": "hsl(322, 70%, 50%)" },
        { "id": "ruby", "label": "ruby", "value": 439, "color": "hsl(117, 70%, 50%)" },
        { "id": "elixir", "label": "elixir", "value": 366, "color": "hsl(286, 70%, 50%)" }
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
                mui.icon.pie_chart()
                mui.typography("Pie chart", sx={"flex": 1})

            with mui.box(sx={"flex": 1, "minHeight": 0}):
                nivo.pie(
                    data=data,
                    theme=self._theme["dark" if self._dark_mode else "light"],
                    margin={ "top": 40, "right": 80, "bottom": 80, "left": 80 },
                    inner_radius=0.5,
                    pad_angle=0.7,
                    corner_radius=3,
                    active_outer_radius_offset=8,
                    border_width=1,
                    border_color={
                        "from": "color",
                        "modifiers": [
                            [
                                "darker",
                                0.2,
                            ]
                        ]
                    },
                    arc_link_labels_skip_angle=10,
                    arc_link_labels_text_color="grey",
                    arc_link_labels_thickness=2,
                    arc_link_labels_color={ "from": "color" },
                    arc_labels_skip_angle=10,
                    arc_labels_text_color={
                        "from": "color",
                        "modifiers": [
                            [
                                "darker",
                                2
                            ]
                        ]
                    },
                    defs=[
                        {
                            "id": "dots",
                            "type": "patternDots",
                            "background": "inherit",
                            "color": "rgba(255, 255, 255, 0.3)",
                            "size": 4,
                            "padding": 1,
                            "stagger": True
                        },
                        {
                            "id": "lines",
                            "type": "patternLines",
                            "background": "inherit",
                            "color": "rgba(255, 255, 255, 0.3)",
                            "rotation": -45,
                            "lineWidth": 6,
                            "spacing": 10
                        }
                    ],
                    fill=[
                        { "match": { "id": "ruby" }, "id": "dots" },
                        { "match": { "id": "c" }, "id": "dots" },
                        { "match": { "id": "go" }, "id": "dots" },
                        { "match": { "id": "python" }, "id": "dots" },
                        { "match": { "id": "scala" }, "id": "lines" },
                        { "match": { "id": "lisp" }, "id": "lines" },
                        { "match": { "id": "elixir" }, "id": "lines" },
                        { "match": { "id": "javascript" }, "id": "lines" }
                    ],
                    legends=[
                        {
                            "anchor": "bottom",
                            "direction": "row",
                            "justify": False,
                            "translateX": 0,
                            "translateY": 56,
                            "itemsSpacing": 0,
                            "itemWidth": 100,
                            "itemHeight": 18,
                            "itemTextColor": "#999",
                            "itemDirection": "left-to-right",
                            "itemOpacity": 1,
                            "symbolSize": 18,
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
