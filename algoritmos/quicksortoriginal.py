lista=[0,12,3,11,5,9,10,4,15,7]

def dividirmM(lista:list,pmenor:int,pmayor:int):
    pivote=lista[pmenor]
    izq=pmenor +1
    der=pmayor

    while True:

        while izq<=der and lista[izq]<=pivote:
            izq+=1

        while izq<=der and lista[izq]>=pivote:
            der-=1

        if der<izq:
            break
        else:
            lista[izq],lista[der]=lista[der],lista[izq]

    #intercambiar el pivote con el puntero derecho
    lista[pmenor],lista[der]=lista[der],lista[pmenor]

    return der


def quicksort(lista:list,pmenor:int,pmayor:int):
    if pmenor<pmayor:
        pivote=dividirmM(lista,pmenor,pmayor)
        quicksort(lista,pmenor,pivote-1)#parte izquierda
        quicksort(lista,pivote+1,pmayor)#parte 
        
quicksort(lista,0,len(lista)-1)
print(lista)