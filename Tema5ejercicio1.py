# Escribe una función que calcule el área de un triángulo,
# recibiendo la altura y la base como parámetros y otra función
# que calcule el área de un círculo recibiendo el radio del mismo.

def areatriangulo():
    area = float((base*altura)/2)
    print('el area del triángulo es:', area)
altura = float(input('escribe altura:'))
base = float(input('escribe la base:'))


def areacircunferencia():
    areacircunferencia = float(3.1416*radio)
    print('el area de la circunferencia es:', areacircunferencia)
radio=float(input('escribe radio:'))

areatriangulo()
areacircunferencia()
















