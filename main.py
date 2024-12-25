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

    def listar_favoritos(self):
        favoritos = [contato for contato in self.contatos if contato.favorito]
        if not favoritos:
            print("Nenhum contato favorito.")
        else:
            for contato in favoritos:
                print(contato)

    def deletar_contato(self, indice):
        if 0 <= indice < len(self.contatos):
            deletado = self.contatos.pop(indice)
            print(f"Contato '{deletado.nome}' deletado com sucesso.")
        else:
            print("Índice inválido.")

def menu():
    agenda = Agenda()

    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Editar contato")
        print("4. Marcar/Desmarcar como favorito")
        print("5. Listar favoritos")
        print("6. Apagar contato")
        print("7. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            email = input("Digite o email: ")
            agenda.adicionar_contato(nome, telefone, email)
        elif opcao == '2':
            agenda.listar_contatos()
        elif opcao == '3':
            indice = int(input("Digite o número do contato para editar: ")) - 1
            nome = input("Novo nome (deixe vazio para manter): ")
            telefone = input("Novo telefone (deixe vazio para manter): ")
            email = input("Novo email (deixe vazio para manter): ")
            agenda.editar_contato(indice, nome, telefone, email)
        elif opcao == '4':
            indice = int(input("Digite o número do contato para marcar/desmarcar como favorito: ")) - 1
            agenda.marcar_favorito(indice)
        elif opcao == '5':
            agenda.listar_favoritos()
        elif opcao == '6':
            indice = int(input("Digite o número do contato para apagar: ")) - 1
            agenda.deletar_contato(indice)
        elif opcao == '7':
            print("Saindo da aplicação. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()


