class Conta:
    def __init__(self, numero, titular, saldo, limite=1000.0):
        print(f"Criando Conta do {titular}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo de {self.__saldo} na conta do(a) {self.__titular}")

    def sacar(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f"Você não pode sacar {valor}")

    def depositar(self, valor):
        self.__saldo += valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    # Getters e Getters como Propriedades (Saldo, Titular e Limite)

    # def get_saldo(self):
    #     return self.__saldo
    @property
    def saldo(self):
        return self.__saldo

    # def get_titular(self):
    #     return self.__titular
    @property
    def titular(self):
        print("chamando @property")
        return self.__titular

    # def get_limite(self):
    #     return self.__limite
    @property
    def limite(self):
        return self.__limite

    # Setters e Setters Como Propriedades(Limite, Saldo (Set do Saldo em Sacar, Depositar e Transferir))

    # def set_limite(self, limite):
    #     self.__limite = limite
    @limite.setter
    def limite(self, limite):
        print("chamando @'atributo'.setter")
        self.__limite = limite

    # Métodos Auxiliares
    # Métodos Privados são similares a atributos privados, basta adicionar __ na frente do nome do método
    def __pode_sacar(self, valor_saque):
        valor_disponível_para_saque = self.__saldo + self.__limite
        print(f"Valor Disponível para saque : {valor_disponível_para_saque}")
        return valor_saque <= valor_disponível_para_saque  # True se puder Sacar
