class Conta:
    def __init__(self, numero, titular, saldo, limite=1000.0):
        print(
            f"Conta com dados:\n Numero: {numero}\n Titular: {titular}\n Saldo: {saldo}\n Limite: {limite}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo de {self.__saldo} na conta do(a) {self.__titular}")

    def sacar(self, valor):
        self.__saldo -= valor

    def depositar(self, valor):
        self.__saldo += valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
