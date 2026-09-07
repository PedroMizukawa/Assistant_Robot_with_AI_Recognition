from pylgbst import get_connection_bleak
from pylgbst.hub import MoveHub
from pylgbst.peripherals import EncodedMotor
import time
import random

hub = None
motor_ext = None

def iniciar_lego():
    global hub, motor_ext
    print("Conectando ao Gato Robótico...")
    conn = get_connection_bleak(hub_mac="(Robot ID)", hub_name="(robot's name)")
    hub = MoveHub(conn)
    motor_ext = EncodedMotor(hub, 3)
    print("Conectado!")
    return hub, motor_ext

def desconectar_lego():
    global hub
    if hub:
        hub.disconnect()
        print("Desconectado.")
        
def levantar_corpo():
    try:
        hub.motor_A.angled(180, -0.7)
        time.sleep(2)
        hub.motor_A.angled(180, 0.7)
        time.sleep(1)
        motor_ext.start_speed(0.8)
        time.sleep(1)
        motor_ext.start_speed(-0.8)
        time.sleep(1)
        motor_ext.stop()
        print("O gato se levantou.")
    except Exception as e:
        print("Erro ao levantar corpo:", e)


def reagir_emocao(emocao, duracao):
    inicio = time.time()
    print(f"Reagindo à emoção '{emocao}' por {duracao:.1f}s...")

    while time.time() - inicio < duracao:
        if emocao == "happy":
            hub.motor_A.angled(180, -0.8) 
            time.sleep(0.1)
            hub.motor_A.angled(180, 0.8)   
            time.sleep(random.uniform(0.4, 1.0))
            
            hub.motor_B.angled(100, -0.6)  
            time.sleep(0.2)
            hub.motor_B.angled(100, 0.6) 
            time.sleep(random.uniform(0.5, 1.2))
            
            motor_ext.start_speed(0.8)
            time.sleep(1)
            motor_ext.start_speed(-0.8)
            time.sleep(1)
            motor_ext.stop()

        elif emocao == "sad":
            hub.motor_A.angled(180, 0.3)
            time.sleep(0.5)
            hub.motor_A.angled(180, -0.3)
            time.sleep(1.0)
            
            motor_ext.start_speed(0.3)
            time.sleep(1)
            motor_ext.start_speed(-0.3)
            time.sleep(1)
            motor_ext.stop()

            hub.motor_B.angled(180, -0.3)  
            time.sleep(1.2)
            hub.motor_B.angled(180, 0.3)
            time.sleep(random.uniform(1.5, 2.0))

        elif emocao == "neutral":
            hub.motor_A.angled(190, -0.4)
            time.sleep(0.4)
            hub.motor_A.angled(190, 0.4)
            time.sleep(0.6)
            
            hub.motor_B.angled(80, -0.4)
            time.sleep(0.4)
            hub.motor_B.angled(80, 0.4)
            time.sleep(random.uniform(1.5, 2.5))
            
            motor_ext.start_speed(0.8)
            time.sleep(1)
            motor_ext.start_speed(-0.8)
            time.sleep(1)
            motor_ext.stop()

    print("Movimento encerrado após a música.")


