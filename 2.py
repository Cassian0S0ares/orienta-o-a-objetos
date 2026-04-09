class pessoa:
    def __init__(self, nome=None, idade=None):
        if nome is None:
            nome = input("Fale o seu nome: ")
        if idade is None:
            idade = int(input("fale sua idade:"))
        self.nome = nome
        self.idade = idade
    def apresentacao(self):
        print(f"Fala guys, blz? Meu nome é {self.nome} e tenho {self.idade} anos")

pessoa1 = pessoa()
pessoa2 = pessoa()
pessoa3 = pessoa()
aluna = pessoa("ana",21)
print("-"*50)
pessoa1.apresentacao()
print("-"*50)
pessoa2.apresentacao()
print("-"*50)
pessoa3.apresentacao()
print("-"*50)
aluna.apresentacao()
print("-"*50)