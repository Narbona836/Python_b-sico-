# Estrutura chave-valor
usuario = {
    "nome": "Willian",
    "idade": 30,
    "ativo": True
}

print(usuario["nome"])
print(usuario.get("idade"))

# Adicionando nova chave
usuario["email"] = "willian@email.com"

# Percorrendo dicionário
for chave, valor in usuario.items():
    print(chave, ":", valor)

# Removendo chave
del usuario["ativo"]
print(usuario)

# Verificando se chave existe
if "nome" in usuario:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")

# Limpando dicionário
usuario.clear()
print(usuario)