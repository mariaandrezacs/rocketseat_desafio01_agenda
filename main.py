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

    def editar_contato(self, indice, nome=None, telefone=None, email=None):
        if 0 <= indice < len(self.contatos):
            contato = self.contatos[indice]
            contato.nome = nome if nome else contato.nome
            contato.telefone = telefone if telefone else contato.telefone
            contato.email = email if email else contato.email
            print("Contato editado com sucesso.")
        else:
            print("Índice inválido.")

    def marcar_favorito(self, indice):
        if 0 <= indice < len(self.contatos):
            self.contatos[indice].favorito = not self.contatos[indice].favorito
            estado = "marcado" if self.contatos[indice].favorito else "desmarcado"
            print(f"Contato {estado} como favorito.")
        else:
            print("Índice inválido.")