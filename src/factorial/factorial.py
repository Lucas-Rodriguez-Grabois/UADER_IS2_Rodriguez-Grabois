#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

if len(sys.argv) == 1:# si se omite el argumento, lo solicita 
    entrada = input("Por favor, ingrese el número o rango (ej: 10, 4-8, -10, 10-): ")
else:# si existe, lo toma de la terminal
    entrada = sys.argv[1]

# procesamiento de rangos
inicio = 1
fin = 1

if "-" in entrada:
    partes = entrada.split("-")
    
    if partes[0] == "":# caso "-hasta"
        inicio = 1
        fin = int(partes[1])
    
    elif partes[1] == "":# caso "desde-"
        inicio = int(partes[0])
        fin = 60
     
    else:# caso "desde-hasta"
        inicio = int(partes[0])
        fin = int(partes[1])
else:# caso de un solo número
    inicio = int(entrada)
    fin = inicio

for n in range(inicio, fin + 1):
    print(f"Factorial de {n}! es {factorial(n)}")