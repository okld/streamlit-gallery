import streamlit as st

from streamlit_player import st_player, _SUPPORTED_EVENTS
from streamlit_pages.utils import readme


def main():
    with readme("streamlit-player", st_player, __file__):
        with st.sidebar:
            st.title("⚙️ Parameters")

            options = {
                "events": st.multiselect("Events to listen", _SUPPORTED_EVENTS, ["onProgress"]),
                "progress_interval": st.slider("Progress refresh interval (ms)", 200, 2000, 500, 1),
                "volume": st.slider("Volume", 0.0, 1.0, 1.0, .01),
                "playing": st.checkbox("Playing", False),
                "loop": st.checkbox("Loop", False),
                "controls": st.checkbox("Controls", True),
                "muted": st.checkbox("Muted", False),
            }

            st.write("""
            ---
            ## ⏯️ Supported players
            * Dailymotion
            * Facebook
            * Local files
            * Mixcloud
            * SoundCloud
            * Streamable
            * Twitch
            * Vimeo
            * Wistia
            * YouTube
            """)

        c1, c2 = st.beta_columns(2)

        with c1:
            url = st.text_input("First URL", "https://youtu.be/CmSKVW1v0xM")
            event = st_player(url, **options, key=1)

            st.write(event)

        with c2:
            url = st.text_input("Second URL", "https://soundcloud.com/imaginedragons/demons")
            event = st_player(url, **options, key=2)

            st.write(event)


if __name__ == "__main__":
    main()
