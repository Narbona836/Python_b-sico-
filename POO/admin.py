# =========================================
# HERANÇA
# =========================================


from .usuario import Usuario



class Admin(Usuario):
    """
    Classe que herda de Usuario.
    Representa um usuário administrador.
    """

    def __init__(self, nome: str, email: str, nivel_acesso: int):
        # Chama o construtor da classe pai (Usuario)
        super().__init__(nome, email)
        self._nivel_acesso = nivel_acesso

    def promover_usuario(self, usuario: Usuario):
        """
        Método exclusivo do Admin.
        """
        print(f"{usuario._nome} foi promovido por {self._nome}")

    def __str__(self) -> str:
        """
        Polimorfismo:
        sobrescreve o método __str__ da classe pai.
        """
        return (
            f"Admin: {self._nome} | "
            f"Email: {self._email} | "
            f"Nível de acesso: {self._nivel_acesso}"
        )