from uuid import uuid4
from abc import ABC, abstractmethod
from streamlit_elements import dashboard, mui
from contextlib import contextmanager


class Dashboard:

    DRAGGABLE_CLASS = "draggable"

    _layout = []

    @contextmanager
    def __call__(self, **grid_props):
        # Draggable classname query selector.
        grid_props["draggable_handle"] = f".{Dashboard.DRAGGABLE_CLASS}"

        with dashboard(Dashboard._layout, **grid_props):
            yield

    class Item(ABC):

        def __init__(self, x, y, w, h, **item_props):
            self._key = str(uuid4())
            self._draggable_class = Dashboard.DRAGGABLE_CLASS
            self._dark_mode = True
            Dashboard._layout.append(dashboard.item(self._key, x, y, w, h, **item_props))

        def _switch_theme(self):
            self._dark_mode = not self._dark_mode

        @contextmanager
        def title_bar(self, padding="5px 15px 5px 15px", dark_switcher=True):
            with mui.stack(
                class_name=self._draggable_class,
                align_items="center",
                direction="row",
                spacing=1,
                sx={
                    "padding": padding,
                    "borderBottom": 1,
                    "borderColor": "divider",
                },
            ):
                yield

                if dark_switcher:
                    if self._dark_mode:
                        mui.icon_button(mui.icon.dark_mode, on_click=self._switch_theme)
                    else:
                        mui.icon_button(mui.icon.light_mode, sx={"color": "#ffc107"}, on_click=self._switch_theme)

        @abstractmethod
        def __call__(self):
            """Show elements."""
            raise NotImplementedError
