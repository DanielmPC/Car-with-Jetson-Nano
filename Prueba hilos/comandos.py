import RPi.GPIO as GPIO

## Declaración de pines
pin_rueda1_1 = 21
pin_rueda1_2 = 22

# Declaración de pines segunda rueda
pin_rueda2_1 = 31
pin_rueda2_2 = 32


def setup():

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(pin_rueda1_1,GPIO.OUT)
    GPIO.setup(pin_rueda1_2,GPIO.OUT)

    GPIO.setup(pin_rueda2_1,GPIO.OUT)
    GPIO.setup(pin_rueda2_2,GPIO.OUT)

   
# Recto
def recto():
    ## Siempre deben de ir 1-0, sino puede haber un corto
    GPIO.output(pin_rueda1_1, GPIO.HIGH)
    GPIO.output(pin_rueda1_2, GPIO.LOW)

    GPIO.output(pin_rueda2_1, GPIO.HIGH)
    GPIO.output(pin_rueda2_2, GPIO.LOW)
    

# Reversa
def reversa():

    GPIO.output(pin_rueda1_1, GPIO.LOW)
    GPIO.output(pin_rueda1_2, GPIO.HIGH)

    GPIO.output(pin_rueda2_1, GPIO.LOW)
    GPIO.output(pin_rueda2_2, GPIO.HIGH)
    

# Derecha 
def derecha():
    GPIO.output(pin_rueda1_1, GPIO.HIGH)
    GPIO.output(pin_rueda1_2, GPIO.LOW)

    GPIO.output(pin_rueda2_1, GPIO.LOW)
    GPIO.output(pin_rueda2_2, GPIO.LOW)

# Izquierda
def izquierda():
    
    GPIO.output(pin_rueda1_1, GPIO.LOW)
    GPIO.output(pin_rueda1_2, GPIO.LOW)

    GPIO.output(pin_rueda2_1, GPIO.HIGH)
    GPIO.output(pin_rueda2_2, GPIO.LOW)

# paro
def paro():
    GPIO.output(pin_rueda1_1, GPIO.LOW)
    GPIO.output(pin_rueda1_2, GPIO.LOW)

    GPIO.output(pin_rueda2_1, GPIO.LOW)
    GPIO.output(pin_rueda2_2, GPIO.LOW)



if __name__=="__main__":
    setup()

'''
while True:
    GPIO.output(pin_recto, GPIO.LOW)
    GPIO.output(pin_reversa, GPIO.LOW)
    time.sleep(1)
    GPIO.output(pin_recto, GPIO.HIGH)
    GPIO.output(pin_reversa, GPIO.HIGH)
    time.sleep(1)'''
    
