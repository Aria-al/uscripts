from typing import List, Optional, Tuple
import random 
CaseT = str
PlateauT = List[List[CaseT]]


def plateau_vide () -> PlateauT :
    return [[" ", " ", " "] for i in range (3)]

# table : str = '/---\\\n|',pla[0][0], pla[0][1], pla[0][2] ,'|\n|',pla[1][0], pla[1][1], pla[1][2],'|\n|',pla[2][0], pla[2][1], pla[2][2],'|\n\\---/'

pla1 : PlateauT = plateau_vide()
assert pla1[0][2] == " "
assert pla1[2][0] == " "


def videt (pla : PlateauT, i : int, j : int) -> bool : 
    """
    Precondition : i <= 2 and j <= 2
    
    """ 
    return pla[i][j] == " "


def jouex (pla : PlateauT, i : int, j : int) -> None : 
    """
    Place un X dans la case donné du plateau de morpion
    """
    pla[i][j] = "X"
    return None


def joueo (pla : PlateauT, i : int, j : int) -> None : 
    """
    PLace un O dans la case donné du plateau de morpion
    """
    pla[i][j] = "O"
    return None

assert videt (pla1 , 0, 2) == True
assert jouex (pla1 , 1, 1) == None
assert joueo (pla1 , 0, 2) == None
assert videt (pla1 , 0, 2) == False

def dessine_plateaut (pla : PlateauT) -> str :
    """
    Renvoie une chaine de caractères correspondant au jeu de morpion en cours
    """
    result : List[str] = [pla[i][2] + pla[i][1] + pla[i][0] + "\n" for i in range (3)]
    fin : str = ""
    u : str
    for u in result :
        fin = fin + u 
    return fin

assert (dessine_plateaut(pla1)) == "O  \n X \n   \n"

def gagnet (pla : PlateauT, caract : str ) -> bool :
    """
    Renvoie si le jeu est gagné, en fonction du signe
    """
    i : int
    
    for i in range(3) :
        if caract == pla[i][0] == pla[i][1] == pla[i][2] :
            return True

    j : int
    
    for j in range(3) :
        if caract == pla[0][j] == pla[1][j] == pla[2][j] :
            return True
        
    return (caract == pla[0][0] == pla[1][1] == pla[2][2]) or (caract == pla[0][2] == pla[1][1] == pla[2][0]) 


assert gagnet ([["O", " ", "X"], ["O", "X", " "], ["X", " ", " "]], "X") == True
assert gagnet ([["O", " ", "X"], ["O", "X", " "], ["X", " ", " "]], "O") == False
assert gagnet ([["X", " ", "O"], ["X", "O", " "], ["X", " ", " "]], "X") == True
assert gagnet ([["X", " ", "O"], ["O", "X", " "], ["X", " ", " "]], "X") == False
assert gagnet ([["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]], "O") == True



def pleint (pla : PlateauT) -> bool :
    """
    Renvoie si le jeu est plein, et résulte donc en une égalité
    """
    q : int = 0
    i : List[str]
    j : str
    
    for i in pla : 
        for j in i :
            if j != " " :
                q = q + 1
                
    return q == 9

assert pleint ([["X", " ", "O"], ["O", "X", " "], ["X", " ", " "]]) == False
assert pleint ([["O", "X", "O"], ["X", "O", "X"], ["O", "X", "O"]]) == True

def tourt (pla : PlateauT, i : int, j : int) -> Optional[str] :
    """
    Joue un tour de morpion, commençant par le joueur  
    """
    if pla[i][j] != " ":
        print('/-------\\\n|',pla[0][0], pla[0][1], pla[0][2] ,'|\n|',pla[1][0], pla[1][1], pla[1][2],'|\n|',pla[2][0], pla[2][1], pla[2][2],'|\n\\-------/')
        return "* Vous ne pouvez pas jouer ici *"

    jouex(pla, i, j)
    
    if gagnet(pla, "X") == True :
        print('/-------\\\n|',pla[0][0], pla[0][1], pla[0][2] ,'|\n|',pla[1][0], pla[1][1], pla[1][2],'|\n|',pla[2][0], pla[2][1], pla[2][2],'|\n\\-------/')
        return "*** Gagné ***"
    
    if pleint(pla) == True :
        print('/-------\\\n|',pla[0][0], pla[0][1], pla[0][2] ,'|\n|',pla[1][0], pla[1][1], pla[1][2],'|\n|',pla[2][0], pla[2][1], pla[2][2],'|\n\\-------/')
        return "Il y a égalité"

    a : int = int(random.random() * 2)
    b : int = int(random.random() * 2)
    while pla[a][b] != " " :
        a = int(random.random() * 2)
        b = int(random.random() * 2)

    joueo(pla, a, b)
    print("L'ordinateur joue en",'"',a,",",b,'"')
    
    if gagnet(pla, "O") == True :
        print('/-------\\\n|',pla[0][0], pla[0][1], pla[0][2] ,'|\n|',pla[1][0], pla[1][1], pla[1][2],'|\n|',pla[2][0], pla[2][1], pla[2][2],'|\n\\-------/')
        return '*** Perdu ***'
    
    if pleint(pla) == True :
        print('/-------\\\n|',pla[0][0], pla[0][1], pla[0][2] ,'|\n|',pla[1][0], pla[1][1], pla[1][2],'|\n|',pla[2][0], pla[2][1], pla[2][2],'|\n\\-------/')
        return "Il y a égalité"
    
    print('/-------\\\n|',pla[0][0], pla[0][1], pla[0][2] ,'|\n|',pla[1][0], pla[1][1], pla[1][2],'|\n|',pla[2][0], pla[2][1], pla[2][2],'|\n\\-------/')

    return None

plat_essai : PlateauT = plateau_vide()


def trace_jeu () -> Image :
    """
    Trace les cases du jeu de morpion 
    """
    q : float = 0.9
    
    im1 : Image = draw_line(-q, -q, -q, q)
    im1_1 : Image = draw_line(-q / 3, -q, -q / 3, q)
    
    im2 : Image = draw_line(-q, -q, q, -q)
    im2_2 : Image = draw_line(-q, -q/3, q, -q/3)
    
    im3 : Image = draw_line(-q, q, q, q)
    im3_3 : Image = draw_line(-q, q/3, q, q/3)
    
    im4 : Image = draw_line(q, -q, q, q)
    im4_4 : Image = draw_line(q/3, -q, q/3, q)
        
    return overlay(im1, im1_1, im2, im2_2, im3, im3_3, im4, im4_4)

def trace_croix (jeu_morp : Image, i : int, j : int) -> Image :
    """
    Trace une croix dans le jeu de morpion au coordonnées indiqués
    """
    coordinate_list : List[float] = [-0.9, -0.3, 0.3]
    
    im1 : Image = draw_line(coordinate_list[i] + 0.1, coordinate_list[j] + 0.1, coordinate_list[i] + 0.5, coordinate_list[j] + 0.5)
    im2 : Image = draw_line(coordinate_list[i] + 0.1, coordinate_list[j] + 0.5, coordinate_list[i] + 0.5, coordinate_list[j] + 0.1)
    
    return overlay(jeu_morp, im1, im2)

def trace_rond (jeu_morp : Image, i : int, j : int) -> Image :
    """
    Trace un rond dans le jeu de morpion au coordonnées indiqués
    """
    coordinate_list : List[float] = [-0.9, -0.3, 0.3]
    
    im1 : Image = draw_ellipse(coordinate_list[i] + 0.1, coordinate_list[j] + 0.1, coordinate_list[i] + 0.5, coordinate_list[j] + 0.5)
    
    return overlay(jeu_morp, im1)

def trace_morpion (pla : PlateauT) -> Image :
    """
    Trace un jeu de morpion à partir d'un jeu donné 
    """
    new_img : Image = trace_jeu()
    x : int
    
    for x in range(3) :
        y : int
        
        for y in range(3) :
            
            if pla[x][y] == 'X':
                im_temp_croix : Image = trace_croix(new_img, x, y)
                new_img = overlay(im_temp_croix, new_img)
                
            elif pla[x][y] == 'O' :
                im_temp_rond : Image = trace_rond(new_img, x, y)
                new_img = overlay(im_temp_rond, new_img)
                
    return new_img


def tour_morpion_complet (pla : PlateauT, i : int, j : int) -> Optional[str] : 
    """
    Joue un tour entier de morpion
    """
    if pla[i][j] != " ":
        show_image(trace_morpion(pla))
        return "* Vous ne pouvez pas jouer ici *"

    jouex(pla, i, j)

    if gagnet(pla, "X") == True :
        show_image(trace_morpion(pla))
        return "*** Gagné ***"

    if pleint(pla) ==  True :
        show_image(trace_morpion(pla))
        return "Le tableau est plein, il y a égalité"       
    
    a : int = int(random.random() * 2)
    b : int = int(random.random() * 2)
    while pla[a][b] != " " :
        a = int(random.random() * 2)
        b = int(random.random() * 2)

    joueo(pla, a, b)
    print("L'ordinateur joue en",'"',a,",",b,'"')

    if gagnet(pla, "O") == True : 
        show_image(trace_morpion(pla))
        return "*** Perdu ***" 

    if pleint(pla) ==  True :
        show_image(trace_morpion(pla))
        return "Le tableau est plein, il y a égalité" 

    show_image(trace_morpion(pla))

    return None



