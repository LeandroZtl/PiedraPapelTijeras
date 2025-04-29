import random
elegido=0
maquina=0
print ("vamos a jugar piedra papel o tijeras")
print ("ingresa un numero, el 1 es tijera, el 2 es piedra, el 3 es papel")
elegido=int(input())
if (elegido==1):
    print ("elegiste  tijera")
elif (elegido==2):
    print ("elegiste piedra")
elif (elegido==3):
    print ("elegiste papel")
else:
   print ("eleccion invalida")
maquina=random.randint(1,3)
if (maquina==1):
    print ("eligio tijera")
elif (maquina==2):
    print ("eligio piedra")
elif (maquina==3):
    print ("eligio papel")

if (elegido==maquina):
    print ("empataron")
elif (elegido==1 and maquina==3) or (elegido==2 and maquina==1) or (elegido==3 and maquina==2):
    print ("ganaste")
else:
    print ("perdiste")
