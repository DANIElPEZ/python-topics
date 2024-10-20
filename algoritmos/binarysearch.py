lista=[1,3,5,7,13,23,34,40,45,69,80,81,82]

def binarysearch(lista:list,number:int):
    pinicial=0
    pfinal=len(lista)-1
    while pinicial <= pfinal:
        pmedio=(pinicial+pfinal)//2

        if number ==lista[pmedio]:
            return True
        elif number > lista[pmedio]:
            pinicial=pmedio+1
        elif number < lista[pmedio]:
            pfinal=pmedio-1
    return False


print(binarysearch(lista,23))