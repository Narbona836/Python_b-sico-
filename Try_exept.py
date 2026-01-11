try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: divisão por zero")
except Exception as erro:
    print("Erro inesperado:", erro)
else:
    print("Deu tudo certo")
finally:
    print("Finalizando execução")

print("Programa continua...")