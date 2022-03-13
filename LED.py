import pyfirmata
PORT="\\ \COM7"
BOARD=pyfirmata.Arduino(PORT)
BOARD.digital[13].write(1)

def onLed():
    BOARD.digital[13].write(1)

def offled():
    BOARD.digital[13].write(0)