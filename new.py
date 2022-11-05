from colorama import Fore, init
import os, time

init(autoreset=True)

menu ="""
Que te gustaria realizar: 
1. Suma
2. Resta
3. Multiplicacion
4. Division
S. Salir
"""

while True:
      print(Fore.GREEN + menu)
      print("\n")
      choice = input("Ingrese su eleccion: ").capitalize()
      os.system("cls")
      
      if choice == "S":
            print(Fore.YELLOW + "Gracias por usar nuestro programa!")
            break

      num1 = int(input("Numero 1: "))
      num2 = int(input("Numero 2: "))
      
      os.system('cls')

      if choice == "1":
            operacion = num1 + num2
            print(Fore.CYAN + f"El Resultado de la Suma es de: {operacion}")
            time.sleep(3)
      elif choice == "2":
            operacion = num1 - num2
            print(Fore.CYAN + f"El Resultado de la Resta es de: {operacion}")
            time.sleep(3)
      elif choice == "3":
            operacion = num1 * num2
            print(Fore.CYAN + f"El Resultado de la Resta es de: {operacion}")
            time.sleep(3)
      elif choice == "4":
            operacion = num1 / num2
            print(Fore.CYAN + f"El Resultado de la Resta es de: {operacion}")
            time.sleep(3)
      
      os.system("cls")