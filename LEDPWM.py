#Matias Luca Caccalano - 13676815
#Thiago Dias da Silva - 13751228
#LED PWM
from gpiozero import PWMLED #Biblioteca para utilizar o PWM no LED
from time import sleep #Biblioteca para utilizar o sleep

led = PWMLED(18) #Define o LED que vai ser usado

while True: #Loop infinito
    led.value = 0 #Led desligado
    sleep(0.1)      #Espera 1 segundo
    led.value = 0.5 #duty cyle em 50%
    sleep(0.1)      #Espera 1 segundo
    led.value = 1  #duty cyle em 100%
    sleep(0.1)      #Espera 1 segundo
