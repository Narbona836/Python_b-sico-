# Tupla é imutável (não pode ser alterada)
cores = ("vermelho", "verde", "azul")
print(cores[1])
print(type(cores))

# Desempacotamento de tuplas
r, g, b = cores
print(r)
print(g)
print(b)

# Tuplas podem conter diferentes tipos de dados
tupla_mista = (1, "dois", 3.0, True)
print(tupla_mista)
print(type(tupla_mista))

# Tuplas aninhadas
tupla_aninhada = (1, (2, 3), (4, 5))
print(tupla_aninhada)
print(type(tupla_aninhada))

