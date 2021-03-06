# coding: utf-8
import time
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

compteurMarche = 0 #Appel à la fonction qui renvoie le nombre de marches rencontrées ce jour-ci grâce à une requete de à dweet
booleanMarche = False #Booléen pour savoir si l'utilisateur passe sur une marche
booleanActiver = False #Booléen pour activer ou désactiver la détection de la canne
compteurActiver = 0

def calibrageCanne():
     while digitalRead(buttonCalibrage)==1:
              axeX = accelerometre.readRawAccelX()
              axeY = accelerometre.readRawAccelY()
              axeZ = accelerometre.readRawAccelZ()
              print (axeX)
              print (axeY)
              print (axeZ)
              time.sleep(0.08)
        

def activationBuzzer(tempsBuzzerInactif):
     digitalWrite(buzzer,1)
     time.sleep(0.1)
     digitalWrite(buzzer,0)
     time.sleep(tempsBuzzerInactif)

def frequenceBuzzer(valeurCapteur,booleanMarche):
    if (valeurCapteur<5):
         activationBuzzer(0.1)
         print ("Capteur 1 activé")
         return False
     

    elif (valeurCapteur<15):
         activationBuzzer(0.2)
         return False

    elif (valeurCapteur<25):
         activationBuzzer(0.3)
         return False

    elif (valeurCapteur<35):
         activationBuzzer(0.4)
         return False

    elif (valeurCapteur<45):
         activationBuzzer(0.5)
         return False

    elif (valeurCapteur<50):
         activationBuzzer(0.6)
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
         
    # Si le boutton On/Off est activé alors les capteurs ultrasons sont lancés
    while compteurActiver==1:
	print ("Bouton appuyé")
     #   try:
            # Buzz si le capteur 1 est activé
	valeurCapteur1 = ultrasonicRead(ultrasonic_ranger1)
	valeurCapteur2 = ultrasonicRead(ultrasonic_ranger2)
	
	print ("Distance Capteur 1")
	print (valeurCapteur1)

	print ("Distance Capteur 2")
	print (valeurCapteur2)

        booleanMarche = frequenceBuzzer(valeurCapteur1,booleanMarche)
        if(booleanMarche):
             compteurMarche = compteurMarche + 1
             
        frequenceBuzzer(valeurCapteur2,booleanMarche)

        while (digitalRead(buttonActivationCanne)==1):
             print ("Fonctionnalité capteur arrêtée")
             compteurActiver = 0     # REGLER PROBLEME COMPTEUR MARCHE

    if(booleanMarche == True): 
         compteurMarche = compteurMarche + 1
    print ("Bouton relaché")
    print("CompteurMarche :")
    print(compteurMarche)    
