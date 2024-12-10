import streamlit as st
from streamlit_webrtc import webrtc_streamer, RTCConfiguration
# import av
# import cv2
#
# cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# class VideoProcessor:
#     def recv(self, frame):
#         frm = frame.to_ndarray(format="bgr24")
#
#         faces = cascade.detectMultiScale(cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY), 1.3, 5)
#
#         for x,y,w,h in faces:
#             cv2.rectangle(frm, (x,y), (x+w,y+h), (255, 0, 0), 2)
#
#         return av.VideoFrame.from_ndarray(frm, format="bgr24")

st.title("Chamada de Vídeo")

webrtc_streamer(key="sample")


