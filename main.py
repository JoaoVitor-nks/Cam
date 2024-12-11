import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode

st.title("Teste de Câmera com WebRTC")

RTC_CONFIGURATION = {
    "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}],
}

MEDIA_STREAM_CONSTRAINTS = {
    "video": True,  # Habilita o vídeo
    "audio": True,  # Desabilita o áudio para simplificar o teste
}

# Configuração mínima para capturar o feed da câmera
webrtc_streamer(
    key="camera-stream",
    mode=WebRtcMode.SENDONLY,  # Apenas envia o feed de vídeo
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints=MEDIA_STREAM_CONSTRAINTS,
)
