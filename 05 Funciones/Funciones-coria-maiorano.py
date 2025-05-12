#Ejercicio 1
'''def imprimir_hola_mundo() :
    print("Hola mundo")
     

imprimir_hola_mundo()  '''
#Ejercicio 2    
'''def saludar_usuario(nombre) :
    print(f"Hola {nombre} !")

nombre=str(input("Ingrese el nombre de quien quiere saludar:"))
saludar_usuario(nombre) '''
#Ejercicio 3
'''def informacion_personal(nombre, apellido,edad, residencia) :
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia} ")

nombre=str(input("Ingresa tu nombre:"))
apellido=str(input("Ingrese tu apellido:"))
edad=int(input("Ingrese tu nombre:"))
residencia=str(input("Ingrese donde vive:"))

informacion_personal(nombre,apellido,edad,residencia) '''
#Ejercicio 4
'''import math 
def calcular_area_circulo(radio) :
    area= radio *radio * math.pi   
    print(f"El area del circulo es {round(area, 2)}")
def calcular_perimetro_circulo(radio) :
    perimetro=2 *math.pi *radio
    print(f"El perimetro del circulo es {round(perimetro, 2)}")
radio=int(input("Ingrese el radio del circulo y te devolvemos el perimetro y area:"))

calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)'''
#Ejercicio 5
'''def segundos_a_horas(segundos):
    hora=segundos/360
    print(f"Los segundos ingresados son {hora} horas")

segundos=int(input("Ingrese segundos para ver cuantos horas son:"))

segundos_a_horas(segundos)'''
#Ejercicio 6

'''def tabla_multiplicar(numero):
    i=1
    while i <=10:
        print(f"{numero} x {i} = {numero * i}")
        i+=1


numero=int(input("Ingrese un numero y te devuelvo la tabla de multiplicar:"))
tabla_multiplicar(numero)'''
#Ejercicio 7
'''def operaciones_basicas(a, b):
     print(f"{a} x {b} = {a * b}")
     print(f"{a} + {b} = {a + b}")
     print(f"{a} - {b} = {a - b}")
     print(f"{a} / {b} = {a / b}")

a=int(input("Ingrese un numero:"))
b=int(input("Ingrese otro numero:"))

operaciones_basicas(a,b)'''
#Ejercicio 8
'''def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    imc = round(imc, 2)
    print(f"Tu imc es {imc}")
peso=float(input("Ingrese su peso:"))
altura=float(input("Ingrese su altura:"))

calcular_imc(peso, altura)'''
#Ejercicio 9
'''def celsius_a_fahrenheit(celsius):
    fahrenheit=((celsius*(9/5))+32)
    print(f"tu temperatura en celsius era de {celsius} y en fahrenheit es {fahrenheit}")

celsius=int(input("Ingrese su temperatura en celsius:"))
celsius_a_fahrenheit(celsius)'''
#Ejercicio 10
'''def calcular_promedio(a, b, c):
    promedio=((a+b+c)/3)
    print(f"su promedio es de {promedio}")

a=float(input("Ingrese un numero:"))
b=float(input("Ingrese otro numero:"))
c=float(input("Ingrese otro numero:"))
calcular_promedio(a, b, c)'''