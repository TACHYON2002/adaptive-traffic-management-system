import ard
import time
import serial

ser = serial.Serial('COM4', 9600, timeout=1)

if ser.isOpen():
    ser.close()

ser.open()
ser.isOpen()

def ledgreenhorizontal(b):
    if b == 1:
        ser.write(b'a')
    else:
        ser.write(b'A')


def ledyellowhorizontal(b):
    if b == 1:
        ser.write(b'b')

    else:
        ser.write(b'B')


def ledredhorizontal(b):
    if b == 1:
        ser.write(b'c')
    else:
        ser.write(b'C')


def ledgreenvertical(b):
    if b == 1:
        ser.write(b'd')
    else:
        ser.write(b'D')


def ledyellowvertical(b):
    if b == 1:
        ser.write(b'e')
    else:
        ser.write(b'E')


def ledredvertical(b):
    if b == 1:
        ser.write(b'f')
    else:
        ser.write(b'F')


def ldrhorizontal1():
    a = ard.callc()
    return a


def ldrhorizontal2():
    a = ard.calld()
    return a


def ldrvertical1():
    a = ard.calla()
    return a


def ldrvertical2():
    a = ard.callb()
    return a


def main():
    b = 1

    while b == 1:

        a = input('TO START ENTER 1    TO END ENTER 0\n')

        if a == '1':

            while True:
                traffic()

        elif a == '0':

            print('PROGRAM ENDED')
            b = 2

        else:

            print('TRY AGAIN')


def traffic():
    ledredvertical(1)
    ledredhorizontal(1)

    ldrhorizontal1in = ldrhorizontal1()
    ldrhorizontal2in = ldrhorizontal2()
    ldrvertical1in = ldrvertical1()
    ldrvertical2in = ldrvertical2()

    if ldrhorizontal1in + ldrhorizontal2in == ldrvertical1in + ldrvertical2in:

        ledredvertical(0)
        ledyellowvertical(1)
        time.sleep(2)
        ledyellowvertical(0)
        ledgreenvertical(1)
        time.sleep(7)
        ledgreenvertical(0)
        ledyellowvertical(1)
        time.sleep(2)
        ledyellowvertical(0)
        ledredvertical(1)
        ledredhorizontal(0)
        ledyellowhorizontal(1)
        time.sleep(2)
        ledyellowhorizontal(0)
        ledgreenhorizontal(1)
        time.sleep(7)
        ledgreenhorizontal(0)
        ledyellowhorizontal(1)
        time.sleep(2)
        ledyellowhorizontal(0)
        ledredvertical(0)


    elif ldrhorizontal1in + ldrhorizontal2in == 0 and ldrvertical1in + ldrvertical2in != 0:

        ledredvertical(0)
        ledyellowvertical(1)
        time.sleep(2)
        ledyellowvertical(0)
        ledgreenvertical(1)
        time.sleep(7)
        ledgreenvertical(0)
        ledyellowvertical(1)
        time.sleep(2)
        ledyellowvertical(0)
        ledredhorizontal(0)

    elif ldrhorizontal1in + ldrhorizontal2in != 0 and ldrvertical1in + ldrvertical2in == 0:

        ledredhorizontal(0)
        ledyellowhorizontal(1)
        time.sleep(2)
        ledyellowhorizontal(0)
        ledgreenhorizontal(1)
        time.sleep(7)
        ledgreenhorizontal(0)
        ledyellowhorizontal(1)
        time.sleep(2)
        ledyellowhorizontal(0)
        ledredvertical(0)

    elif ldrhorizontal1in + ldrhorizontal2in == 1 and ldrvertical1in + ldrvertical2in == 2:

        ledredvertical(0)
        ledyellowvertical(1)
        time.sleep(2)
        ledyellowvertical(0)
        ledgreenvertical(1)
        time.sleep(7)
        ledgreenvertical(0)
        ledyellowvertical(1)
        time.sleep(2)
        ledyellowvertical(0)
        ledredvertical(1)
        ledredhorizontal(0)
        ledyellowhorizontal(1)
        time.sleep(2)
        ledyellowhorizontal(0)
        ledgreenhorizontal(1)
        time.sleep(4)
        ledgreenhorizontal(0)
        ledyellowhorizontal(1)
        time.sleep(2)
        ledyellowhorizontal(0)
        ledredvertical(0)


    elif ldrhorizontal1in + ldrhorizontal2in == 2 and ldrvertical1in + ldrvertical2in == 1:

        ledredvertical(0)
        ledyellowvertical(1)
        time.sleep(2)
        ledyellowvertical(0)
        ledgreenvertical(1)
        time.sleep(4)
        ledgreenvertical(0)
        ledyellowvertical(1)
        time.sleep(2)
        ledyellowvertical(0)
        ledredvertical(1)
        ledredhorizontal(0)
        ledyellowhorizontal(1)
        time.sleep(2)
        ledyellowhorizontal(0)
        ledgreenhorizontal(1)
        time.sleep(7)
        ledgreenhorizontal(0)
        ledyellowhorizontal(1)
        time.sleep(2)
        ledyellowhorizontal(0)
        ledredvertical(0)


main()
