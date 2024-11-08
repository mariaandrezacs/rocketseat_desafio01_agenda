# CREATING THE CONTACT CLASS
class Contato:
    def __init__(self, nome, telefone, email, favorito=False):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.favorito = favorito

    def __str__(self):
        favorito_str = " (Favorito)" if self.favorito else ""
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}{favorito_str}"