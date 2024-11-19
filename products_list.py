class Product:
    def __init__(self, Code = "indefinido", Type = 0):
        self.Code = Code
        self.Type = Type

    def __repr__(self):
        return "%s - %d" % (self.Code, self.Type)

class Nodo:
    def __init__(self, given=None, next_nodo=None):
        self.content = given
        self.next = next_nodo

    def __repr__(self):
        return "%s -> %s" % (self.content, self.next)

class LinkedList:
    def __init__(self):
        self.start = None

    def __repr__(self):
        return "[" + str(self.start) + "]"

    def EmptyList(self):
        return self.start is None

    def PrintList(self):
        current = self.start
        cont = 0
        print("Início da Lista")
        if self.start is None:
            print("Lista Vazia")
        else:
            while current:
                print("Posição:", cont, current)
                cont += 1
                current = current.next
        print("Final da Lista")

    def TotalRefrigeratedProduct(self):
        current = self.start
        total = 0
        while current:
            if current.content.Type == 1:
                total += 1
            current = current.next
        return total

    def NovoProduct(self, Nd):
        Nd.next = self.start
        self.start = Nd

lista = LinkedList()

lista.NovoProduct(Nodo(Product("001", 1)))
lista.NovoProduct(Nodo(Product("002", 0)))
lista.NovoProduct(Nodo(Product("003", 0)))
lista.NovoProduct(Nodo(Product("004", 1)))
lista.NovoProduct(Nodo(Product("005", 0)))

lista.PrintList()

print("Total de Produtos com Refrigeração:", lista.TotalRefrigeratedProduct())
