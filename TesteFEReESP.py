import cv2
import sys
from fer import FER

ESP32_STREAM_URL = '(ESP URL)'  

detector = FER(mtcnn=True)

cap = cv2.VideoCapture(ESP32_STREAM_URL)
if not cap.isOpened():
    print("Erro ao conectar ao stream da ESP32-CAM.")
    sys.exit()

print("Conectado ao stream da ESP32-CAM.")
print("Pressione 'q' para sair.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Frame não capturado. Verifique a conexão.")
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
    results = detector.detect_emotions(rgb)

    for result in results:
        (x, y, w, h) = result["box"]
        emotions = result["emotions"]
        top_emotion = max(emotions, key=emotions.get)

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, top_emotion, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    cv2.imshow("ESP32-CAM - Emoções em Tempo Real", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
