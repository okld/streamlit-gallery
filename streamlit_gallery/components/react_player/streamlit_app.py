import streamlit as st

from streamlit_player import st_player, _SUPPORTED_EVENTS
from streamlit_gallery.utils.readme import readme


def main():
    with readme("streamlit-player", st_player, __file__):
        c1, c2, c3 = st.columns([3, 3, 2])

        with c3:
            st.subheader("Parameters")

            options = {
                "events": st.multiselect("Events to listen", _SUPPORTED_EVENTS, ["onProgress"]),
                "progress_interval": 1000,
                "volume": st.slider("Volume", 0.0, 1.0, 1.0, .01),
                "playing": st.checkbox("Playing", False),
                "loop": st.checkbox("Loop", False),
                "controls": st.checkbox("Controls", True),
                "muted": st.checkbox("Muted", False),
            }

            with st.expander("SUPPORTED PLAYERS", expanded=True):
                st.write("""
                - Dailymotion
                - Facebook
                - Mixcloud
                - SoundCloud
                - Streamable
                - Twitch
                - Vimeo
                - Wistia
                - YouTube
                <br/><br/>
                """, unsafe_allow_html=True)


        with c1:
            url = st.text_input("First URL", "https://youtu.be/c9k8K1eII4g")
            event = st_player(url, **options, key="youtube_player")

            st.write(event)

        with c2:
            url = st.text_input("Second URL", "https://soundcloud.com/imaginedragons/demons")
            event = st_player(url, **options, key="soundcloud_player")

            st.write(event)


if __name__ == "__main__":
    main()
