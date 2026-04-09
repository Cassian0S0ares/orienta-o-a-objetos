class calculadora:
    def adicionar(self, a,b):
        return a+b
    def tirar(self, a,b):
        return a-b
    def multi(self, a,b):
        return a*b
    def divide(self, a,b):
        if a == 0 or b == 0:
            return "Pode não"
        else:
            return a/b

calc = calculadora()
print(calc.adicionar(10,5))
print(calc.tirar(10,5))
print(calc.multi(10,5))
print(calc.divide(0,5))