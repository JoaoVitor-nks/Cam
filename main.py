import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode

st.title("Teste de Câmera com WebRTC")

# Configuração do WebRTC
RTC_CONFIGURATION = {
    "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}],  # Servidor STUN
}

MEDIA_STREAM_CONSTRAINTS = {
    "video": True,  # Habilita o feed de vídeo
    "audio": False,  # Desabilita o áudio para simplificar
}

# Inicialização do WebRTC
webrtc_streamer(
    key="camera-stream",
    mode=WebRtcMode.SENDONLY,  # Apenas envia o feed de vídeo
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints=MEDIA_STREAM_CONSTRAINTS,
)
