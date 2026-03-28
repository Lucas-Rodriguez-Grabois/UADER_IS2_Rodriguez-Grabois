import matplotlib.pyplot as plt

def calcular_collatz(n):
    iteraciones = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        iteraciones += 1
    return iteraciones

numeros_n = list(range(1, 10001))
lista_iteraciones = []

for n in numeros_n:
    lista_iteraciones.append(calcular_collatz(n))

plt.figure(figsize=(10, 6))

plt.scatter(lista_iteraciones, numeros_n, s=1, color='blue', alpha=0.5)

plt.title("Conjetura de Collatz (1 a 10,000)")
plt.xlabel("Número de iteraciones para converger (Abscisas)")
plt.ylabel("Número n de comienzo (Ordenadas)")

plt.grid(True, linestyle=':', alpha=0.6)
plt.show()