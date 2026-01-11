
# OBS: input sempre retorna string
nome_usuario = input("Digite seu nome: ")
print("Bem-vindo,", nome_usuario)

idade = int(input("Digite sua idade: "))
print("Sua idade é:", idade)

# Convertendo entrada para float
altura = float(input("Digite sua altura em metros: "))
print("Sua altura é:", altura)

peso = float(input("Digite seu peso em kg: "))
imc = peso / (altura ** 2)
print("Seu IMC é:", imc)

# Formatando a saída
print(f"Seu IMC é: {imc:.2f}")
print("Seu IMC é: {:.2f}".format(imc))

# Formatando a saída com f-strings
print(f"Seu nome é: {nome_usuario}")
print(f"Sua idade é: {idade}")
print(f"Sua altura é: {altura}")
print(f"Seu peso é: {peso}")
print(f"Seu IMC é: {imc:.2f}")

# Formatando a saída com format
print("Seu nome é: {}".format(nome_usuario))
print("Sua idade é: {}".format(idade))
print("Sua altura é: {}".format(altura))
print("Seu peso é: {}".format(peso))
print("Seu IMC é: {:.2f}".format(imc))

# Exemplo de múltiplas entradas
entrada = input("Digite seu nome, idade e altura separados por vírgula: ")
nome, idade, altura = entrada.split(",")
print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)

# Exemplo de múltiplas saídas
print("Nome:", nome, "Idade:", idade, "Altura:", altura)