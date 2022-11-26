from typing import List, Set, Dict, Tuple

# NGO Andy 21207516
# Activité 9, fréquence dans un texte 



exemple1 : List[str] = ["Je suis belle , o mortels ! comme un reve de pierre , \n",
"Et mon sein , ou chacun s'est meurtri tour a tour , \n",
"Est fait pour inspirer au poete un amour \n",
"Eternel et muet ainsi que la matiere . \n",
" \n",
"Je trone dans l'azur comme un sphinx incompris ; \n",
"J'unis un coeur de neige a la blancheur des cygnes ; \n",
"Je hais le mouvement qui deplace les lignes , \n",
"Et jamais je ne pleure et jamais je ne ris . \n",
" \n",
"Les poetes , devant mes grandes attitudes , \n",
"Que j'ai l'air d'emprunter aux plus fiers monuments , \n",
" Consumeront leurs jours en d'austeres etudes ; \n",
" \n",
"Car j'ai , pour fasciner ces dociles amants , \n",
"De purs miroirs qui font toutes choses plus belles : \n",
"Mes yeux , mes larges yeux aux clartes eternelles !"]

def ouvre_fichier (file : str) -> List[str] :
    """ renvoie la liste des lignes du fichier texte ayant pour chemin path """
    with open(file + ".txt", "r", encoding = "utf-8") as f:
        return f. readlines ()



# Question 1
    
ponctuation : Set[str] = { " ", ",", ";", "'", "(", ")", ".", "!", "?", ":" }

def decompose_ligne (li : str, sep : Set[str]) -> List[str] :
    """
    Decompose une ligne li selon un ensemble de separateurs sep
    """
    q : str = ""
    m : List[str] = []
    i: str
    for i in li :
        q = q + i 
        if i in sep :
            if len(q) > 1 : 
                m.append(q[:-1])
            q = ""
            
    return m  

# Jeu de test 

assert decompose_ligne(exemple1[0],ponctuation) == ['Je', 'suis', 'belle', 'o', 'mortels', 'comme', 'un', 'reve', 'de', 'pierre']
assert decompose_ligne(exemple1[4],ponctuation) == []
assert decompose_ligne(exemple1[8],ponctuation) == ['Et', 'jamais', 'je', 'ne', 'pleure', 'et', 'jamais', 'je', 'ne', 'ris']



# Question 2 

def est_majuscule (caract : str) -> bool :
    """ Détermine si le caractrère est une lettre romaine majuscule"""
    return 65 <= ord (caract) <= 90 

assert est_majuscule("A") 
assert not est_majuscule("z") 

def minusculise_char (c : str) -> str :
    """Décale le caractère c de n lettres si celui-ci est une lettre romaine, ne le décale pas sinon"""
    cdecal : str = c
    ind : int = ord(c) + 32 
    if est_majuscule(c) :
        return chr(ind)        
    return cdecal

assert minusculise_char("C") == "c"
assert minusculise_char("t") == "t"

def minusculise (li : str) -> str :
    """
    Transforme l'ensemble des caracteres de li en son equivalent minuscule
    """
    newstr : str = ""
    c : str
    for c in li :
        newstr = newstr + minusculise_char(c)
    return newstr

# Jeu de test 
    
assert minusculise("bonjour") == "bonjour"
assert minusculise("BONJOUR") == "bonjour"
assert minusculise("Bonjour") == "bonjour"




# Question 3
def mots (lis : List[str], sep : Set[str]) -> List[str] :
    """
    Renvoie, a partir d'une liste lis constitue de lignes de caracteres, une liste de mots separes avec les
    caracteres sep en lettres minuscules
    """
    lit : List[List[str]] = [decompose_ligne(li, sep) for li in lis ]
    listmot : List[str] = []
    i : List[str]
    u : str
    for i in lit : 
        for u in i : 
            listmot.append(u)
    return [minusculise(li) for li in listmot]

# Test 

assert mots(exemple1, ponctuation)[:15] == ['je', 'suis', 'belle', 'o', 'mortels', 'comme', 'un', 'reve', 'de', 'pierre', 'et', 'mon', 'sein', 'ou', 'chacun']



# Question 4

def dictionnaire_occ_mots (texte : List[str]) -> Dict[str , int] :
    """
    Renvoie un dictionnaire d'occurences de mots dans un texte donne
    """
    dic : Dict[str , int] = {} 
    c : str
    for c in texte : 
        if c not in dic : 
            dic[c] = 0 
        dic[c] = dic[c] + 1 
    return dic

dico1 : Dict[str , int] = dictionnaire_occ_mots(mots(exemple1, ponctuation))

# Jeu de test 

assert dico1["je"] == 5
assert dico1["belle"] == 1
assert dico1["jamais"] == 2



# Question 5 

def hapax (dic : Dict[str, int]) -> Dict[str, int] :
    """
    Renvoie la liste constitue des hapax, c'est a dire des mots n'apparaisant qu'une seule
    et unique fois
    """
    l : Dict[str, int] = {}
    cle : str
    val : int
    for (cle, val) in dic.items():
        if val == 1 : 
            l[cle] = val 
    return l 

# Jeu de test 

assert len(hapax(dico1)) == 67
assert not "jamais" in hapax(dico1)
assert "belle" in hapax(dico1)



# Question 6

def plus_frequent(dic : Dict[str, int]) -> str :
    """
    Renvoie le mot le plus frequent dans un texte donne, sachant le dictionnaire
    d'occurences dic ayant l'ordonne la plus faible selon l'ordre du dictionnaire
    """
    u : Iterable[Tuple[str, int]] = dic.items()
    urev : List[Tuple[str, int]] = [("", 0) for i in u]
    num : int = -1
    c : Tuple[str, int]
    for c in u : 
        urev[num] = c
        num = num - 1
    maxi : int = 0
    maxstr : str = ""
    key : str
    val : int
    i : Tuple[str, int]
    for i in urev :
        key, val = i 
        if val > maxi :
            maxi = val
            maxstr = key
    return maxstr

# Test 

assert plus_frequent(dico1) == "je"



# Suggestion 4 : Attaque de Cesar 

lettres_francais : Dict[str , float ] = { "e" : 0.1210 ,
"a" : 0.0711 ,
"i" : 0.0659 ,
"s" : 0.0651 ,
"n" : 0.0639 ,
"r" : 0.0607 ,
"t" : 0.0592 ,
"o" : 0.0502 ,
"l" : 0.0496 ,
"u" : 0.0449 ,
"d" : 0.0367 ,
"c" : 0.0318 ,
"m" : 0.0262 ,
"p" : 0.0249 ,
"g" : 0.0123 ,
"b" : 0.0114 ,
"v" : 0.0111 ,
"h" : 0.0111 ,
"f" : 0.0111 ,
"q" : 0.0065 ,
"y" : 0.0046 ,
"x" : 0.0038 ,
"j" : 0.0034 ,
"k" : 0.0029 ,
"w" : 0.0017 ,
"z" : 0.0015}


def est_minuscule (caract : str) -> bool :
    """
    Détermine si le caractère est une lettre romaine minuscule
    """
    return 97 <= ord (caract) <= 122


def caractere_decale (c : str, n : int) -> str :
    """
    Décale le caractère c de n lettres si celui-ci est une lettre romaine, ne le décale pas sinon
    """
    cdecal : str = c
    ind : int = ord(c) + n
    
    if est_majuscule(c) :
        
        if ind > 90 :
            cdecal = chr((ind % 90) + 64)
            
        else : 
            cdecal = chr(ord(c) + n)
            
        return cdecal
    
    elif est_minuscule(c) :
        
        if ind > 122 :
            cdecal = chr((ind % 122) + 96)
            
        else :
            cdecal = chr(ord(c) + n)
            
        return cdecal
    
    else :
        return cdecal


def ligne_dechiffre_cesar (c: str, n : int) -> str :
    """
    Decrypte la chaîne de caractère c avec un décalage de n
    """
    ligne_decrypt : str = ""
    i : str
    
    for i in c :
        ligne_decrypt = ligne_decrypt + caractere_decale(i, 26 - n)
        
    return ligne_decrypt


def text_frequency (filepath : str, language_frequency : Dict[str, float], punctuation : Set[str], n : int) -> Dict[str, float] :
    """
    Calcule la frequence de chaque lettre dans un texte ayant pour chemin d'acces filepath avec un decalage de n, sachant que chaque lettre du language
    est une cle dans language_frequency et que le texte est separe selon les caracteres contenu dans punctuation
    """
    text : List[str] = ouvre_fichier(filepath)
    transformed_txt : List[str] = [ligne_dechiffre_cesar(line, n) for line in text]
    language_amount : Dict[str, float] = {}
    key_0 : str
    
    for key_0 in language_frequency.keys() : 
        language_amount[key_0] = 0
        
    line : str
    for line in transformed_txt:
        letter : str
        for letter in line : 
            if letter in language_frequency : 
                language_amount[letter] = language_amount[letter] + 1
                
    liste_mots : List[str] = mots(transformed_txt, punctuation)
    txt_length : int = 0
    mot : str
    p : str

    for mot in liste_mots : 
        for p in mot :
            txt_length = txt_length + 1
            
    dictfreq : Dict[str , float ] = {}
    key : str
    
    for key in language_frequency.keys() : 
        dictfreq[key] = language_amount[key] / txt_length
    
    return dictfreq 


def diff_dict (freq_txt : Dict[str , float], language_frequency : Dict[str, float]) -> float :
    """
    Renvoie la difference entre un dictionnaire de frequence d'un texte donne, et le dictionnaire de reference du language du texte
    """
    p : float = 0
    i : str
    
    for i in freq_txt :
        difference : float = (float(freq_txt[i]) - float(language_frequency[i]))
        p = p + abs(difference)
    
    return p 


def dechiffre_fichier_cesar (nom : str, n : int) -> None :
    """
    Precondition : <nom>.txt est un fichier existant
    recopie le contenu du fichier <nom>.txt dans <nom>-copie.txt
    Decrypte le fichier nom.txt et enregistre le texte decrypté dans nom-decrypt.txt 
    """
    with open(nom + "-cesar.txt", "r") as source :
        with open(nom + "-decrypt.txt", "w") as destination :
            ligne : str
            for ligne in source.readlines() :
                destination.write(ligne_dechiffre_cesar(ligne, n))

                
def decode_cesar_auto (filepath : str, language_frequency : Dict[str, float], punctuation : Set[str] ) -> None :
    """
    Cree un fichier qui est le resultat du decodage automatique du chiffrement de cesar
    """ 
    score : float = diff_dict(text_frequency(filepath + "-cesar", language_frequency, punctuation, 0), language_frequency)
    current_score : float = 0
    rotation : int = 0
    i : int
    
    for i in range (1, 26) : 
        current_score = diff_dict(text_frequency(filepath + "-cesar", language_frequency, punctuation, i), language_frequency)
        if current_score < score : 
            score = current_score
            rotation = i
    dechiffre_fichier_cesar(filepath, rotation)



# Jeu de test 
# Pour tester si la fonction marche, un test intéressant serait d'éxécuter la ligne ci-dessous
# en ayant téléchargé le document texte beaute-cesar.txt dans le dossier
# decode_cesar_auto("beaute", lettres_francais, ponctuation)
