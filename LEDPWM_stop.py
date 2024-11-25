#Matias Luca Caccalano - 13676815
#Thiago Dias da Silva - 13751228
#LED PWM_stop
from gpiozero import PWMLED #Biblioteca para utilizar o PWM no LED
from time import sleep #Biblioteca para utilizar o sleep

led = PWMLED(18) #Define o LED que vai ser usado

while True: #Loop infinito
    led.value = 0 #Led desligado
    sleep(0.5)      #Espera 0,5 segundo
    
