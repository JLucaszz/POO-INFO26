class Bingo: 
    def __init__(self, numBolas, Bolas):
        self.set_numBolas(numBolas)
        self.set_Bolas(Bolas)
    
    def set_numBolas(self, numBolas):
        if numBolas < 0: raise ValueError()
        self.__numBolas = numBolas
    def set_Bolas(self, Bolas):
        self.__Bolas = Bolas
    
    def get_numBolas(self): return self.__numBolas
    def get_Bolas(self): return self.__Bolas

    def __str__(self):
        return f"{self.__numBolas} - {self.__Bolas}"
    
class BingoUI:
    @staticmethod
    def main():
            op = 0
            while op != 4:
                op = BingoUI.menu()
                if op == 1: BingoUI.iniciarJogo()
                elif op == 2: BingoUI.Sortear()
                elif op == 3: BingoUI.Sorteados()
    @staticmethod
    def main():
        print("1- Iniciar novo jogo, 2- Sortear um numero, 3- Verificar, 4- Sair")
    
    @classmethod
    def iniciarJogo(cls):
        num = int(input("Digite a quantidade de Bolas:"))
        cls.bingo = Bingo(num)
        print("Novo Jogo!")

    @classmethod    
    def Sortear(cls):
        if cls.Bingo is None:
            print("Inicie primeiro")
            return
        num = cls.Bingo.sortear()
        if num == -1:
            print("Todas as bolas foram sorteadas")
        else: 
            print(f"Bola sorteada{num}")
    
    @classmethod
    def Sorteados(cls):
        if cls.bingo is None:
            print("Inicie um jogo primeiro!")
            return
        
        print("Bolas sorteadas:", cls.bingo.sorteados())

BingoUI.main()