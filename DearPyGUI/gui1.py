from dearpygui.core import *
from dearpygui.simple import *
from math import cos

import SerialReader.Serial as sr

defaltSerialPort = "Atualizar Portas"
port = []

# Functions of call_backs 
def serial_att(sender, data): 
    global defaltSerialPort
    global port
    port = sr.serialPorts()
    if port == []:
        defaltSerialPort = "Atualizar Portas"
    else:
        defaltSerialPort = port[0]

def serial_setValues(sender, data):
    global port
    try:
        port = get_value("##comboComports") 
        comport = serial.Serial( port , baudrate= get_value("##comboBaudrate") , timeout=get_value("##inputIntTimeout") )
        comport.close()
        comport = port
    except:
        log_error("Serial Inválida, selecione outra!!")
        comport = 0


X_WINDOW = 1400
Y_WINDOW = 800

# Window configurations 
set_main_window_size(X_WINDOW, Y_WINDOW)
set_global_font_scale(1.0)
set_style_window_padding(30,30)


with window("main_window"):
    with tab_bar("headerTable"):
        with tab("Serial"):
            with child("Configure a porta serial", width=400, height=400):
                # Usar funções para pegar as comports 
                serial_att(0,0)
                add_text("Comports")
                add_combo("##comboComports", items=port, default_value=defaltSerialPort, width=310 )

                add_text("Baudrate")
                add_combo("##comboBaudrate", items=[9600, 57600, 1000000], default_value="null", width=310 )
                
                add_text("Timeout")
                add_input_float("##inputIntTimeout", width=310 )
                
                add_button("inputAtt##Serial" ,label = "Atualizar Portas", callback = serial_att, width= 150 )
                add_same_line()
                add_button("inputSet##Serial" ,label = "Set values", callback = serial_setValues, width= 152)
            

        with tab("Teste de rigidez"):
            pass
            #add_slider_float("Mot1Y", vertical=True, min_value=-180, max_value=180, default_value=0, callback=update_drawing)
            #add_slider_float("Mot1X", vertical=True, min_value=-180, max_value=180, default_value=0, callback=update_drawing)
            #draw_circle("CircleMotor1##Rigidez", [300,300], 50, [255,200,200,250])
        

        with tab("Amplitude"):
            pass


start_dearpygui(primary_window="main_window")