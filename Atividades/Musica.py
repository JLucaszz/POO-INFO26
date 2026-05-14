class playlist:
    def __init__(self, id, nome, descricao):
        self.set_id(id)
        self.set_nome(nome)
        self.set_descricao(descricao)

    def set_id(self, id):
        if id < 0:
            raise ValueError("o id deve ser positivo")
        self.__id = id
    
    def set_nome(self, nome):
        if nome == "":
            raise ValueError("tem que escrever algo")
        self.__nome = nome
    
    def set_descricao(self, descricao):
        if descricao == "":
            raise ValueError("tem que escrever algo")
        self.__descricao = descricao

    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_descricao(self):
        return self.__descricao
    
    def __str__(self):
        return "id: {self.__id} - nome: {self.__nome} - descrição: {self.__descricao}"
    
class musica:
    def __init__(self, id, titulo, artista, album):
        self.set_id(id)
        self.set_titulo(titulo)
        self.set_artista(artista)
        self.set_album(album)
    
    def set_id(self, id):
        if id < 0:
            raise ValueError("tem que ser positivo")
        self.__id = id
    
    def set_titulo(self, titulo):
        if titulo == "":
            raise ValueError("põe o titulo da music caramba")
        self.__titulo = titulo

    def set_artista(self, artista):
        if artista == "":
            raise ValueError("não cale o artista")
        self.__artista = artista

    def set_album(self, album):
        if album == "":
            raise ValueError("cadê o album")
        self.__album = album

    def get_id(self):
        return self.__id
    def get_titulo(self):
        return self.__titulo
    def get_artista(self):
        return self.__artista
    def get_album(self):
        return self.__album
    
    def __str__(self):
        return f"Id = {self.__id} - Titulo = {self.__titulo} - Artista = {self.__artista} - Álbum = {self.__album}"
    
class playlistitem:
    def __init__(self, id, idplaylist, idmusica, sequencia):
        self.set_id(id)
        self.set_idplaylist(idplaylist)
        self.set_idmusica(idmusica)
        self.set_sequencia(sequencia)
    
    def set_id(self, id):
        if id < 0:
            raise ValueError("id deve ser positivo")
        self.__id = id

    def set_idplaylist(self, idplaylist):
        if idplaylist < 0:
            raise ValueError("o id deve ser positivo")
        self.__idplaylist =  idplaylist

    def set_idmusica(self, idmusica):
        if idmusica < 0:
            raise ValueError("o id deve ser positivo")
        self.__idmusica = idmusica

    def set_sequencia(self, sequencia):
        if sequencia < 0:
            raise ValueError("a sequência deve ser positiva")
        self.__sequencia = sequencia

    def get_id(self):
        return self.__id
    def get_idplaylist(self):
        return self.__idplaylist
    def get_idmusica(self):
        return self.__idmusica
    def get_sequencia(self):
        return self.__sequencia
    
    def __str__(self):
        return f"Id = {self.__id} - id da playlist = {self.__idplaylist} - Id da música = {self.__idmusica} - Sequência = {self.__sequencia}"
    
class UI:
    playlists = []
    musicas = []
    itens = []

    @classmethod
    def main(cls):
        op = 0
        while op != 11:
            op = cls.menu()
            if op == 1: cls.inserir_playlist()
            if op == 2: cls.listar_playlists()
            if op == 3: cls.inserir_musica()
            if op == 4: cls.listar_musicas()
            if op == 5: cls.inserir_item_playlist()
            if op == 6: cls.listar_itens_playlist()
            if op == 7: cls.atualizar_playlist()
            if op == 8: cls.excluir_playlist()
            if op == 9: cls.atualizar_musica()
            if op == 10: cls.excluir_musica()

    @staticmethod
    def menu():
        print("1-Inserir Playlist        2-Listar Playlists")
        print("3-Inserir Música          4-Listar Músicas")
        print("5-Adicionar Música na PL  6-Ver Músicas de uma PL")
        print("7-Atualizar Playlist      8-Excluir Playlist")
        print("9-Atualizar Música        10-Excluir Música")
        print("11-Sair")
        return int(input("Escolha uma opção: "))

    @classmethod
    def inserir_playlist(cls):
        id = int(input("ID da Playlist: "))
        nome = input("Nome: ")
        desc = input("Descrição: ")
        cls.playlists.append(playlist(id, nome, desc))

    @classmethod
    def listar_playlists(cls):
        for p in cls.playlists: print(p)

    @classmethod
    def atualizar_playlist(cls):
        id = int(input("ID da playlist para atualizar: "))
        for p in cls.playlists:
            if p.get_id() == id:
                p.set_nome(input("Novo nome: "))
                p.set_descricao(input("Nova descrição: "))

    @classmethod
    def excluir_playlist(cls):
        id = int(input("ID da playlist para excluir: "))
        cls.playlists = [p for p in cls.playlists if p.get_id() != id]
        # Remove também os itens vinculados a essa playlist
        cls.itens = [i for i in cls.itens if i.get_idplaylist() != id]

    # --- Métodos para Música ---
    @classmethod
    def inserir_musica(cls):
        id = int(input("ID da Música: "))
        titulo = input("Título: ")
        artista = input("Artista: ")
        album = input("Álbum: ")
        cls.musicas.append(musica(id, titulo, artista, album))

    @classmethod
    def listar_musicas(cls):
        print("\n--- Músicas Cadastradas ---")
        for m in cls.musicas: print(m)

    @classmethod
    def atualizar_musica(cls):
        id = int(input("ID da música para atualizar: "))
        for m in cls.musicas:
            if m.get_id() == id:
                m.set_titulo(input("Novo título: "))
                m.set_artista(input("Novo artista: "))
                m.set_album(input("Novo álbum: "))

    @classmethod
    def excluir_musica(cls):
        id = int(input("ID da música para excluir: "))
        cls.musicas = [m for m in cls.musicas if m.get_id() != id]
        cls.itens = [i for i in cls.itens if i.get_idmusica() != id]


    @classmethod
    def inserir_item_playlist(cls):
        id = int(input("ID do Vínculo (Item ID): "))
        id_p = int(input("ID da Playlist: "))
        id_m = int(input("ID da Música: "))
        seq = int(input("Sequência (Ordem): "))
        cls.itens.append(playlistitem(id, id_p, id_m, seq))

    @classmethod
    def listar_itens_playlist(cls):
        id_p = int(input("ID da Playlist que deseja visualizar: "))
        print(f"\n--- Músicas da Playlist {id_p} ---")
        for i in cls.itens:
            if i.get_idplaylist() == id_p:
                nome_musica = "Desconhecida"
                for m in cls.musicas:
                    if m.get_id() == i.get_idmusica():
                        nome_musica = m.get_titulo()
                print(f"Posição {i.get_sequencia()}: {nome_musica} (ID Item: {i.get_id()})")

UI.main()