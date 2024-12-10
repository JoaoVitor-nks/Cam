import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, ClientSettings

# Configurações para WebRTC
WEBRTC_CLIENT_SETTINGS = ClientSettings(
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
    media_stream_constraints={"video": True, "audio": False},
)

st.title("Teste de Câmera")

st.markdown(
    """
    - Certifique-se de conceder permissões para usar a câmera.
    - Caso não veja o vídeo, tente em outro navegador ou verifique os logs.
    """
)

# Captura e exibe o feed de vídeo
webrtc_streamer(
    key="camera-test",
    mode=WebRtcMode.SENDRECV,  # Envia e recebe o feed
    client_settings=WEBRTC_CLIENT_SETTINGS,
)
