import time
from grovepi import *

# Connect the Grove Buzzer to digital port D8
# SIG,NC,VCC,GND
buzzer = 8
ultrasonic_ranger1 = 4
ultrasonic_ranger2 = 5 ### A VERIFIER
ultrasonic_ranger3 = 6 ### A VERIFIER
button = 3

pinMode(button,"INPUT")
pinMode(buzzer,"OUTPUT")

while True:
    
    #######
    ## CODAGE CALIBRAGE ACCELEROMETRE A IMPLEMENTER ##
    #######
    
    # Si le boutton On/Off est activé alors les capteurs ultrasons sont lancés
    while digitalRead(button)==1:
        try:
            # Buzz si le capteur 1 est activé
            if (ultrasonicRead(ultrasonic_ranger1)<2):
                digitalWrite(buzzer,1)
                print ultrasonicRead(ultrasonic_ranger1)
                print ('start')
        

            # Stop le buzz du capteur 1
            if(ultrasonicRead(ultrasonic_ranger1)>=2):
                digitalWrite(buzzer,0)
                print ultrasonicRead(ultrasonic_ranger1)
                print ('stop')



            #########----------------###########



            # Buzz si le capteur 2 est activé
            if (ultrasonicRead(ultrasonic_ranger2)<2):
                digitalWrite(buzzer,1)
                print ultrasonicRead(ultrasonic_ranger2)
                print ('start')
        

            # Stop le buzz du capteur 2
            if(ultrasonicRead(ultrasonic_ranger2)>=2):
                digitalWrite(buzzer,0)
                print ultrasonicRead(ultrasonic_ranger2)
                print ('stop')



            #########----------------###########



            # Buzz si le capteur 3 est activé
            if (ultrasonicRead(ultrasonic_ranger3)<2):
                digitalWrite(buzzer,1)
                print ultrasonicRead(ultrasonic_ranger3)
                print ('start')
        

            # Stop le buzz du capteur 3
            if(ultrasonicRead(ultrasonic_ranger3)>=2):
                digitalWrite(buzzer,0)
                print ultrasonicRead(ultrasonic_ranger3)
                print ('stop')



        except KeyboardInterrupt:
            digitalWrite(buzzer,0)
            break
        except IOError:
            print ("Error")
            
            
### def CanneEstTombe() ### fonction permettant d'émettre un bip d'une certaine fréquence pour indiquer un changement brutal
### dans les valeurs de l'accéléromètre qui indiquerais une chute de la canne

### def CalibrageCanne() ### fonction permettant de calibrer la canne avec l'accéléromètre



 
