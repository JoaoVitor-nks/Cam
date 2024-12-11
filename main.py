import cv2
import streamlit as st

# Configurações de captura de vídeo
cap = cv2.VideoCapture(1)  # Use 0 para a câmera padrão, 1 para outra câmera

st.title("Projeto Cam")

# Placeholder para exibir o feed
frame_placeholder = st.empty()

# Botão para parar o vídeo
stop_button = st.button("Stop")

# Loop de captura de vídeo
while not stop_button:
    ret, frame = cap.read()

    if not ret:
        st.write("Não foi possível capturar o vídeo.")
        break

    # Converte o frame para RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Exibe o frame no Streamlit
    frame_placeholder.image(frame, channels="RGB")

# Libera os recursos da câmera
cap.release()
