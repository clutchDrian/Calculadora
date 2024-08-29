import math
import numpy as np
#Utilizaremos la biblioteca math para Logaritmos.
suma=[]
multiplicacion=[]

#Utilizaremos numpy para suma y multplicación.

#RESTA
def resta():
    cant=int(input("Escribe la cantidad de numeros a restar: "))
    restato=None
    for i in range(cant):
        resta_numeros=float(input("Escribe el numero a restar: "))
        if restato is None:
            restato = resta_numeros
        else:
            restato=restato-resta_numeros
        print("El total es: ", restato)
#DIVISIÓN
def division():
    cantd=int(input("Escribe la cantidad de numeros a dividir: "))
    divto=None
    for i in range(cantd):
        div_num=float(input("Escribe el numero a dividir: "))
        if divto is None:
            divto = div_num
        else:
            divto=divto/div_num
        print("El total es: ", divto)
#MCD
def mcd(num1, num2):
  a=max(num1, num2)
  b=min(num1, num2)
  while b!=0:
    mcd=b
    b=a%b
    a=mcd
  return mcd

#MCM
def mcm(num1, num2):
  a=max(num1, num2)
  b=min(num1, num2)
  mcm=(a/mcd(a,b)) * b
  return mcm

#Raiz bajo cualquier indice
def raiz_random(numero, indice):
  return numero**((1.) / (indice))

#Factorial
def factorial(n):
   if n==0 or n==1:
            resultado=1
   elif n>1:
            resultado=n*factorial(n-1)
   return resultado


print("Calculadora - Proyecto Final")
print("")
while True:
  opciones = 0
  print("""
              ¿Que operación deseas hacer?

    1) Sumar        2) Restar        3) Multiplicar

    4) Dividir      5) Potencia      6) Raiz Cuadrada

    7) Raiz         8) MCM           9) MCD

    10) Factorial   11) Seno         12) Coseno

    13) Tangente    14) Residuo      15)Logaritmo

    """)
  opciones = int(input("Elige una opción: ") )
  if opciones == 1:
    print("")
    print("Elegiste SUMA")
    cantidad=int(input("¿Cuantos numeros vas a SUMAR? "))
    for i in range(cantidad):
      s=int(input("Introduce los numeros a sumar: "))
      suma=np.append(suma, s)
      print("La suma total es: ", np.sum(suma),)
    print("""

        ¿Continuar?

    1) Sí        2) No

    """)
    opcion2 = int(input("Elige una opción"))
    if opcion2 == 2:
      break
    elif opcion2 == 1:
      print("Volvamos a las operaciones...")
  elif opciones == 2:
    print("")
    print("Elegiste RESTA")
    resta()
    print("""

        ¿Continuar?

    1) Sí        2) No

    """)
    opcion2 = int(input("Elige una opción"))
    if opcion2 == 2:
      break
    elif opcion2 == 1:
      print("Volvamos a las operaciones")
  elif opciones == 3:
    print("")
    cantidad=int(input("¿Cuantos numeros vas a MULTIPLICAR? "))
    for i in range(cantidad):
      m=int(input("Introduce los numeros a multiplicar: "))
      multiplicacion=np.append(multiplicacion, m)
      print("El total es: ", np.prod(multiplicacion),)
    print("""

        ¿Continuar?

    1) Sí        2) No

    """)
    opcion2 = int(input("Elige una opción"))
    if opcion2 == 2:
      break
    elif opcion2 == 1:
      print("Volvamos a las operaciones...")
  elif opciones == 4:
    print("")
    print("Has elegido DIVISION")
    division()
    print("""

        ¿Continuar?

    1) Sí        2) No

    """)
    opcion2 = int(input("Elige una opción"))
    if opcion2 == 2:
      break
    elif opcion2 == 1:
      print("Volvamos a las operaciones...")
  elif opciones == 5:
    print("")
    print("Has elegido POTENCIA")
    numero=int(input("¿Que numero vas a querer potenciar?"))
    potencia=int(input("A que numero lo vas a elevar?"))
    print("")
    print("El numero", numero, "potenciado al valor", potencia,"es igual a: ", numero**potencia)
    print("""

        ¿Continuar?

    1) Sí        2) No

    """)
    opcion2 = int(input("Elige una opción"))
    if opcion2 == 2:
      break
    elif opcion2 == 1:
      print("Volvamos a las operaciones...")
  elif opciones == 6:
    print("")
    print("Has elegido RAIZ CUADRADA")
    raiz=int(input("Numero que le sacaras raiz cuadrada: "))
    rcuad=np.sqrt(raiz)
    print("")
    print("La raiz cuadrada de", raiz, "es: ", rcuad)
    print("""

        ¿Continuar?

    1) Sí        2) No

    """)
    opcion2 = int(input("Elige una opción"))
    if opcion2 == 2:
      break
    elif opcion2 == 1:
      print("Volvamos a las operaciones...")
  elif opciones == 7:
    print("")
    print("Has elegido RAIZ (Bajo cualquier indice)")
    num=int(input("¿Cual es el numero? : "))
    ind=int(input("Bajo el indice: "))
    print("")
    print("La Raiz de", num, "bajo el indice", ind, "es igual a:")
    print(raiz_random(num, ind))
    print("""

        ¿Continuar?

    1) Sí        2) No

    """)
    opcion2 = int(input("Elige una opción"))
    if opcion2 == 2:
      break
    elif opcion2 == 1:
      print("Volvamos a las operaciones...")
  elif opciones == 8:
    print("")
    print("Has elegido Minimo Común Multiplo")
    num1= int(input("Ingresa primer numero: "))
    num2= int(input("Ingresa segundo numero: "))
    print("")
    print("El Minimo Común Multiplo entre ", num1, "y ", num2, "es: ", mcm(num1, num2))
    print("""

        ¿Continuar?

    1) Sí        2) No

    """)
    opcion2 = int(input("Elige una opción"))
    if opcion2 == 2:
      break
    elif opcion2 == 1:
      print("Volvamos a las operaciones...")
  elif opciones == 9:
    print("")
    print("Has elegido Maximo Común Divisor")
    num1= int(input("Ingresa primer numero: "))
    num2= int(input("Ingresa segundo numero: "))
    print("")
    print("El Maximo Común Divisor entre ", num1, "y ", num2, "es: ", mcd(num1, num2))
    print("""

        ¿Continuar?

    1) Sí        2) No

    """)
    opcion2 = int(input("Elige una opción"))
    if opcion2 == 2:
      break
    elif opcion2 == 1:

      print("Volvamos a las operaciones...")
  elif opciones == 10:
    print("")
    print("Has elegido FACTORIAL")
    numero=int(input("Ingrese numero a sacar el factorial: "))
    print("El factorial de", numero, "es: " , factorial(numero))
    print("""

        ¿Continuar?

    1) Sí        2) No

    """)
    opcion2 = int(input("Elige una opción"))
    if opcion2 == 2:
      break
    elif opcion2 == 1:
      print("Volvamos a las operaciones...")
  elif opciones == 11:
    print("")
    print("Has elegido SENO")
    numero=int(input("¿A que numero desea sacar SENO? "))
    print("El SENO de", numero, "es: ", np.sin(numero))
    print("""

        ¿Continuar?

    1) Sí        2) No

    """)
    opcion2 = int(input("Elige una opción"))
    if opcion2 == 2:
      break
    elif opcion2 == 1:
      print("Volvamos a las operaciones...")
  elif opciones == 12:
    print("")
    print("Has elegido COSENO")
    numero=int(input("¿A que numero desea sacar COSENO? "))
    print("El COSENO de", numero, "es: ", np.cos(numero))
    print("""

        ¿Continuar?

    1) Sí        2) No

    """)
    opcion2 = int(input("Elige una opción"))
    if opcion2 == 2:
      break
    elif opcion2 == 1:
      print("Volvamos a las operaciones...")
  elif opciones == 13:
    print("")
    print("Has elegido TANGENTE")
    numero=int(input("¿A que numero desea sacar TANGENTE? "))
    print("El TANGENTE de", numero, "es: ", np.tan(numero))
    print("""

        ¿Continuar?

    1) Sí        2) No

    """)
    opcion2 = int(input("Elige una opción"))
    if opcion2 == 2:
      break
    elif opcion2 == 1:
      print("Volvamos a las operaciones...")
  elif opciones == 14:
    print("")
    print("Has elegido RESIDUO")
    num1=int(input("Elige primer numero: "))
    num2=int(input("Elige segundo numero: "))
    print("El residuo de ", num1,"/", num2,"es igual a ", num1%num2)
    print("""

        ¿Continuar?

    1) Sí        2) No

    """)
    opcion2 = int(input("Elige una opción"))
    if opcion2 == 2:
      break
    elif opcion2 == 1:
      print("Volvamos a las operaciones...")
  elif opciones == 15:
    print("")
    print("Has elegido LOGARITMO")
    argumento=int(input("Logaritmo del numero: "))
    base=int(input("En base: "))
    print("")
    print("El logaritmo del numero ", argumento, "en base", base, "es igual a: ", math.log(argumento, base))
    print("""

        ¿Continuar?

    1) Sí        2) No

    """)
    opcion2 = int(input("Elige una opción"))
    if opcion2 == 2:
      break
    elif opcion2 == 1:
      print("Volvamos a las operaciones... ")
  else:
    print("INCORRECTO. Por favor eliga una opción valida desde el 1 hasta el 15")