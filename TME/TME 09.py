from typing import Dict, Set, List

# Andy NGO 21207516

# Exercice 9.5 


# Question 1 

basprix : Dict[str, float] = {"Sabre laser" : 229.0,"Mitendo DX" : 127.30,"Coussin Linux" : 74.50,"Slip Goldorak" : 29.90,"Station Nextpresso" : 184.60}


# Question 2 

def prix_moyen (base_prix : Dict[str, float]) -> float : 
    """
    Determine le prix moyen des articles d'une base de prix
    """
    price : float
    somme : float = 0
    for _, price in base_prix.items() :
        somme = somme + price
    return somme / len(base_prix) 

# Jeu de test 

assert prix_moyen(basprix) == 129.06


# Question 3

def fourchette_prix (mini : float, maxi : float, base_prix : Dict[str, float]) -> Set[str] : 
    """
    Precondition : 0 < mini < maxi
    Renvoie l'ensemble des articles dont le prix est compris entre mini et maxi 
    """
    product : str
    price : float
    result : Set[str] = set()
    for product, price in base_prix.items() :
         if mini <= price <= maxi :
             result.add(product)
    return result

def fourchette_prix_com (mini : float, maxi : float, base_prix : Dict[str, float]) -> Set[str] :
    """
    Precondition : 0 < mini < maxi
    Renvoie les produits dont le prix est compris entre mini et maxi en compréhension
    """
    return {product for product in base_prix if mini < base_prix[product] < maxi}

# Jeu de test 

assert fourchette_prix(50, 200, basprix) == {'Coussin Linux', 'Mitendo DX', 'Station Nextpresso'}
assert fourchette_prix_com(50, 200, basprix) == {'Coussin Linux', 'Mitendo DX', 'Station Nextpresso'}


# Question 4

achat : Dict[str, int] = {"Sabre laser" : 3, "Coussin Linux" : 2, "Slip Goldorak" : 1}


# Question 5 

def tous_disponible (achat : Dict[str, int], base_prix : Dict[str, float]) -> bool : 
    """
    Renvoie si l'ensemble des produits dans le panier est disponible dans la base des prix
    """
    item : str 
    for item in achat : 
        if item not in base_prix : 
            return False 
    return True 

# Jeu de test

assert tous_disponible(achat, basprix) == True 


# Qusetion 6

def prix_achat (achat : Dict[str, int], base_prix : Dict[str, float]) -> float : 
    """
    Renvoie le prix total d'un panier d'achat à partir d'un panier et d'une base de prix
    """
    item : str
    amount : int
    price : float = 0 
    for item, amount in achat.items() :
        price = price + base_prix[item] * amount
    return price

# Jeu de test 

assert prix_achat(achat, basprix) == 865.9


# Exercice 10.3 ; question 2


def fourchette_prix_com_1 (mini : float, maxi : float, base_prix : Dict[str, float]) -> Set[str] :
    """
    Precondition : 0 < mini < maxi
    Renvoie les produits dont le prix est compris entre mini et maxi en compréhension
    """
    return {product for product in base_prix if mini < base_prix[product] < maxi}

# Jeu de test

assert fourchette_prix_com_1(50, 200, basprix) == fourchette_prix(50, 200, basprix)


# Exercice 10.4


# Question 1


def melements_list (l : List[T]) -> Set[T] :
    """
    Retourne l'ensemble des elements presents au moins une fois dans la liste l dans un ensemble 
    """
    return {i for i in l}

def melements_dict (d : Dict[T, U]) -> Set[T] :
    """
    Retourne l'ensemble des elements presents au moins une fois dans le dictionnaire d
    """
    return {i for i, q in d.items()}

# Jeu de test 

assert melements_list(['a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c']) == {'a', 'b', 'c'}
assert melements_list(['a', 'b', 'c', 'c', 'a', 'b', 'c', 'b', 'b' ]) == {'a', 'b', 'c'}
assert melements_list([]) == set()

assert melements_dict({'a':2, 'b':4, 'c':3}) == {'a', 'b', 'c'}
assert melements_dict({'b':2, 'c':4, 'a':3}) == {'a', 'b', 'c'}
assert melements_dict({}) == set()


# Question 2


def mdict_de_mlist(l : List[T]) -> Dict[T, int] : 
    """
    Renvoie le multi-ensemble sous forme de liste converti sous forme de dictionnaire
    """
    d : Dict[T, int] = {u: 0 for u in melements_list(l)}
    i : T
    for i in l : 
        d[i] = d[i] + 1
    return d

# Jeu de test 

assert mdict_de_mlist(['a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c']) == {'b': 4, 'c': 3, 'a': 2}
assert mdict_de_mlist(['a', 'b', 'c', 'c', 'a', 'b', 'c', 'b', 'b' ]) == {'b': 4, 'c': 3, 'a': 2}
assert mdict_de_mlist([]) == {}

# On ne peut effectuer de liste en comprehension, en effet il serait necessaire d'une facon ou d'une autre 
# d'acceder a la valeur correspondant a la cle donnee alors qu'elle est en train d'etre cree, ce qui ne semble pas possible 


# Question 3 


def mlist_de_mdict (d : Dict[T, int]) -> List[T] : 
    """
    Renvoie le multi-ensemble sous forme de dictionnaire converti sous forme de liste
    """
    result : List[T] = []
    for i, k in d.items():
        p : int  
        for p in range(k): 
            result.append(i)
    return result

# Jeu de test 

assert mdict_de_mlist(mlist_de_mdict({'b': 4, 'c': 3, 'a': 2})) == {'b': 4, 'c': 3, 'a': 2}
assert mdict_de_mlist(mlist_de_mdict({})) == {}

# Fonction mlist_de_mdict() définie sous forme de liste en compréhension
def mlist_de_mdict_com (d : Dict[T, int]) -> List[T] :
    """
    Renvoie le multi-ensemble sous forme de dictionnaire converti sous forme de liste, en employant la comprehension de liste
    """
    return [key for key, value in d.items() for p in range(value)]

# Jeu de test

assert mdict_de_mlist(mlist_de_mdict_com({'b': 4, 'c': 3, 'a': 2})) == {'b': 4, 'c': 3, 'a': 2}


# Question 4


def minter_dict (d1 : Dict[T, int], d2 : Dict[T, int]) -> Dict[T, int] :
    """
    Renvoie un dictionnaire constitue de l'intesection des dictionnaires d1 et d2
    """ 
    return {q : min(d1[q], d2[q]) for q in d1 if q in d2}

# Jeu de test 

assert minter_dict({'a':2, 'b':4, 'c':3},{'f':1, 'a':1, 'b':3}) == {'b': 3, 'a': 1}
assert minter_dict(dict(), {'f':1, 'a':1, 'b':3}) ==  {}
assert minter_dict({'a':2, 'b':4, 'c':3}, dict()) == {}


# Question 5


def minter_list (l1 : List[T], l2 : List[T]) -> List[T] :
    """
    Renvoie une liste constitue de l'intesection des listes l1 et l2
    """
    return mlist_de_mdict_com(minter_dict(mdict_de_mlist(l1), mdict_de_mlist(l2)))

# Jeu de test 

assert mdict_de_mlist(minter_list(['a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c'],['f', 'a', 'b', 'b', 'b'])) == {'a': 1, 'b' : 3}


# Question 6

def munion_list ( l1 : List[T], l2 : List[T]) -> List[T] :
    """
    Renvoie l'union des deux listes l1 et l2 en utilisant la representation multi-ensembliste
    """
    d1 : Dict[T, int] = mdict_de_mlist(l1)
    d2 : Dict[T, int] = mdict_de_mlist(l2)
    d_fin : Dict[T, int] = {}
    for key, value in d1.items() :
        d_fin[key] = value
    for key, value in d2.items() : 
        if key in d_fin : 
            d_fin[key] = d_fin[key] + value
        else : 
            d_fin[key] = value
    return mlist_de_mdict(d_fin)

def munion_dict(d1 : Dict[T, int], d2 : Dict[T, int]) -> Dict[T, int]:
    """
    Renvoie l'union des deux listes l1 et l2 en utilisant la representation à base d'ensemble
    """
    d : Dict[T, int] = d1
    k : T
    l : T
    for k in d:
        if k in d2:
            d[k] = d[k] + d2[k]
    for l in d2:
        if l not in d:
            d[l] = d2[l]
    return d

# On ne peut pas implémenter munion_dict par compréhension car il faudrait concatener 2 dictionnaires c1 et c2 pour ensuite parcourir "d1 + d2",
# or certains couple clés/valeurs ayant la même clé, elle sera effacée.

# Jeu de test 

assert munion_dict({'a':2, 'b':4, 'c':3},{'f':1, 'a':1, 'b':3}) == {'a':3, 'b': 7, 'c':3, 'f':1}
assert munion_dict({},{'f':1, 'a':1, 'b':3}) == {'f':1, 'a':1, 'b':3}
assert munion_dict({'a':2, 'b':4, 'c':3}, {}) == {'a':2, 'b':4, 'c':3}
assert mdict_de_mlist(munion_list(['a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c'],['f', 'a', 'b', 'b', 'b'])) == {'a' : 3, 'b' : 7, 'c' : 3, 'f' : 1}
