import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, ClientSettings

# Configurações para o cliente WebRTC
WEBRTC_CLIENT_SETTINGS = ClientSettings(
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
    media_stream_constraints={"video": True, "audio": True},
)

st.title("Videochamada")

# Oferecer a opção de ser "host" ou "participante"
role = st.radio("Escolha seu papel:", ["Host", "Participante"], horizontal=True)

if role == "Host":
    st.subheader("Você é o Host")
    webrtc_streamer(
        key="host",
        mode=WebRtcMode.SENDRECV,
        client_settings=WEBRTC_CLIENT_SETTINGS,
    )
else:
    st.subheader("Você é um Participante")
    webrtc_streamer(
        key="guest",
        mode=WebRtcMode.SENDRECV,
        client_settings=WEBRTC_CLIENT_SETTINGS,
    )


