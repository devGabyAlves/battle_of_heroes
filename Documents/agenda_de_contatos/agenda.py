class Contato: 
    def __init__(self, nome, telefone, email, favorito=False):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.favorito = favorito

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contatos(self, contato):
        self.adicionar_contatos(contato)
    
    def visualizar_contatos(self):
        for contato in self.contatos:
            print(f"Nome: {contato.nome}, Telefone: {contato.telefone}, Email: {contato.email}, Favorito: {contato.favorito}")
    
    def editar_contato(self, nome_antigo, novo_contato):
        for contato in self.contatos:
            if contato.nome == nome_antigo:
                contato.nome = novo_contato.nome
                contato.telefone = novo_contato.telefone
                contato.email = novo_contato.email
                contato.favorito = novo_contato.favorito
                print("Contato editado com sucesso.")
                return
        print("Contato nao encontrado")
    
    def marcar_favorito(self, nome_contato):
        for contato in self.contatos:
            if contato.nome == nome_contato:
                contato.favorito = not contato.favorito
                print("Status de favorito atualizado.")
                return
        print("Contato náo encontrado.")

    def contatos_favoritos(self):
        favoritos = [contato for contato in self.contatos if contato.favorito]
        if favoritos:
            for contato in favoritos:
                print(f"Nome: {contato.nome}, Telefone: {contato.telefone}, Email: {contato.email}")
        else:
            print("Nenhum contato favorito encontrado.")
    
    def apagar_contato(self, nome_contato):
        for contato in self.contatos:
            if contato.nome == nome_contato:
                self.contatos.remove(contato)
                print("Contato apagado com sucesso.")
                return
        print("Contato nao encontrado.")

def main():
    agenda = Agenda()

    while True:
        print("\n1. Adicionar Contato")
        print("2. Visualizar Contatos")
        print("3. Editar Contato")
        print("4. Marcar/Desmarcar Favorito")
        print("5. Contatos Favoritos")
        print("6. Apagar Contato")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            favorito = input("É favorito? (S/N): ").upper() == "S"
            novo_contato = Contato(nome, telefone, email, favorito)
            agenda.adicionar_contato(novo_contato)

        elif escolha == "2":
            agenda.visualizar_contatos()

        elif escolha == "3":
            nome_antigo = input("Digite o nome do contato que deseja editar: ")
            novo_nome = input("Novo Nome: ")
            novo_telefone = input("Novo Telefone: ")
            novo_email = input("Novo Email: ")
            novo_favorito = input("É favorito? (S/N): ").upper() == "S"
            novo_contato = Contato(novo_nome, novo_telefone, novo_email, novo_favorito)
            agenda.editar_contato(nome_antigo, novo_contato)

        elif escolha == "4":
            nome_contato = input("Digite o nome do contato: ")
            agenda.marcar_favorito(nome_contato)

        elif escolha == "5":
            agenda.contatos_favoritos()

        elif escolha == "6":
            nome_contato = input("Digite o nome do contato que deseja apagar: ")
            agenda.apagar_contato(nome_contato)

        elif escolha == "0":
            print("Saindo do programa. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "_main_":
    main()
