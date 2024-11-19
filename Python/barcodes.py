class No:
    def __init__(self, given):
        self.given = given
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.start = None
    
    def add_final(self, item):
        new_no = No(item)
        if self.start = is None:
            self.start = new_no
        else:
            current = self.start
            while current.next:
                current = current.next
            current.next = new_no
    
    def __repr__(self):
        no = self.start
        nos = []
        while no is not None:
            nos.append(str(no.given))
            no = no.next
        return " -> ".join(nos)

list = SingleLinkedList()
barcodes = [1111, 2222, 3333, 4444]

for code in barcodes:
    list.add_final(code)

print(list)
