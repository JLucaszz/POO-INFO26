class Contato:
    def __init__(self, id, nome, email, fone):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)

    def set_id(self, id):
        if id < 0: raise ValueError("id deve ser positivo")
        self.__id = id

    def set_nome(self, nome):
        if nome == '': raise ValueError("id deve ser positivo")
        self.__nome = nome

    def set_email(self, email):
        self.__email = email

    def set_fone(self, fone):
        self.__fone = fone

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"




class ContatoUI:
        contatos = [] #atributo de classe - é uma lista de contatos
        @staticmethod
        def main():
            op = 0
            while op != 6:
                op = ContatoUI.menu()
                if op == 1: ContatoUI.inserir()
                elif op == 2: ContatoUI.listar()
                elif op == 3: ContatoUI.atualizar()
                elif op == 4: ContatoUI.excluir()
                elif op == 5: ContatoUI.pesquisar()
        @staticmethod
        def menu():
            print("1 - Inserir, 2 - listar, 3 - Atualizar, 4 - Excluir, 5 - Pesquisar, 6 - Fim")
            return int(input("Escolha:"))
        
        @classmethod
        def inserir(cls):
            id = int(input("Informe o id de contato:"))
            nome = input("Informe o nome:")
            email = input("Informe o email:")
            fone = input("Informe o fone:")
            x = Contato(id, nome, email, fone)
            cls.contatos.append(x)
            print("Contato inserido com sucesso")

        @classmethod
        def listar(cls):
            if len(cls.contatos) == 0: print("Nenhum contato na agenda")
            else:
                for x in cls.contatos: print(x)
        
        @classmethod
        def atualizar(cls):
            id = int(input("Informe o ID do contato: "))
            for c in cls.contatos:
                if c.get_id() == id:
                    c.set_nome(input("Novo nome: "))
                    c.set_email(input("Novo email: "))
                    c.set_fone(input("Novo fone: "))
                    print("Contato atualizado!")
                    return
            print("Contato não encontrado.")

        @classmethod
        def excluir(cls):
            id = int(input("Informe o ID do contato: "))
            for c in cls.contatos:
                if c.get_id() == id:
                    cls.contatos.remove(c)
                    print("Contato removido!")
                    return
            print("Contato não encontrado.")
        
        @classmethod 
        def pesquisar(cls):
          iniciais = int(input("Digite:")).lower()
          encotrados = False
          for c in cls.contatos:
              if iniciais in c.get_nome().lower:
                  print(c)
                  encotrados = True
          if not encotrados:
              print("Nada")
    
ContatoUI.main()