# coding: utf-8
import time
import os
import requests
from grovepi import *
from LSM6DS3 import *

# Connect the Grove Buzzer to digital port D8
# SIG,NC,VCC,GND
buzzer = 2
ultrasonic_ranger1 = 4
ultrasonic_ranger2 = 3 
buttonActivationCanne = 7
buttonCalibrage = 8
accelerometre = LSM6DS3()

pinMode(buttonActivationCanne,"INPUT")
pinMode(buttonCalibrage,"INPUT")
pinMode(buzzer,"OUTPUT")

compteurMarche = 0 
booleanMarche = False #Booléen pour savoir si l'utilisateur passe sur une marche
booleanActiver = False #Booléen pour activer ou désactiver la détection de la canne
compteurActiver = 0
booleanEnvoieDonnee = False

def calibrageCanne():
     while digitalRead(buttonCalibrage)==1:
              axeY = accelerometre.readRawAccelY()
              print (axeY)
              if(axeY < -10000 and axeY > -13000):
                   activationBuzzer(0.2)
        

def activationBuzzer(tempsBuzzerInactif):
     digitalWrite(buzzer,1)
     time.sleep(0.1)
     digitalWrite(buzzer,0)
     time.sleep(tempsBuzzerInactif)

def frequenceBuzzerMur(valeurCapteur):
    if (valeurCapteur<5):
         activationBuzzer(0.1)
         print ("Capteur 1 activé")
     
    elif (valeurCapteur<15):
         activationBuzzer(0.2)

    elif (valeurCapteur<25):
         activationBuzzer(0.3)

    elif (valeurCapteur<35):
         activationBuzzer(0.4)

    elif (valeurCapteur<45):
         activationBuzzer(0.5)

    elif (valeurCapteur<50):
         activationBuzzer(0.6)

    else :      
	digitalWrite(buzzer,0)
	print ("Buzzer désactivé")


def frequenceBuzzerMarche(valeurCapteur,booleanMarche):
    if (valeurCapteur>50):
         digitalWrite(buzzer,1)
         time.sleep(0.1)
         digitalWrite(buzzer,0)
         time.sleep(0.05)
         digitalWrite(buzzer,1)
         time.sleep(0.1)
         digitalWrite(buzzer,0)
         time.sleep(0.7)
         print ("Capteur 1 activé")
         return False

    else :
             
	digitalWrite(buzzer,0)
	compteur = 0
	print ("Buzzer désactivé")
	if(booleanMarche == False):
             return True


while True:
    
    calibrageCanne() #Fonction pour calibrer la canne
    
    if (digitalRead(buttonActivationCanne)==1):
         if (compteurActiver == 0):
              compteurActiver = 1
         else:
              compteurActiver = 0

    booleanEnvoieDonnee = True
         
    # Si le boutton On/Off est activé alors les capteurs ultrasons sont lancés
    while compteurActiver==1:
	print ("Bouton appuyé")
	
            # Buzz si le capteur 1 est activé
	valeurCapteur1 = ultrasonicRead(ultrasonic_ranger1)
	valeurCapteur2 = ultrasonicRead(ultrasonic_ranger2)
	
	print ("Distance Capteur 1")
	print (valeurCapteur1)
	print ("Distance Capteur 2")
	print (valeurCapteur2)

        booleanMarche = frequenceBuzzerMarche(valeurCapteur1,booleanMarche)
        if(booleanMarche):
             compteurMarche = compteurMarche + 1
                
        frequenceBuzzerMur(valeurCapteur2)

        while (digitalRead(buttonActivationCanne)==1):
             print ("Fonctionnalité capteur arrêtée")
             compteurActiver = 0    

    if(booleanMarche): 
         compteurMarche = compteurMarche + 1
         booleanMarche = False

    if(booleanEnvoieDonnee and compteurMarche > 0):
         
         os.system('curl "https://docs.google.com/forms/d/e/1FAIpQLSfrfjh94zl79f9Jrjc3W_lJ_8uXd-jMzkOj2OGMaU6oyyFqDw/formResponse?ifq&entry.2139415933=' + str(compteurMarche) + '&submit=Submit"')
         booleanEnvoieDonnee = False
         compteurMarche = 0
  
    print ("Bouton relaché")
    print("CompteurMarche :")
    print(compteurMarche)



