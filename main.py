
#colores  utilizar
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
RESET = '\033[39m'


#librerias 
import time
import random
import os

puntaje = random.randint (0,11)
inicio_trivia = True
intentos = 0

puntaje_total =[]

def numero_carga():
  for numero_carga in range(5,0,-1):
   print(numero_carga)
   time.sleep(1)
    
#inicio
time.sleep(1)
print(BLUE+"Bienvenido a mi Trivia sobre Instrumentos Musicales"+RESET)
time.sleep(1)
print(GREEN+"estas preparado para el reto?")
time.sleep(3)
print("pondremos a prueba tus conocimientos!"+RESET)
time.sleep(2)

numero_carga()
  
nombre = input(MAGENTA+"escribe tu nombre :"+RESET)
time.sleep(1)

lista = ["hola!",nombre]
for i in lista :
  print(i)
  time.sleep (1)

print("tienes", puntaje, "puntos")
time.sleep(2)

print(GREEN+"\nResponde las preguntas escribiendo la letra de la alternativa que elijas y presiona 'Enter' para enviar la respuesta:\n"+RESET)
time.sleep(1)

while inicio_trivia == True :
  intentos += 1
  puntaje = random.randint(0,11)
  
  print("intento numero:",intentos,)
  input("presione Enter para continuar:")

  numero_carga()
#pregunta 1
  
  print("\nPregunta N°1")
  time.sleep(1)
  print(BLUE+"\n¿que instrumento tiene solo 4 cuerdas?:\n"+RESET)
  time.sleep(1)
  
  instrumento =["a)guitarra","b)piano","c)bajo","d)flauta"]
  for number in range(0,4):
   print (instrumento[number]) 
   time.sleep(1)

  respuesta_1 = input("\nEscribe tu respuesta:")

  while respuesta_1 not in ("a","b","c","d"):
    respuesta_1 = input("debes responder a , b, c o d. Ingresa nuevamente tu respuesta: ")

  if respuesta_1 == "c":
    puntaje += 10
    print(YELLOW+"\nTu respuesta es Correcta!"+RESET)
    time.sleep(1)
  else:
    puntaje -= 10
    print(RED+"que pena,respuesta incorrecta!"+RESET)
    
  print("llevas",puntaje,"puntos")
  time.sleep(1)

#pregunta 2
  
  print("\nPregunta N°2")
  time.sleep(1)
  
  print(BLUE+"\n¿cual de las 4 alternativas no es un instrumento de viento?\n"+RESET)
  time.sleep(1)
  
  noinstrumento =["a)flauta","b)quena","c)trompeta","d)piano"]
  for number1 in range(0,4):
   print (noinstrumento[number1]) 
   time.sleep(1)

  respuesta_2 = input("\nescribe tu respuesta:")
  
  while respuesta_2 not in("a","b","c","d","x"):
    respuesta_2 = input("debes responder a , b, c o d. Ingresa nuevamente tu respuesta:")
  
  if respuesta_2 == "a":
    print(RED+"incorrecto!", nombre, "la flauta tiene forma tubular y es un instrumento de viento ")
    puntaje -=  random.randint (0,11)
  elif respuesta_2 == "b":
    print("incorrecto!", nombre,"la quena es un instrumento de viento ")
    puntaje -=  random.randint (0,11)
  elif respuesta_2 == "c":
    print("incorrecto!", nombre, "instrumento más pequeño y agudo de la familia de los metales,tambien es de viento"+RESET)
    puntaje -=  random.randint (0,11)
  #Pregunta secreta
  elif respuesta_2 == "x":
   puntaje += 100
   print("esta es una respuesta secreta")
   print("genial!has obtenido 100 puntos!")
  else:
    puntaje +=  random.randint (0,11)
    print(YELLOW+"\nMuy Bien" , nombre,"!"+RESET)
    time.sleep(1)

  print("llevas",puntaje,"puntos")
  time.sleep(1)

#pregunta 3
  print("\nPregunta N°3")
  time.sleep(1)
  print("\n¿Que instrumento es el mas popular?\n")
  time.sleep(1)
  
  popular = ["a)bateria","b)guitarra","c)violin","d)ukelele"]
  for number2 in range (0,4):
   print (popular[number2])
  time.sleep(1)
               
  pregunta_3 = input("\nescribe tu respuesta:")

  while pregunta_3 not in ("a","b","c","d"):
    pregunta_3 = input("debes responder a , b, c o d. Ingresa nuevamente tu respuesta:")
  
  if pregunta_3 == "a" :
    print(RED+"totalmente incorrecto!"+RESET)
    puntaje = puntaje /2
  elif pregunta_3 == "b":
    print(YELLOW+"perfecto!respuesta correcta!"+RESET)
    puntaje = puntaje * 2
  elif pregunta_3 == "c":
    print(RED+"que lastima es incorrecto!!"+RESET)
    puntaje = puntaje**(1/2)
  else:
    print(RED+"lo siento,respuesta incorrecta"+RESET)
    puntaje = puntaje - 2

  print(BLUE+"\ngracias", nombre,"por jugar mi trivia obtuviste",puntaje,"puntos"+RESET)
  time.sleep(1) 
  print(GREEN+"\n¿Deseas intentar la trivia nuevamente?\n")
  time.sleep(1)
  repetir_trivia = input("ingresa´si´para repetir , o presiona cualquier tecla para finalizar: "+RESET).lower()

  if repetir_trivia != "si":
    
    inicio_trivia = False
  puntaje_total.append(puntaje)
  os.system("clear")

print(CYAN+"\nEspero ",nombre,"que lo hayas pasado bien, hasta pronto!"+RESET)
time.sleep(1)
print(GREEN+"\nResumen De Resultados:\n"+RESET)

for x in range (1,intentos+1):
 print("intento:",x,"\n")
 print("puntaje:",puntaje_total[x-1],"\n")

print("\ntotal:",sum(puntaje_total))

if sum(puntaje_total) > 20 :
 win = ["W","I","N","N","E","R"]
 for i in win :
        print(i, end = " ")
        time.sleep(0.2)
else:
 perdedor = ["G","A","M","E","  ","O","V","E","R"]
 for i in perdedor :
    print(i, end = " ")
    time.sleep(0.2)
  
