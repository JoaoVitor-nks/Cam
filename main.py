import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, ClientSettings

# Configurações para o WebRTC
WEBRTC_CLIENT_SETTINGS = ClientSettings(
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
    media_stream_constraints={"video": True, "audio": False},
)

st.title("Use a câmera do celular como webcam")

st.markdown(
    """
    - Abra este link no navegador do celular para usar sua câmera.
    - Certifique-se de conceder permissões de câmera ao navegador.
    """
)

webrtc_streamer(
    key="camera",
    mode=WebRtcMode.SENDONLY,  # Modo de envio apenas
    client_settings=WEBRTC_CLIENT_SETTINGS,
)
