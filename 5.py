class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Deposito de R$ {valor} efetuado")
        else:
            print("Valor invalido para o deposito")
    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"Saque de R$ {valor} efetuado")
            else:
                print("Saldo insuficiente para o saque")
        else:
            print("Valor incorreto")
    def mostrar_saldo(self):
        status = "Devendo ao banco" if self.saldo < 0 else "Em dia"
        print(f"Saldo R$ {self.saldo} - {status}")
    def get_titular(self):
        return self.titular

class Banco:
    def __init__(self):
        self.correntistas = []
    def abrir_conta(self):
        nome = input("Digite o nome do titular: ")
        conta = ContaBancaria(nome)
        self.correntistas.append(conta)
        print("Conta aberta com sucesso!!!")
    def encontrar_conta(self, nome):
        for conta in self.correntistas:
            if conta.get_titular() == nome:
                return conta
        return None
    def depositar_fundos(self):
        nome = input("Digite o nome da conta ;) : ")
        conta = self.encontrar_conta(nome)
        if conta:
            try:
                valor = float(input("Digite o deposito: "))
                conta.depositar(valor)
            except ValueError:
                print("Entrada invalida")
        else:
            print("Correntista não encontrado :(")
    def sacar_fundos(self):
        nome = input("Digite o nome do titular: ")
        conta = self.encontrar_conta(nome)
        if conta:
            try:
                valor = float(input("Digite o valor de saque: "))
                conta.sacar(valor)
            except ValueError:
                print("Entrada inválida")
        else:
            print("Correntista não encontrado")
    def mostrar_saldo_correntista(self):
        nome = input("Digite o nome do titular: ")
        conta = self.encontrar_conta(nome)
        if conta:
            conta.mostrar_saldo()
        else:
            print("Correntista nao encontrado.")
    def listar_contas(self):
        if not self.correntistas:
            print("Nenhuma conta cadastrada")
            return
        print("Lista de correntistas:")
        for conta in self.correntistas:
            print(conta.get_titular(), "Saldo de R$", conta.mostrar_saldo())
            print("-"*50)

def main():
    banco = Banco()
    while True:
        print("\n ----- Menu Bancário -----")
        print("1. Abrir conta")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Mostrar Saldo")
        print("5. Mostrar correntistas")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            banco.abrir_conta()
        elif opcao == '2':
            banco.depositar_fundos()
        elif opcao == '3':
            banco.sacar_fundos()
        elif opcao == "4":
            banco.mostrar_saldo_correntista()
        elif opcao == "5":
            banco.listar_contas()
        elif opcao == "6":
            break
        else:
            print("Opção invalida")
main()