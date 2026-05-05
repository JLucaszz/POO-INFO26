class Jogadores:
    def __init__(self, id, nome, idTime, camisa):
        self.set_id(id)
        self.set_idTime(idTime)
        self.set_nome(nome)
        self.set_camisa(camisa)

    def set_id(self, id):
        if id < 0: raise ValueError("id deve ser positivo")
        self.__id = id

    def set_nome(self, nome):
        if nome == '': raise ValueError("id deve ser positivo")
        self.__nome = nome

    def set_idTime(self, idTime):
        if id < 0: raise ValueError("id deve ser positivo")
        self.__idTime = idTime

    def set_camisa(self, camisa):
        if id < 0: raise ValueError("id deve ser positivo")
        self.__camisa = camisa

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__idTime
    def get_fone(self): return self.__camisa
    
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__idTime} - {self.__camisa}"

class Bingo: 
    def __init__(self, numBolas, Bolas):
        self.set_numBolas(numBolas)
        self.set_Bolas(Bolas)
    
    def set_numBolas(self, numBolas):
        if numBolas < 0: raise ValueError()
        self.__numBolas = numBolas
    def set_Bolas(self, nome):
        if nome == '': 
        self.__nome
    
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_estado(self): return self.__estado

    def __str__(self):
        return f"{self.__id} - {self._nome} - {self.__estado}"
    
class UI:
        @staticmethod
        def main():
            op = 0
            while op != 11:
                op = UI.menu()
                if op == 1: UI.inserir_t()
                elif op == 2: UI.listar_t()
                elif op == 3: UI.atualizar_t()
                elif op == 4: UI.excluir_times()
                elif op == 5: UI.inserir_j()
                elif op == 6: UI.listar_j()
                elif op == 7: UI.atualizar_j()
                elif op == 8: UI.excluir_j()
                elif op == 9: UI.listar_jogadores_do_time()
                elif op == 10: UI.transferir_jogador
        @staticmethod
        def menu():
            print("\n1 - Inserir t")
            print("2 - Listar t")
            print("3 - Atualizar t")
            print("4 - Excluir t")
            print("5 - Inserir j")
            print("6 - Listar j")
            print("7 - Atualizar j")
            print("8 - Excluir j")
            print("9 - Inserir t")
            print("10 - Listar Jogadores do t")
            print("11- Transeferir Jogador")
           
            return int(input("Escolha uma opção: "))
    
        @classmethod
        def inserir_j(cls):
            id = int(input("Informe o id de contato:"))
            nome = input("Informe o nome:")
            idTime = input("Informe o idTime:")
            camisa = input("Informe a camisa:")
            x = Jogadores(id, nome, idTime, camisa)
            cls.contatos.append(x)
            print("Jogador Inserido com sucesso!")
        
        @classmethod
        def listar_j(cls):
                if len(cls.Jogadores) == 0: print("Nenhum jogador encontrado")
                else:
                    for x in cls.Jogadores: print(x)
        
        @classmethod
        def atualizar_j(cls):
            id = int(input("Informe o Jogador: "))
            for c in cls.jogadoes:
                if c.get_id() == id:
                    c.set_nome(input("Novo nome: "))
                    c.set_idTime(input("Novo idTime: "))
                    c.set_camisa(input("Novo camisa: "))
                    print("Jogador atualizado!")
                    return
            print("Jogador não encontrado.")

        @classmethod
        def excluir_j(cls):
            id = int(input("Informe o jogador: "))
            for c in cls.jogadores:
                if c.get_id() == id:
                    cls.jogadores.remove(c)
                    print("Jogador removido!")
                    return
            print("Jogador não encontrado.")

        

        

      
    
UI.main()