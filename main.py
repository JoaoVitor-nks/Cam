import streamlit as st
from streamlit_webrtc import webrtc_streamer

st.title("Chamada de Vídeo Teste")

webrtc_streamer(key="sample")


