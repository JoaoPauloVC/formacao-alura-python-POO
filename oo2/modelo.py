class Programa:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0
    
    @property
    def likes(self):
        return self.__likes
    
    def dar_like(self):
        self.__likes += 1
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
        
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


vingadores = Filme("vingadores - guerra infinita", 2018, 160)
vingadores.dar_like()
print(f"Filme: {vingadores.nome}; Ano: {vingadores.ano}; Duração: {vingadores.duracao}; Likes: {vingadores.likes}")


arrow = Serie("arrow", 2015, 2)
arrow.dar_like()
arrow.dar_like()
print(f"Série: {arrow.nome}; Ano: {arrow.ano}; Temporadas: {arrow.temporadas}; Likes: {arrow.likes}")
