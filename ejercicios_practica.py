#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Ezequiel Alarcon"
__email__ = "zekalarcon@gmail.com"


def ej1():
    # Ejercicios de práctica numérica

    # Comparadores
    # Ingrese dos números cualesquiera y realice las sigueintes
    # comparaciones entre ellos
    numero_1 = int(input('Ingrese el primer número:\n'))

    numero_2 = int(input('Ingrese el segundo número:\n'))

    # Compare cual de los dos números es mayor
    # Imprima en pantalla según corresponda

    if numero_1 > numero_2:
        print(f'El primer numero ingresado es mayor que el segundo {numero_1} > {numero_2}')
    else:
        print(f'El segundo numero ingresado es mayor que el primero {numero_2} > {numero_1}')


    # Verifique si el numero_1 positivo, negativo o cero
    # Imprima el resultado en cada caso

    if numero_1 > 0:
        print(f'El {numero_1} es positivo')
    elif numero_1 < 0:
        print(f'El {numero_1} es negativo')
    else:
        print('El numero es 0')        

    # Verifique si el numero_1 es mayor a 0 y menor a 100
    # Imprima en pantalla si se cumple o no la condición

    if numero_1 > 0 and numero_1 < 100:
        print(f'El numero {numero_1} es mayor a 0 y menor que 100, cumple con la condicion')
    else:
        if numero_1 == 0:
            print('El numero es 0, no cumple la condicion')
        elif numero_1 < 0:
            print('El numero es menor a 0, no cumple la condicion')  
        else:
            print('El numero es mayor a 100, no cumple la condicion')          

    # Verifique si el numero_1 es menor a 10 o el numero_2
    # es mayor a -2
    # Imprima en pantalla si se cumple o no la condición

    if numero_1 < 10 or numero_2 > -2:
        if numero_1 < 10:
            print(f'El primer numero ingreado: {numero_1}\nCumple la condicion')
        elif numero_2 > -2:
            print(f'El segundo numero ingresado: {numero_2}\nCumple la condicion')    
    else:
        print('Los numeros no cumplen ninguna condicion')
                
          



def ej2():
    # Ejemplos variables de texto

    # Comparadores
    # Ingrese dos palabras cualesquiera y realice las sigueintes
    # comparaciones entre ellas
    texto_1 = str(input('Ingrese la primera palabra:\n'))

    texto_2 = str(input('Ingrese la segunda palabra:\n'))

    # Compare cual de las dos palabras es mayor (alfabéticamente)
    # Imprima en pantalla según corresponda
    
    if texto_1 > texto_2:
        print(f'La palabra "{texto_1}" es mayor alfabeticamente que la palabra "{texto_2}"')
    elif texto_2 > texto_1:
        print(f'La palabra "{texto_2}" es mayor alfabeticamente que la palabra "{texto_1}"')
    else:
        print(f'La palabra "{texto_1}" y "{texto_2}" son iguales alfabeticamente')        

    # Compare cual de las dos palabras tiene mayor
    # cantidad de letras
    # Imprima en pantalla según corresponda

    if len(texto_1) > len(texto_2):
        print(f'La palabra "{texto_1}" tiene mayor catidad de letras que la palabra "{texto_2}"')
    elif len(texto_2) > len(texto_1):
        print(f'La palabra "{texto_2}" tiene mayor catidad de letras que la palabra "{texto_1}"') 
    else:
        print(f'Las palabras "{texto_1}" y "{texto_2}" tienen la misma cantidad de letras')       

    # Verifique si la primera letra de la primera palabra
    # es mayor a la primera letra de la segunda palabra
    # Imprima en pantalla según corresponda

    if texto_1[:1] > texto_2[:1]:
        print(f'La primer letra "{texto_1[:1]}" es mayor alfabeticamente que la primer letra "{texto_2[:1]}"')
    elif texto_2[:1] > texto_1[:1]:
        print(f'La primer letra "{texto_2[:1]}" es mayor alfabeticamente que la primer letra "{texto_1[:1]}"')
    else:
        print(f'La primer letra "{texto_1[:1]}" y primer letra "{texto_2[:1]}" son iguales alfabeticamente')       

    copia_texto_1 = texto_1  # Copia de la variable texto_1

    # Verifique que copia_texto_1 es igual a texto_1
    # Imprima en pantalla según corresponda
    if copia_texto_1 == texto_1:
        print(f'La palabra "{copia_texto_1}" es igual a "{texto_1}"')
    else:
        print(f'La palabra "{copia_texto_1}" es diferente a "{texto_1}"')    

    # Verifique que copia_texto_1 es distinta a texto_2
    # Imprima en pantalla según corresponda

    if copia_texto_1 != texto_2:
        print(f'La palabra "{copia_texto_1}" es diferente a "{texto_2}"')
    else:
        print(f'La palabra "{copia_texto_1}" es igual a "{texto_2}"')    


def ej3():
    # Ejercicios de práctica numérica

    # Condicionales anidados
    numero_1 = 3
    numero_2 = 5

    # Verifique si el numero_1 es mayor a 5
    #   --> En caso afirmativo, verifique si el numero_2
    #       es positivo
    #       --> En caso afirmativo imprima en pantalla "Resp=1"
    #       --> En caso negativo imprima en pantalla   "Resp=2"
    #  --> En caso negativo (numero_1 no es mayor a 5)
    #      verifique si el numero_2 es mayor a 5
    #       --> En caso afirmativo imprima en pantalla "Resp=3"
    #       --> En caso negativo imprima en pantalla "Resp=4"

    if numero_1 > 5:
        if numero_2 > 0:
            print('Resp = 1')
        else:
            print('Resp = 2')
    elif numero_1 <= 5:
        if numero_2 > 5:
            print('Resp = 3')
        else:
            print('Resp = 4')            
    
    # Verifique la calificación de un estudiante según su
    # puntaje en un examen
    puntaje = 70

    # Si el puntaje es mayor igual a 90 --> imprimir A
    # Si el puntaje es mayor igual a 80 --> imprimir B
    # Si el puntaje es mayor igual a 70 --> imprimir C
    # Si el puntaje es mayor igual a 60 --> imprimir D
    # Si el puntaje es manor a  60      --> imprimir F

    # Debe imprimir en pantalla la calificacion
    # Utilizar "if" anidados

    if puntaje >= 90:
        print('A')
    elif puntaje >= 80:
        print('B')
    elif puntaje >= 70:
        print('C')
    elif puntaje >= 60:
        print('D')
    elif puntaje < 60:
        print('F')
                                 


def ej4():
    # Ejemplos variables de texto

    texto_1 = '7'
    texto_2 = '5'

    # Verifique cual cual de los dos textos es mayor alfabéticamente
    # Imprima en pantalla según corresponda

    if texto_1 > texto_2:
        print(f"Alfabeticamente el string '{texto_1}' es mayor que el string '{texto_2}'")
    elif texto_2 > texto_1:
        print(f"Alfabeticamente el string '{texto_2}' es mayor que el string '{texto_1}'")
    else:
        print(f"Alfabeticamente los strings '{texto_1}' y '{texto_2}' son iguales")    

    # Transforma esas variables tipo texto y almacénalas
    # en nuevas variables númericas (int)
    # Repita el proceso, ¿Cuál de las nuevas variables es mayor?
    # Imprima en pantalla según corresponda

    numero_1 = int(texto_1)
    numero_2 = int(texto_2) 
        
           
    if numero_1 > numero_2:
        print(f'El numero {numero_1} es mayor que el numero {numero_2}')
    elif numero_2 > numero_1:
        print(f'El numero {numero_2} es mayor que el numero {numero_1}')
    else:
        print(f'Los numeros {numero_1} y {numero_2} son iguales')        

    # Para pensar!
    # ¿Por qué cree que texto_2 es mayor a texto_1?
    # Siendo números tiene sentido, pero son caracteres, texto,
    # aún así el operador arroja el mismo resultado que con las
    # variables numéricas, cierto? ¿Por qué creen que es así?
    # Esta pregunta estará repetida en el Campus para que puedan
    # responder.
    # NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
