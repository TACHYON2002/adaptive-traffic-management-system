import serial
import csv
import sys
import time

a = 0
b = 0
c = 0
d = 0
if __name__ == '__main__':

    ser = serial.Serial('COM4', 9600, timeout=1)
    ser.reset_input_buffer()

    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            x=line.split(",")
            a=int(x[0]) 
            b=int(x[1])    
            c=int(x[2])
            d=int(x[3])
            
            break   

def calla():
    return(a)
    

def callb():
    return(b)

def callc():
    return(c)

def calld():
    return(d)