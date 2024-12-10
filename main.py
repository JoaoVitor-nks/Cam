import av
import cv2
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, WebRtcMode, ClientSettings

# Configuração do WebRTC
WEBRTC_CLIENT_SETTINGS = ClientSettings(
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
    media_stream_constraints={"video": True, "audio": False},
)

# Classe para processar os frames capturados
class VideoProcessor(VideoProcessorBase):
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")  # Converte o frame para um array Numpy
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Converte para RGB
        return av.VideoFrame.from_ndarray(img, format="rgb24")  # Retorna o frame processado

# Título da aplicação
st.title("Câmera do Celular no Streamlit")

st.markdown(
    """
    ### Como usar:
    - Abra esta aplicação no navegador do celular para acessar a câmera.
    - Conceda permissões para usar a câmera.
    - O feed da câmera será exibido abaixo.
    """
)

# Inicializa o streamer do WebRTC
webrtc_streamer(
    key="camera",
    mode=WebRtcMode.SENDRECV,  # Envia e recebe o feed
    client_settings=WEBRTC_CLIENT_SETTINGS,
    video_processor_factory=VideoProcessor,  # Usa a classe para processar os frames
)
