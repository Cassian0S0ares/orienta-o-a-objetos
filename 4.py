class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor

    def mostrar_saldo(self):
        print(f"Saldo de {self.saldo}")

    def mostrarTitular(self):
        print(f"Correntista: {self.titular}")


conta = ContaBancaria("ana")
conta.depositar(5000)
conta.sacar(1000)
conta.mostrar_saldo()
conta.mostrarTitular()