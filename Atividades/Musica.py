class Playlist:
    def __init__(self, id, nome, descricao):
        self.set_id(id)
        self.set_nome(nome)
        self.set_descricao(descricao)

    def set_id(self, id):
        if id < 0: raise ValueError()
        self.__id = id

    def set_nome(self, nome):
        if nome == '': raise ValueError()
        self.__nome = nome

    def set_descricao(self, descricao):
        if descricao == '': raise ValueError()
        self.__descricao = descricao

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_descricao(self):return self.__descricao

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__descricao}"
    
class PlaylistItem:
    def __init__(self, id, idPlaylist, idMusica, sequencia):
        self.set_id(id)
        self.set_idPlaylist(idPlaylist)
        self.set_idMusica(idMusica)
        self.set_sequencia(sequencia)

    def set_id(self, id):
        if id < 0: raise ValueError()
        self.__id = id

    def set_idPlaylist(self, idPlaylist):
        if idPlaylist < 0: raise ValueError()
        self.__idPlaylist = idPlaylist
    
    def set_idMusica(self, idMusica):
        if idMusica < 0: raise ValueError()
        self.__idMusica = idMusica

    def set_sequencia(self, sequencia):
        if sequencia < 0: raise ValueError()
        self.__sequencia = sequencia

    def get_id(self): return self.__id
    def get_idPlaylist(self): return self.__idPlaylist
    def get_idMusica(self): return self.__idMusica
    def get_sequencia(self): return self.__sequencia

    def __str__(self):
        return f"{self.__id} - {self.__idPlaylist} - {self.__idMusica} - {self.__sequencia}"
    
class Musicas:
    def __init__(self, id, titulo, artista, album):
        self.set_id(id)
        self.set_titulo(titulo)
        self.set_artista(artista)
        self.set_album(album)

    def set_id(self, id):
        if id < 0: raise ValueError()
        self.__id = id

    def set_titulo(self, titulo):
        if titulo == '': raise ValueError()
        self.__titulo = titulo

    def set_artista(self, artista):
        if artista == '': raise ValueError()
        self.__artista = artista

    def set_album(self, album):
        if album == '': raise ValueError()
        self.__album = album

    def get_id(self): return self.__id
    def get_titulo(self): return self.__titulo
    def get_artistas(self): return self.__artista
    def get_album(self): return self.__album

    def __str__(self):
        return f"{self.__id} - {self.__titulo} - {self.__artista} - {self.__album}"


