import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode

st.title("Sistema de Ligações com WebRTC")

# Configurações do WebRTC
RTC_CONFIGURATION = {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
MEDIA_STREAM_CONSTRAINTS = {"video": True, "audio": True}

# Escolha o modo: Host ou Participante
role = st.radio("Escolha o papel:", ["Host", "Participante"], horizontal=True)

if role == "Host":
    st.subheader("Você é o Host")
    webrtc_streamer(
        key="host",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration=RTC_CONFIGURATION,
        media_stream_constraints=MEDIA_STREAM_CONSTRAINTS,
    )
elif role == "Participante":
    st.subheader("Você é o Participante")
    webrtc_streamer(
        key="guest",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration=RTC_CONFIGURATION,
        media_stream_constraints=MEDIA_STREAM_CONSTRAINTS,
    )
