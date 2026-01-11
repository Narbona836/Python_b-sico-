def saudacao(nome):
    """
    Função simples que recebe um parâmetro
    e retorna uma mensagem
    """
    return f"Olá, {nome}!"

print(saudacao("QA"))

# Função com valor padrão
def soma(a, b=10):
    return a + b

print(soma(5))
print(soma(5, 20))

# Função com número variável de argumentos
def multiplica(*numeros):
    resultado = 1
    for num in numeros:
        resultado *= num
    return resultado

print(multiplica(2, 3, 4))
print(multiplica(2, 3))