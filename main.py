import cv2

cap = cv2.VideoCapture(0)  # Tente com o índice 0

if not cap.isOpened():
    print("Não foi possível acessar a câmera.")
else:
    print("Câmera acessada com sucesso!")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Não foi possível capturar o frame.")
            break

        cv2.imshow("Câmera", frame)

        # Pressione 'q' para sair
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
