#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
from pybricks.messaging import BluetoothMailboxServer, TextMailbox

# Crear el objeto EV3
ev3 = EV3Brick()

# Crear los objetos motor
motor_right = Motor(Port.A)
motor_left = Motor(Port.D)

# Configurar la conexión Bluetooth
server = BluetoothMailboxServer()
command_mailbox = TextMailbox('command', server)

# Esperar a que se establezca la conexión
server.wait_for_connection()

try:
    while True:
        command_mailbox.wait()
        command = command_mailbox.read()

        if command == 'forward':
            motor_right.run(-1000)
            motor_left.run(-1000)
        elif command == 'backward':
            motor_right.run(1000)
            motor_left.run(1000)
        elif command == 'turn_right':
            motor_right.run(-500)
            motor_left.run(500)
        elif command == 'turn_left':
            motor_right.run(500)
            motor_left.run(-500)
        elif command == 'stop':
            motor_right.stop()
            motor_left.stop()
finally:
    motor_right.stop()
    motor_left.stop()
    server.disconnect()