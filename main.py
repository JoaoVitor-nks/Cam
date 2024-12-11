import cv2
import streamlit as st

st.title("Projeto Cam - OpenCV e Streamlit")

# Inicialize a câmera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    st.error("Não foi possível acessar a câmera.")
else:
    st.success("Câmera acessada com sucesso!")

# Placeholder para o feed de vídeo
frame_placeholder = st.empty()

# Botão para parar o feed
stop = st.button("Parar Feed")

# Loop para capturar frames
while cap.isOpened() and not stop:
    ret, frame = cap.read()
    if not ret:
        st.warning("Não foi possível capturar o frame. Encerrando...")
        break

    # Converte o frame para RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Exibe o frame no Streamlit
    frame_placeholder.image(frame, channels="RGB")

cap.release()
st.info("Feed encerrado.")
