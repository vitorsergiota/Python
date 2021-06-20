#2)

def lista(l, n):
    if n in l:
        print(f"pertence ({n}, {l})")
    else:
        print(f"não pertence ({n}, {l})")    

lista( [2,3,7], 3 )
lista( [3,4,6], 1 )