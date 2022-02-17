"""
Rosales Blanco Victor Ernesto
Creado: 16/02/2022
Ultima modificacion: 16/02/2022

Diseña un programa que reciba una
cierta cantidad de céntimos, y calcule
su equivalente en el mínimo número de
monedas ($5, $2, $1, $0.5, $0.2, $0.1 )

"""

cent = int(input("Escribe la cantidad de centimos: "))

if cent >= 500:
    cantidad = cent // 500
    print("monedas de 5 pesos: " + str(cantidad))
    cent = cent % 500

if cent >= 200:
    cantidad = cent // 200
    print("monedas de 2 pesos: " + str(cantidad))
    cent = cent % 200

if cent >= 100:
    cantidad = cent // 100
    print("monedas de 1 pesos: " + str(cantidad))
    cent = cent % 100

if cent >= 50:
    cantidad = cent // 50
    print("monedas de 50 centavos: " + str(cantidad))
    cent = cent % 50

if cent >= 20:
    cantidad = cent // 20
    print("monedas de 20 centavos: " + str(cantidad))
    cent = cent % 20

if cent >= 10:
    cantidad = cent // 10
    print("monedas de 10 centavos: " + str(cantidad))
    cent = cent % 10


