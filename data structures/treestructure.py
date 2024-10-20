class node():
    def __init__(self,value,parent=None):
        self.value=value
        self.right=None
        self.left=None
        self.parent=parent #nodo sepa si tiene nodo padre

class tree():
    def __init__(self):
        self.root=None

    def create_node(self,value:int, parent=None):
        new_node=node(value,parent)
        return new_node

    def insert_node(self,value:int):
        if self.root is None:
            self.root=self.create_node(value)
        else:
            self.insert_in_tree(self.root,value)

    def insert_in_tree(self,current_node,value):
        if value < current_node.value: #value of root
            if current_node.left is None:
                current_node.left=self.create_node(value,current_node)
            else:
                self.insert_in_tree(current_node.left,value)
        
        else:
            if current_node.right is None:
                current_node.right=self.create_node(value,current_node)
            else:
                self.insert_in_tree(current_node.right,value)

    def delete(self,root,value):
        if root is not None:
            # Recur down the tree
            if value < root.value:
                self.delete(root.left,value)
            elif value > root.value:
                self.delete(root.right,value)
            else:
                self.delete_node(root)

    def delete_node(self,node):
        #cuando tiene 2 hijos
        """
        se encuentra el elemento y se va al nodo derecha y luego al mas izquierdo,
        y el nodo original se reemplaza por el mas izquierdo y se elemina el nodo izquierdo,
        porque ya se reemplazo
        """
        if node.left and node.right: #si tiene nodo izquierdo y derecho
            minimum=self.minimum_value_node(node.right)
            node.value=minimum.value #reemplazar el valor 
            self.delete_node(minimum) #eliminar nodo

        #cuando tiene un solo hijo izquierdo o derecho
        elif node.left: #hijo izquierdo
            self.replace_node(node,node.left)
            self.destroy_node(node)

        elif node.right: #hijo derecho
            self.replace_node(node,node.right)
            self.destroy_node(node)

        #cuando es el nodo hoja
        else: #nodo hoja
            self.replace_node(node,None)
            self.destroy_node(node)
    
    def minimum_value_node(self,tree):
        if tree is not None:
            if tree.left: #si tiene hijo izquierdo
                return self.minimum_value_node(tree.left) #buscar la parte mas izquierda posible
            else: #si no tiene mas hijo izquierdo
                return tree #retorna el subarbol
            
    def replace_node(self,node,new_replace_node):
        if node.parent:

            #a tree.root hay que asignar el nuevo hijo
            if node.value == node.parent.left.value:
                node.parent.left=new_replace_node
            elif node.value == node.parent.right.value:
                node.parent.right=new_replace_node

        if new_replace_node:
            # el paso anterior solo el padre apunta al nuevo hijo
            # asignar al hijo su nuevo padre
            new_replace_node.parent=node.parent

    def destroy_node(self,node):
        node.left=None
        node.right=None
        del node

    def dysplaytree(self,tree,cont):
        if tree is not None:

            self.dysplaytree(tree.right,cont+1)
            for _ in range(cont):
                print("   ",end='')

            print(tree.value)
            self.dysplaytree(tree.left,cont+1)

    def findnode(self,tree,target):
        if tree is not None:
            if tree.value == target:
                return True
            elif target<tree.value:
                return self.findnode(tree.left,target)
            else:
                return self.findnode(tree.right,target)
            
    def preorderdysplay(self,tree):
        if tree is not None:
            print(tree.value,end="-")
            self.preorderdysplay(tree.left)
            self.preorderdysplay(tree.right)

    def indorderdysplay(self,tree):
        if tree is not None:
            self.indorderdysplay(tree.left)
            print(tree.value,end='-')
            self.indorderdysplay(tree.right)

    def postorderdysplay(self,tree):
        if tree is not None:
            self.postorderdysplay(tree.left)
            self.postorderdysplay(tree.right)
            print(tree.value,end='-')

mytree=tree()
#insertando nodos
mytree.insert_node(10)
mytree.insert_node(5)
mytree.insert_node(3)
mytree.insert_node(8)
mytree.insert_node(6)
mytree.insert_node(7)
mytree.insert_node(9)
mytree.insert_node(15)
mytree.insert_node(12)
mytree.insert_node(20)
mytree.insert_node(30)
#buscando nodo
result=mytree.findnode(mytree.root,6)
print(result)
#Pre-order Traversal
mytree.preorderdysplay(mytree.root)
print('\n\n')
#In-order Traversal
mytree.indorderdysplay(mytree.root)
print('\n\n')
#In-order Traversal
mytree.postorderdysplay(mytree.root)
print('\n\n\n')
#mostrar arbol
mytree.dysplaytree(mytree.root,0)
print('\n\n\n')
#eliminando nodos
mytree.delete(mytree.root,5)
mytree.dysplaytree(mytree.root,0)
print('\n\n\n')
mytree.delete(mytree.root,20)
mytree.dysplaytree(mytree.root,0)
print('\n\n\n')
mytree.delete(mytree.root,9)
mytree.dysplaytree(mytree.root,0)