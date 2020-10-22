#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Ezequiel Alarcon"
__email__ = "zekalarcon@gmail.com"



def ej1():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite por consola 2 números
    Calcule la diferencia entre ellos e informe por pantalla
    si el resultado es positivo, negativo o cero.
    '''

    print('Ingrese 2 numeros para saber si la diferencia es positiva, negativa, o 0')

    num_1 = int(input('Ingrese primer numero:\n'))
    num_2 = int(input('Ingrese segundo numero:\n'))

    resta = num_1 - num_2

    if resta > 0:
        print(f'La diferencia entre los numeros ingresados es {resta}, numero positivo')
    elif resta < 0:
        print(f'La diferencia entre los numeros ingresados es {resta}, numero negativo')
    else:
        print('La diferencia entre los numeros ingresados es 0')        


def ej2():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el resultado en pantalla.
    '''

    print('Ingrese 3 numeros para saber si son par o impar')

    num_1 = int(input('Ingrese primer numero:\n'))
    num_2 = int(input('Ingrese segundo numero:\n'))
    num_3 = int(input('Ingrese tercer numero:\n'))

    if (num_1 % 2) == 0:
        print(f'Numero {num_1} es par')
    else:
        print(f'Numero {num_1} es impar')  

    if (num_2 % 2) == 0:
        print(f'Numero {num_2} es par')
    else:
        print(f'Numero {num_2} es impar') 

    if (num_3 % 2) == 0:
        print(f'Numero {num_3} es par')
    else:
        print(f'Numero {num_3} es impar')           
        

def ej3():
    print('Ejercicios de práctica con números')

    '''
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se desea ejecutar
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)

    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    '''

    print('Ingrese dos numeros para realizar las siguientes operaciones:')

    num_1 = int(input('Ingrese primer numero:\n'))
    num_2 = int(input('Ingrese segundo numero:\n'))
    
    print(
        '-Ingrese el simbolo (+) para suma\n'
        '-Ingrese el simbolo (-) para resta\n'
        '-Ingrese el simbolo (*) para multiplicacion\n'
        '-Ingrese el simbolo (/) para division\n'
        '-Ingrese el simbolo (**) para exponente/potencia\n'
    )

    simbolo = str(input('Ingrese simbolo:\n'))

    if simbolo == '+':
        suma = num_1 + num_2
        print(f'La suma entre {num_1} y {num_2} es: {suma}')
    elif simbolo == '-':
        resta = num_1 - num_2
        print(f'La resta entre {num_1} y {num_2} es: {resta}')
    elif simbolo == '*':
        multiplicacion = num_1 * num_2
        print(f'La multiplicacion entre {num_1} y {num_2} es: {multiplicacion}')
    elif simbolo == '/':
        division = num_1 / num_2
        print(f'La division entre {num_1} y {num_2} es: {division}')
    elif simbolo == '**':
        potencia = num_1 ** num_2
        print(f'La potencia entre {num_1} y {num_2} es: {potencia}')
    else:
        print('El simbolo ingresado es incorrecto')                


def ej4():
    print('Ejercicios de práctica con cadenas')

    '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)

    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor

    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor
    '''

    print('Ingrese 3 palabras y elija una opcion para ver el resultado:\n')

    palabra_1 = str(input('Ingrese primer palabra:\n'))
    palabra_2 = str(input('Ingrese segunda palabra:\n'))
    palabra_3 = str(input('Ingrese tercer palabra:\n'))
    
    print(
        '- Ingrese 1 para ordenar alfabeticamente\n'
        '- Ingrese 2 para ordenar por cantidad de letras\n'
    )


    opcion = int(input('Elija una opcion:\n'))

    lista_palabras = (palabra_1, palabra_2, palabra_3)

    if opcion == 1:
        palabras_ordenadas = sorted(lista_palabras)
        palabras_ordenadas = ', '.join(palabras_ordenadas)
        print(f'Palabras ordenadas alfabeticamente:\n{palabras_ordenadas}')
    elif opcion == 2:
        palabras_ordenadas = sorted(lista_palabras, key=len, reverse=True)
        palabras_ordenadas = ', '.join(palabras_ordenadas)
        print(f'Palabras ordenadas por cantidad de caracteres:\n{palabras_ordenadas}')
    else:
        ('La opcion ingresada no es valida')    
        

        
def ej5():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?

    En cada caso imprimir en pantalla el resultado
    '''

    print('Ingrese 3 temperaturas y elija una opcion para ver el resultado')

    temp_1 = float(input('Ingrese primer temperatura:\n'))
    temp_2 = float(input('Ingrese segunda temperatura:\n'))
    temp_3 = float(input('Ingrese tercer temperatura:\n'))

    print(
        '- Elija 1 para saber cual temperatura es la maxima\n'
        '- Elija 2 para saber cual temperatura es la minima\n'
        '- Elija 3 para saber el promedio entre las tres temperaturas\n'
    )


    opcion = int(input('Ingrese opcion:\n'))

    temperaturas = (temp_1, temp_2, temp_3)

    if opcion == 1:
        temp_max = max(temperaturas)
        print(f'La temperatura maxima ingresada es:\n{temp_max}')
    elif opcion == 2:
        temp_min = min(temperaturas)  
        print(f'La temperatura minima ingresada es:\n{temp_min}')
    elif opcion == 3:
        promedio = (temp_1 + temp_2 + temp_3) / 3
        print(f'El promedio entre las temperaturas es:\n{promedio}')
    else:
        print('La opcion ingresada no es valida')          


if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
