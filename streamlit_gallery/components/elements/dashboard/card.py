from streamlit_elements import mui
from .dashboard import Dashboard


class Card(Dashboard.Item):

    DEFAULT_CONTENT = (
        "This impressive paella is a perfect party dish and a fun meal to cook "
        "together with your guests. Add 1 cup of frozen peas along with the mussels, "
        "if you like."
    )

    def __call__(self, content):
        with mui.card(key=self._key, sx={"display": "flex", "flexDirection": "column"}, elevation=3):
            mui.card_header(
                title="Shrimp and Chorizo Paella",
                subheader="September 14, 2016",
                avatar=mui.avatar("R", sx={"bgcolor": "red"}),
                action=mui.icon_button(mui.icon.more_vert),
                class_name=self._draggable_class,
            )
            mui.card_media(
                component="img",
                height=194,
                image="https://mui.com/static/images/cards/paella.jpg",
                alt="Paella dish",
            )

            with mui.card_content(sx={"flex": 1}):
                mui.typography(content)

            with mui.card_actions(disable_spacing=True):
                mui.icon_button(mui.icon.favorite)
                mui.icon_button(mui.icon.share)
