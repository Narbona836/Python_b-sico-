# =========================================
# USO DAS CLASSES (INSTÂNCIA)
# =========================================

from POO.usuario import Usuario
from POO.admin import Admin



if __name__ == "__main__":
    # Criando objetos (instâncias)
    usuario_comum = Usuario("João", "joao@email.com")
    admin = Admin("Maria", "maria@email.com", nivel_acesso=10)

    # Usando métodos
    print(usuario_comum)
    print(admin)

    usuario_comum.desativar()
    print(usuario_comum)

    admin.promover_usuario(usuario_comum)
    print(admin)

    # Verificando status
    print(usuario_comum.esta_ativo())
    print(admin.esta_ativo())