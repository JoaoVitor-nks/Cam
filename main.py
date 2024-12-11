import cv2
import streamlit as st
import numpy as np
import tempfile


cap = cv2.VideoCapture(0)

st.title('Projeto Cam')

frame_placeholder = st.empty()

stop_button = st.button('Stop')


while cap.isOpened() and not stop_button:

    ret, frame = cap.read()

    if not ret:
        st.write("O video acabou")
        break

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    frame_placeholder.image(frame, channels='RGB')

    if cv2.waitKey(0) & 0xFF == ord('q') or stop_button:
        break


cap.release()

