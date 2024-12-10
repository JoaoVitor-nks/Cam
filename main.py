import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, ClientSettings

# Configurações para o cliente WebRTC
WEBRTC_CLIENT_SETTINGS = ClientSettings(
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
    media_stream_constraints={"video": True, "audio": False},  # Apenas vídeo
)

# Inicializa o Streamlit
st.title("Teste de Câmera com Streamlit-WebRTC")
st.markdown(
    """
    ### Como usar:
    - Clique em **Start** para iniciar a câmera.
    - Certifique-se de conceder permissões ao navegador para acessar a câmera.
    """
)

# Configura o WebRTC para capturar o vídeo
webrtc_streamer(
    key="camera-test",
    mode=WebRtcMode.SENDONLY,  # Apenas envia o vídeo
    client_settings=WEBRTC_CLIENT_SETTINGS,
)
