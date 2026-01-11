# Exemplo de loop for em uma lista
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(f"Número: {numero}")

# Loop com range
for i in range(5):
    print(i)  # 0 até 4

# Exemplo de loop while

contador = 0

while contador < 3:
    print("Contador:", contador)
    contador += 1
print("Loop encerrado.")

# Usando break e continue
for i in range(10):
    if i == 5:
        break  # Sai do loop quando i é 5
    if i % 2 == 0:
        continue  # Pula números pares
    print(i)  # Imprime apenas números ímpares menores que 5
print("Fim do programa.")