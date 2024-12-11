import cv2
import streamlit as st

st.title("Projeto Cam - Streamlit com OpenCV")

# Escolha do dispositivo de captura
device_index = st.selectbox("Selecione a câmera:", [0, 1], index=0)

# Botão para iniciar e parar o vídeo
start_button = st.button("Iniciar")
stop_button = st.button("Parar")

frame_placeholder = st.empty()  # Placeholder para exibir os frames

if start_button:
    cap = cv2.VideoCapture(device_index)  # Inicia o dispositivo de captura
    if not cap.isOpened():
        st.error("Não foi possível acessar a câmera.")
    else:
        st.info("Pressione o botão 'Parar' para encerrar o vídeo.")
        
        while True:
            ret, frame = cap.read()
            if not ret:
                st.warning("Não foi possível capturar o frame.")
                break

            # Conversão para RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Exibir o frame no Streamlit
            frame_placeholder.image(frame, channels="RGB")

            # Interrompe o loop se o botão 'Parar' for clicado
            if st.session_state.get('stop', False):
                break

        cap.release()  # Libera a câmera
        cv2.destroyAllWindows()  # Fecha janelas abertas pelo OpenCV

if stop_button:
    st.session_state['stop'] = True
    st.info("O vídeo foi interrompido.")
