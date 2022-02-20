import time
import mysql.connector
COLOURS = {
    "black": "\u001b[30;1m",
    "red": "\u001b[31;1m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33;1m",
    "blue": "\u001b[34;1m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
    "reset": "\u001b[0m",
    "yellow-background": "\u001b[43m",
    "black-background": "\u001b[40m",
    "cyan-background": "\u001b[46;1m",
}


def colortext(text):
    for colour in COLOURS:
        text = text.replace("[[" + colour + "]]", COLOURS[colour])
    return text

def ledspeedhorizontal(b):
    if b == 1:
        print(colortext('[[blue]]speedhorizontalon[[reset]]'))
    else:
        print('speedhorizontaloff')


def ledspeedvertical(b):
    if b == 1:
        print(colortext('[[blue]]speedverticalon[[reset]]'))
    else:
        print('speedverticaloff')

def ldrhorizontal3():
    a = int(input('ldrhorizontal3'))
    return a


def ldrhorizontal4():
    a = int(input('ldrhorizontal4'))
    return a

def ldrvertical3():
    a = int(input('ldrvertical3'))
    return a


def ldrvertical4():
    a = int(input('ldrvertical4'))
    return a

def speedtracker():
    ldrhorizontal3in = ldrhorizontal3()
    time1 = 0

    if ldrhorizontal3in == 1:

        start1 = time.time_ns()
        a = 1

        while a == 1:

            ldrhorizontal4in = ldrhorizontal4()

            if ldrhorizontal4in == 1:

                stop1 = time.time_ns()
                time1 = stop1 - start1
                a = 2
                time.sleep(0.25)

            else:

                time.sleep(0.25)

    speed = 15 / (time1 / 1000000000) * 18 / 5
    print('SPEED: ',speed)

    if speed > 60:
        timerec1 = time.ctime(int(time.time()))
        ledspeedhorizontal(1)

    ldrvertical3in = ldrvertical3()
    time2 = 0

    if ldrvertical3in == 1:

        start2 = time.time_ns()
        a = 1

        while a == 1:

            ldrvertical4in = ldrvertical4()

            if ldrvertical4in == 1:

                stop2 = time.time_ns()
                time2 = stop2 - start2
                a = 2
                time.sleep(0.25)

            else:

                time.sleep(0.25)

    speed = 10 / (time2 / 1000000000) * 18 / 5
    print('SPEED: ',speed)

    if speed > 60:
        timerec2 = time.ctime(int(time.time()))
        ledspeedvertical(1)

def main():
    s = 1

    mdb = mysql.connector.connect(host='localhost', user='root', passwd="1234")
    mc = mdb.cursor()

    mc.execute('CREATE DATABASE IF NOT EXISTS speedtracker;')
    mc.execute('use speedtracker;')
    mc.execute("create table if not exists speedtracker( Date date, time time,road_name varchar(25)")

    while s == 1:

        d = int(input('DO YOU WANT TO RUN THIS PROGRAM:'))

        if d == 1:
            speedtracker()
        else:
            s==2

    print('PROGRAM ENDED\n THANK YOU')

main()
