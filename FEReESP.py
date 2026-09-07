import cv2
from fer import FER
import random
from LegoBoost import levantar_corpo

def detectar_emocao(stream_url):
    detector = FER(mtcnn=True)
    cap = cv2.VideoCapture(stream_url)
    if not cap.isOpened():
        print(" Erro ao conectar ao stream da ESP32-CAM.")
        return None, None

    ret, frame = cap.read()
    cap.release()

    if not ret:
        print("Frame não capturado.")
        return None, None

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = detector.detect_emotions(rgb)

    if not results:
        print("Nenhum rosto detectado, levantando o corpo para tentar de novo...")
        levantar_corpo()
        return None, None 

    emo_dict = results[0]["emotions"]
    emocao = max(emo_dict, key=emo_dict.get)
    confianca = emo_dict[emocao]

    if emocao not in ["happy", "sad", "neutral"]:
        emocao = random.choice(["happy", "sad", "neutral"])
        confianca = random.uniform(0.6, 0.8)

    print(f" Reconhecido: {emocao} ({confianca*100:.1f}%)")

    if confianca < 0.75:
        resposta = input(f" Você está se sentindo {emocao}? (s/n): ").strip().lower()
        if resposta != "s":
            print("O gato vai se levantar e tentar de novo...")
            levantar_corpo()
            return detectar_emocao(stream_url)  # tenta novamente

    return emocao, confianca
