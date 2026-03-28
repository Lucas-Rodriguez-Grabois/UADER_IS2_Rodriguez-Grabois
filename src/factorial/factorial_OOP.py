#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

class Factorial:
    # el constructor __init__ se ejecuta al crear el objeto
    def __init__(self):
        print("Instancia de la clase Factorial creada.")

    # metodo privado para el cálculo matemático
    def _calcular(self, n):
        if n < 0: return 0
        if n == 0: return 1
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

    def run(self, min_val, max_val):# run(min, max)
        for n in range(min_val, max_val + 1):
            resultado = self._calcular(n)
            print(f"Factorial de {n}! es {resultado}")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        entrada = input("Ingrese número o rango (ej: 4-8): ")
    else:
        entrada = sys.argv[1]

    inicio, fin = 1, 1
    if "-" in entrada:
        partes = entrada.split("-")
        inicio = int(partes[0]) if partes[0] != "" else 1
        fin = int(partes[1]) if partes[1] != "" else 60
    else:
        inicio = fin = int(entrada)

    #uso de la Clase POO
    mi_factorial = Factorial() 
    mi_factorial.run(inicio, fin) 