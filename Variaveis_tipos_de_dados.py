# Python é tipagem dinâmica (não precisa declarar o tipo)
nome = "Willian"          # string (str)
idade = 30                # inteiro (int)
altura = 1.75             # decimal (float)
ativo = True              # booleano (bool)

print(nome, idade, altura, ativo)

# Verificando o tipo da variável
print(type(nome))
print(type(idade))
print(type(altura))
print(type(ativo))

# Alterando o tipo da variável
idade = "trinta"          # agora é uma string
print(idade)
print(type(idade))

# Conversão de tipos
altura_str = str(altura)  # convertendo float para string
print(altura_str)
print(type(altura_str))

idade_int = int(30)      # convertendo string para int
print(idade_int)
print(type(idade_int))

ativo_bool = bool(1)     # convertendo int para bool
print(ativo_bool)
print(type(ativo_bool))

# Variáveis compostas
lista_nomes = ["Ana", "Bruno", "Carlos"]  # lista (list)
dicionario_idades = {"Ana": 25, "Bruno": 28}  # dicionário (dict)
tupla_alturas = (1.65, 1.80, 1.75)  # tupla (tuple)     
conjunto_numeros = {1, 2, 3, 4, 5}  # conjunto (set) 

print(lista_nomes)
print(dicionario_idades)
print(tupla_alturas)
print(conjunto_numeros)
print(type(lista_nomes))
print(type(dicionario_idades))
print(type(tupla_alturas))
print(type(conjunto_numeros))

# Comentários em Python

# Este é um comentário de uma linha

"""Este é um 
    comentário
        de várias 
            linhas"""

'''Este também é um 
comentário de várias linhas'''

print("Olá, mundo!")


