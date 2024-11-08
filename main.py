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

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, telefone, email):
        novo_contato = Contato(nome, telefone, email)
        self.contatos.append(novo_contato)
        print("Contato adicionado com sucesso!!!")

    def listar_contatos(self):
        if not self.contatos:
            print("Nenhum contato cadastrado.")
        else:
            for i, contato in enumerate(self.contatos, 1):
                print(f"{i}. {contato}")