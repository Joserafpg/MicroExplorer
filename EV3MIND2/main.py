#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.messaging import BluetoothMailboxClient, TextMailbox


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

# Configurar la conexión Bluetooth
client = BluetoothMailboxClient()
command_mailbox = TextMailbox('command', client)

# Intentar conectar al EV3 esclavo
client.connect('ev3dev')  # Asegúrate de cambiar esto por el nombre real del EV3 esclavo

# Bucle principal del programa

try:
    while True:
        pressed = ev3.buttons.pressed()
        
        if Button.UP in pressed:
            command_mailbox.send('forward')
        elif Button.DOWN in pressed:
            command_mailbox.send('backward')
        elif Button.RIGHT in pressed:
            command_mailbox.send('turn_right')
        elif Button.LEFT in pressed:
            command_mailbox.send('turn_left')
        elif not pressed:
            command_mailbox.send('stop')

        wait(100)  # Tiempo de espera para evitar sobrecargar los mensajes
finally:
    client.disconnect()