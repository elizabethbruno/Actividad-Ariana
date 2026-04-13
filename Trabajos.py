# ETAPAS:
# Un sistema que consulte la edad, y de acuerdo a ella indique si la persona es mayor de edad o no.

# Crear un programa de validación de usuario y contraseña (consultar usuario y contraseña), los únicos dos usuarios conectados son:
# User1: pedro   	Contraseña1: 1234
# User2: angel		Contraseña2: a4s1
# Solicitar el ingreso de 3 notas por pantalla, luego calcular el promedio de las 3 notas (cada nota tiene la misma ponderación), finalmente indicar con una salida de pantalla “Aprobado” en el caso de que el promedio sea igual o mayor a 4.0.

import os
os.system ("cls")


try:
    edad= int(input("ingrese su edad\n"))
    if edad >= 18:
        print ("eres mayor de edad")
    else:
        print("eres menor de edad")

except:
    print ("debe ingresar un numero")

user1= "pedro"
contraseña1= "1234"
user2= "angel"
contraseña2= "a4s1"

user = input("ingrese su nombre de usuario\n")
contraseña = input ("ingrese su contraseña\n")
if user == user1 and contraseña == contraseña1 or user == user2 and contraseña == contraseña2:
    print(f"Hola {user}, puedes acceder al sistema")
else:
    print("No puede acceder")

cantidad = 3
acumulador_nota =0
for x in range (3):
    nota = float(input(f"ingrese nota ({x+1})\n"))
    acumulador_nota = acumulador_nota + nota
promedio = acumulador_nota / cantidad
if promedio >= 4:
    print ("aprobado")
else:
    print("reprobado")