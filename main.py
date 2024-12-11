import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, ClientSettings

st.title("Ligação por Vídeo no Streamlit")

# Configurações do WebRTC
RTC_CONFIGURATION = {
    "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]  # Servidor STUN
}

# Escolha o papel do usuário: Host ou Participante
role = st.radio("Escolha o papel:", ["Host", "Participante"], horizontal=True)

if role == "Host":
    st.subheader("Você é o Host. Espere pelo Participante.")
    webrtc_streamer(
        key="host",
        mode=WebRtcMode.SENDRECV,  # Envia e recebe áudio/vídeo
        rtc_configuration=RTC_CONFIGURATION,
        media_stream_constraints={"video": True, "audio": True},
    )
elif role == "Participante":
    st.subheader("Você é o Participante. Conecte-se ao Host.")
    webrtc_streamer(
        key="guest",
        mode=WebRtcMode.SENDRECV,  # Envia e recebe áudio/vídeo
        rtc_configuration=RTC_CONFIGURATION,
        media_stream_constraints={"video": True, "audio": True},
    )

code = '''import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, ClientSettings

st.title("Ligação por Vídeo no Streamlit")

# Configurações do WebRTC
RTC_CONFIGURATION = {
    "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]  # Servidor STUN
}

# Escolha o papel do usuário: Host ou Participante
role = st.radio("Escolha o papel:", ["Host", "Participante"], horizontal=True)

if role == "Host":
    st.subheader("Você é o Host. Espere pelo Participante.")
    webrtc_streamer(
        key="host",
        mode=WebRtcMode.SENDRECV,  # Envia e recebe áudio/vídeo
        rtc_configuration=RTC_CONFIGURATION,
        media_stream_constraints={"video": True, "audio": True},
    )
elif role == "Participante":
    st.subheader("Você é o Participante. Conecte-se ao Host.")
    webrtc_streamer(
        key="guest",
        mode=WebRtcMode.SENDRECV,  # Envia e recebe áudio/vídeo
        rtc_configuration=RTC_CONFIGURATION,
        media_stream_constraints={"video": True, "audio": True},'''

st.code(code, language="Python")
