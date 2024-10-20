class node():
    def __init__(self,value):
        self.value=value #valor
        self.next_pointer=None #puntero siguiente

class queue:
    def __init__(self):
        self.size=0
        self.head=None
        self.end=None

    def __str__(self):
        elements=[]
        current=self.head
        while current:
            elements.append(str(current.value))
            current=current.next_pointer
        return "->".join(elements)

    def enqueue(self,value):
        new_node=node(value) #crear nodo
        self.size+=1

        if self.end is None:
            self.head=new_node #asignar nuevo nodo a head y end
            self.end=new_node  #si esta vacia la cola
        else:
            self.end.next_pointer=new_node #ir al siguiente espacio memoria
            self.end=new_node #colocar nuevo nodo en el siguiente espacio memoria

    def dequeue(self):
        if self.size>0:
            self.size-=1
            deletenode=self.head #guardar frente como auxiliar
            self.head=deletenode.next_pointer #posicionarme en el siguente elemento
            del deletenode #eliminar frente

myqeueue=queue()
myqeueue.enqueue(1)
myqeueue.enqueue(2)
myqeueue.enqueue(3)

print(myqeueue)

myqeueue.dequeue()

print(myqeueue)