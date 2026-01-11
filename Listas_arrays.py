# Lista é uma coleção ordenada e mutável
frutas = ["maçã", "banana", "uva"]

print(frutas[0])  # Acessa o primeiro elemento

# Adicionando item
frutas.append("laranja")

# Removendo item
frutas.remove("banana")

print(frutas)

# Percorrendo lista
for fruta in frutas:
    print(fruta)

# Array (usando a biblioteca array)
import array

numeros = array.array('i', [1, 2, 3, 4, 5])

print(numeros[0])  # Acessa o primeiro elemento 