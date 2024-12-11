import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Não foi possível acessar a câmera.")
else:
    print("Câmera acessada com sucesso!")

cap.release()
