from datetime import datetime
class Paciente:
    def __init__(self, id, n, c, t, nasc):
        self.set_id(id)
        self.set_n(n)
        self.set_c(c)
        self.set_t(t)
        self.set_nasc(nasc)

    def set_id(self, id):
        if id < 0: raise ValueError()
        self.__id = id
    def set_n(self, n):
        if n == "": raise ValueError()
        self.__n = n
    def set_c(self, c):
        if c == "": raise ValueError()
        self.__c = c
    def set_t(self, t):
        if t == "": raise ValueError()
        self.__t = t
    def set_nasc(self, nasc):
        if nasc > datetime.now(): raise ValueError()
        self.__nasc = nasc

    def get_id(self): return self.__id
    def get_n(self): return self.__n
    def get_c(self): return self.__c
    def get_t(self): return self.__t
    def get_nasc(self): return self.__nasc

    def __str__(self):
        return f"{self.__id} - {self.__n} - {self.__c} - {self.__t} - {self.__nasc.strftime("%d/%m/%Y")}"
    
    def idade(self):
        tempo = datetime.now() - self.__nasc # timedelta é contado em dias
        anos = tempo.days // 365
        meses = tempo.days % 365 // 30
        return f"iades: {anos} ano(s) e {meses} mes(es)"

#x = Paciente(1, "Eduardo", "001.002.003-45", "84-90009-1234", datetime(2010, 1, 25))
#rint(x)
#print(x.idade())

class PacienteUI:
    __pacientes =  []
    @staticmethod
    def main():
        op = PacienteUI.menu()
        while op != 7:
            if op == 1: PacienteUI.inserir()
            elif op == 2: PacienteUI.listar()
            elif op == 3: PacienteUI.atualizar()
            elif op == 4: PacienteUI.excluir()
            elif op == 5: PacienteUI.pesquisar()
            elif op == 6: PacienteUI.aniversariante()
    @staticmethod
    def menu():
        x = int(input("Escolha um:"))
        print("1 - Inserir")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("5 - Pesquisar")
        print("6 - Aniversariante")

    @classmethod
    def inserir(cls):
        id = int(input("Informe:"))
        nome = input("Informe:")
        cpf = input("Informe:")
        fone = input("Informe:")
        nascimento = datetime.strptime(input("Informe:"), "%d/%m/%Y")
        x = Paciente(id, nome, cpf, fone, nascimento)
        cls.__pacientes.append(x)

    @classmethod
    def listar(cls):
        for x in cls.__pacientes: print(x, x.idade())
        print(x)

    @classmethod
    def atualizar(cls):
        id = int(input("Informe:"))
        for x in cls.__pacientes:
            if x.get_id() == id:
                x.set_n(input(""))
                x.set_c(input(""))
                x.set_t(input(""))
                x.set_nasc(datetime.strptime(input(""), "%d/%m/%Y"))
                print("Paciente atualizado!")
                return
    print("Não encontrado!")

    @classmethod
    def excluir(cls):
            id = int(input("Informe o Paciente: "))
            for y in cls.__pacientes:
                if y.get_id() == id:
                    cls.__pacientes.remove(y)
                    print("Paciente removido!")
                    return
            print("Não encontrado.")
    
    @classmethod
    def pesquisar(cls):
        id = int(input("Digite:")).lower()
        encotrados = False
        for b in cls.contatos:
          if id in b.get_nome().lower:
                  print(b)
                  encotrados = True
          if not encotrados:
              print("Nada")

    @classmethod
    def aniversariante(cls):
        print()


    





