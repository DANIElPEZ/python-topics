import re

#definir expresion
exp=r'a'
txt='aircraft'
#encuentra al inicio de la cadena
asw=re.match(exp,txt)
print(asw)

#encuentra * 0 o mas coincidencias
exp=r'a*'
#encuentra todas las coincidencias
asw=re.findall(exp,txt)
print(asw)

#encuentra 1 o mas
exp=r'a+'
asw=re.findall(exp,txt)
print(asw)

#encontrar una o la otra
exp=r'(e|E)'
txt='DevelopEr'
asw=re.findall(exp,txt)
print(asw)

#encuentra en donde inicia en e y termina E
exp=r'((e|E)+)(.)*'
txt='DevelopEr'
#encontrar si hay coincidencia de la expresion
asw=re.search(exp,txt)
print(asw)

#encuentra eceptuando lo del medio con y debe tener rango minimo y maximo
txt='aaaaaaAAA aandresss AAAAaa'
exp=r'((a|A)+) (.{5,11}) ((a|A)+)'
asw=re.search(exp,txt)
print(asw)

#encuentra y el medio debe llevar letras y numeros
txt='aaaaaaAAA ernesto 7893428793289734 AAAAaa'
exp=r'((a|A)+) [a-z].*[0-9].* ((a|A)+)'
asw=re.search(exp,txt)
print(asw)

#ejemplo con url
txt='https://danidev.reflex.run'
exp=r'^(https:?//(www\.)?|www\.)\w{5,18}\.[a-z]{3,8}\.[a-z]{2,4}$' #? indica si existe la letra anterior (s)
asw=re.search(exp,txt)
print(asw)