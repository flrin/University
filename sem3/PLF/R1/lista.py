# 11. a. Determine if a certain element is member in a list.
#     b. Determine the length of a list.


### Mathematical Implementation ###
## a
#f(l1...ln, n) =
# False, l = []
# True, l1 == n
# f(l2...ln, n) otherwise

## b
#f(l) =
# 0, l = []
# 1 + f(l2...ln) otherwise


class Nod:
    def __init__(self, e):
        self.e = e
        self.urm = None
    
class Lista:
    def __init__(self):
        self.prim = None
        

'''
crearea unei liste din valori citite pana la 0
'''
def creareLista():
    lista = Lista()
    lista.prim = creareLista_rec()
    return lista

def creareLista_rec():
    x = int(input("x="))
    if x == 0:
        return None
    else:
        nod = Nod(x)
        nod.urm = creareLista_rec()
        return nod
    
'''
tiparirea elementelor unei liste
'''
def tipar(lista):
    tipar_rec(lista.prim)
    
def tipar_rec(nod):
    if nod != None:
        print (nod.e)
        tipar_rec(nod.urm)
        

'''
program pentru test
'''

'''
a)
'''
def p11a(head , n):
    if head == None:
        return False
    if head.e == n:
        return True
    return p11a(head.urm, n)

'''
b)
'''
def p11b(head):
    if head == None:
        return 0
    return 1 + p11b(head.urm)

def main():
    list = creareLista()
    tipar(list)

    n = int(input("n= "))
    print(p11a(list.prim, n))

    print(p11b(list.prim))

    
main() 
    
    
    
    
    