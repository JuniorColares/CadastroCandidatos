class Inscricao:
    def __init__(self, nome, endereco, exp, descr):
        self.__nome = nome
        self.__endereco = endereco
        self.__exp = exp
        self.__descr = descr

    @property
    def nome(self):
        return self.__nome

    @property
    def endereco(self):
        return self.__endereco

    @property
    def exp(self):
        return self.__exp

    @property
    def descr(self):
        return self.__descr