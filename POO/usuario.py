# =========================================
# EXEMPLO DIDÁTICO DE POO EM PYTHON
# =========================================




class Usuario:
    """
    Classe base que representa um usuário genérico do sistema.
    """

    def __init__(self, nome: str, email: str):
        # Atributos protegidos (convenção com _)
        self._nome = nome
        self._email = email
        self._ativo = True

    def desativar(self):
        """
        Desativa o usuário.
        """
        self._ativo = False

    def ativar(self):
        """
        Ativa o usuário.
        """
        self._ativo = True

    def esta_ativo(self) -> bool:
        """
        Retorna o status do usuário.
        """
        return self._ativo

    def __str__(self) -> str:
        """
        Representação em texto do objeto.
        """
        status = "Ativo" if self._ativo else "Inativo"
        return f"Usuário: {self._nome} | Email: {self._email} | Status: {status}"