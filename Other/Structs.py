class Queue():

    # Constructor
    def __init__(self):
        self.items = []

    # Revisa si la queue esta vacia
    def isEmpty(self):
        return self.items == []

    # Agrega un elemento a la queue
    def enqueue(self, item):
        self.items.insert(0,item)

    # Saca un elemento de la queue
    def dequeue(self):
        return self.items.pop()

    # Regresa el tamano(numero de elementos) de la queue
    def size(self):
        return len(self.items)
        
    # Regresa todos los elementos en la queue
    def getElements(self):
        return self.items

    # Regresa el primer elemento de la queue sin sacarlo
    def peek(self):
        return self.items[len(self.items)-1]


class Stack():

    # Constructor
    def __init__(self):
        self.items = []

    # Revisa si el stack esta vacio
    def isEmpty(self):
        return self.items == []

    # Agrega un elemento al stack
    def push(self, item):
        return self.items.append(item)

    def pushToDict(self, key, val):
        self.items[len(self.items)-1][key] = val

    # Saca un elemento del stack
    def pop(self):
        return self.items.pop()

    # Sirve para ver el elemento superior del stack sin removerlo
    def peek(self):
        return self.items[len(self.items)-1]

    def peekSecond(self):
        return self.items[len(self.items)-2]

    def peekFromDict(self, key):
        return self.items[len(self.items)-1][key]

    def peekSecondFromDict(self, key):
        return self.items[len(self.items)-2][key]

    # Despliega todos los elementos del stack
    def getElements(self):
        return self.items

    # Regresa el tamano ( numero de elementos) del stack
    def size(self):
        return len(self.items)

    def printStack(self):
        l = len(self.items) -1
        print self.size()
        while l != 0:
            print self.items[l]
            l -= 1
        