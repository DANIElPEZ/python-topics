class node():
    def __init__(self,value):
        self.value=value #valor
        self.next_pointer=None #puntero siguiente

class stack():
    def __init__(self):
        self.head=None
        self.size=0

    def __str__(self) -> str: #rrecorrer el nodo
        elements=[]
        current=self.head
        while current:
            elements.append(str(current.value))
            current=current.next_pointer
        return "->".join(elements)

    def push(self,value):
        new_node=node(value) #crear nodo
        if self.head: #esta lleno
            new_node.next_pointer=self.head #ir al siguiente espacio memoria
        self.head=new_node #llenar espacio memoria
        self.size+=1

    def pop(self):
        if self.size>0:
            self.size-=1
            deletenode=self.head #guardar cima como auxiliar
            self.head=self.head.next_pointer #pocisionarme en el siguiente elemento
            del deletenode #eliminar nodo

    def stacksize(self):
        return self.size

mystack=stack()
mystack.push(1)
mystack.push(2)
mystack.push(3)

print(mystack)

mystack.pop()

print(mystack)