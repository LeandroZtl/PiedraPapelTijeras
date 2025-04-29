import random
opciones=["Tijera","Piedra","Papel"]
historial=[]
elegido=0
maquina=0
seguirjugando=True
while seguirjugando:
    def mostrar_historial():
        print ("\nHistorial de las ultimas  20 partidas")
        for i, partida in enumerate(historial,1):
            print (f"Partida {i}:{partida}")

    def cargar_historial(resultado,elegido,maquina):
        if len(historial)>=20:
            historial.pop(0)
        historial.append(f"Jugador: {opciones[elegido-1]},Maquina: {opciones[maquina-1]}, Resultado: {resultado}")

    print ("Empieza El Piedra Papel o Tijeras, que elegis? ")
    print ("ingresa 1 para tijera, 2 para piedra, 3 para papel y mira que eligio la maquina")
    elegido=int(input())
    if 1 <= elegido <= 3:
        print (f"elegiste {opciones[elegido-1]}")

    maquina=random.randint(1,3)
    print (f"la maquina eligio {opciones[maquina-1]}")
    if elegido==maquina:
        resultado="Empataron."
    elif (elegido== 1 and maquina== 3) or (elegido == 2 and maquina== 1 ) or (elegido== 3 and maquina== 2 ):
        resultado="Ganaste."
    else:
        resultado="Perdiste."
    print (resultado)

    cargar_historial(resultado, elegido, maquina)
    print("\n¿Quieres ver el historial? (S/N)")
    respuesta = input().strip().upper()
    if respuesta == "S":
        mostrar_historial()
    elif respuesta=="N":
        seguirjugando=False
