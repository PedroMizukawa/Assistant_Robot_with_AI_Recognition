from FEReESP import detectar_emocao
from LegoBoost import iniciar_lego, reagir_emocao, desconectar_lego
from SpotifyComandos import tocar_playlist_por_emocao
import threading
import time

STREAM_URL = '(ESP URL)'

if __name__ == "__main__":
    print("Iniciando monitoramento de emoções...")
    iniciar_lego()

    try:
        while True:
            emocao, confianca = detectar_emocao(STREAM_URL)

            if emocao:
                print(f"Emoção confirmada: {emocao} ({confianca*100:.1f}%)")

                duracao = tocar_playlist_por_emocao(emocao)
                if not duracao:
                    duracao = 120
                    
                thread_reacao = threading.Thread(target=reagir_emocao, args=(emocao, duracao))
                thread_reacao.start()

                print(f"Tocando música por {duracao:.1f}s...")
                time.sleep(duracao + 3)

                if thread_reacao.is_alive():
                    print("Encerrando movimento após fim da música...")
                    thread_reacao.join(timeout=2)

                print("Pronto para nova detecção em 5 segundos...\n")
                time.sleep(5)

            else:
                print("Nenhuma emoção detectada. Tentando novamente em 5 segundos...\n")
                time.sleep(5)

    except KeyboardInterrupt:
        print("\n Programa interrompido manualmente.")

    finally:
        desconectar_lego()
