import random
import string

class TreapNode:
    def __init__(self, key):
        self.key = key
        self.priority = random.randint(0,99)
        self.left = None
        self.right = None

def rightRotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    return x

def leftRotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    return y

def insert(root, key):
    if not root:
        return TreapNode(key)
    
    if key <= root.key:
        root.left = insert(root.left, key)

        if root.left.priority < root.priority:
            root = rightRotate(root)
    
    else:
        root.right = insert(root.right, key)

        if root.right.priority < root.priority:
            root = leftRotate(root)
    
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print("key:", root.key, "| priority:", root.priority, end="")
        if root.left:
            print(" | left child:", root.left.key, end="")
        if root.right:
            print(" | right child:", root.right.key, end="")
        print()
        inorder(root.right)


if __name__ == '__main__':
 
    root = None
    root = insert(root, 50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)

    inorder(root)

    root = insert(root, 90)

    print("Print after insert 90\n")
    inorder(root)



# def check_bst_property(node, min_key, max_key):
#     if not node:
#         return True
#     if not (min_key <= node.key <= max_key):
#         return False
#     return (check_bst_property(node.left, min_key, node.key - 1) and
#             check_bst_property(node.right, node.key + 1, max_key))

# def check_heap_property(node):
#     if not node:
#         return True
#     if node.left and node.left.priority < node.priority:
#         return False
#     if node.right and node.right.priority < node.priority:
#         return False
#     return check_heap_property(node.left) and check_heap_property(node.right)

# # Funzione di test su 100 casi casuali
# def test_100_random_cases():
#     num_cases = 100
#     max_elements = 20  # Numero massimo di elementi in ogni caso

#     for i in range(1, num_cases + 1):
#         # Genera una lista di chiavi casuali per il caso di test
#         num_elements = random.randint(5, max_elements)
#         case = random.sample(range(1, 1000), num_elements)

#         print(f"\nTest Case {i}: Inserimento {case}")
#         root = None
#         for key in case:
#             root = insert(root, key)
        
#         # Verifica delle proprietà del Treap
#         is_bst = check_bst_property(root, float('-inf'), float('inf'))
#         is_heap = check_heap_property(root)
        
#         print("Proprietà BST rispettata:", is_bst)
#         print("Proprietà Heap rispettata:", is_heap)
        
#         # Stampa il risultato solo se entrambe le proprietà sono rispettate
#         if is_bst and is_heap:
#             print("Inorder traversal per il Treap risultante:")
#             inorder(root)
#         else:
#             print("Errore: il Treap non soddisfa le proprietà richieste.")
        
#         print("\n" + "-"*50)

# # Esegui i test
# test_100_random_cases()