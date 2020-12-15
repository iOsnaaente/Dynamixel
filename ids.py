import PyDynamixel_v2.PyDynamixel_v2 as pd 
import SerialReader.Serial as sr
from time import sleep 
import serial

BAUDRATE = 10000000

# definição das portas seriais conectadas ao RS845
while True:    
    print('Detectando portas Seriais....\n')
    comports = sr.serialPorts()
    for i, com in enumerate(comports):
        print(i, com, end='\t')
    
    if comports != []:
        ind = input("\nEscolha a porta Serial onde esta conectado o Conversor RS845: ")
    else: 
        print("Nenhuma porta serial detectada ! \nPressione enter para atualizar")
        input()

    try:
        ind = int(ind)
        comport = serial.Serial(comports[ind], baudrate= BAUDRATE)
        comport.close()
        comport = comports[ind]
        break
    except:
        print("Comport inválida, tente outra!")
        comport = 0

serial = pd.DxlComm(port=comport, baudrate=BAUDRATE)

for i in range(100):
    sleep(0.05)
    jointest = pd.Joint(i)
    try:
        # Attach das juntas
        serial.attach_joint(jointest)
        serial.enable_torques()
        print(jointest.servo_id )
    except: 
        pass 