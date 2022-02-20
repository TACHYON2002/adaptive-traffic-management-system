def ldrhorizontal4():

    a = 1
    return a

def ldrvertical4():

    a = 1
    return a

def ledhorizontal(b):

    if b == 1:

        print('ledhorizontalon')

def ledvertical(b):

    if b == 1:

        print('ledverticalon')

def rulehorizontal():

    ldrhorizontal4in = ldrhorizontal4()

    if ldrhorizontal4in == 1:

        ledhorizontal(1)


def rulevertical():

    ldrvertical4in = ldrvertical4()

    if ldrvertical4in == 1:

        ledvertical(1)

rulehorizontal()
rulevertical()

