import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode

st.title("Teste de Chamada de Vídeo")

# Configurações WebRTC
RTC_CONFIGURATION = {
    "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}],  # Servidor STUN público
}
MEDIA_STREAM_CONSTRAINTS = {
    "video": True,  # Captura o vídeo
    "audio": True,  # Captura o áudio
}

# Inicia o WebRTC
webrtc_streamer(
    key="camera-test",
    mode=WebRtcMode.SENDRECV,  # Envia e recebe o feed de vídeo/áudio
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints=MEDIA_STREAM_CONSTRAINTS,
)
