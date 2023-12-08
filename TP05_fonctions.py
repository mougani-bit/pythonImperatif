# EX01_SOMME_NB_PAIRS

def somme_nombres_pairs(liste):
    somme = 0
    for nombre in liste:
        if nombre % 2 == 0:
            somme += nombre
    return somme
ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultat = somme_nombres_pairs(ma_liste)
print("La somme des nombres pairs dans la liste est :", resultat)

# EXO02_PALINDROME

def est_palindrome(chaine):
    chaine = chaine.lower()  # Convertir la chaine en minuscules pour ignorer la casse
    return chaine == chaine[::-1]

mot = "bob"
if est_palindrome(mot):
    print(f"{mot} est un palindrome.")
else:
    print(f"{mot} n'est pas un palindrome.")

# EXO3_RECHERCHEMINMAX

def recherche_min_max(minimum, maximum, liste):
    resultats = [nombre for nombre in liste if minimum <= nombre <= maximum]
    return resultats

liste = [1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4]
min_value = 5
max_value = 15
resultat_recherche = recherche_min_max(min_value, max_value, liste)

print(f"Les éléments entre {min_value} et {max_value} inclus sont : {resultat_recherche}")

# EX04_CALCULMOYENNE

def calcul_moyenne(liste):
    if not liste:
        return 0
    return sum(liste) / len(liste)

liste_notes = [85, 90, 78, 92, 88]
moyenne = calcul_moyenne(liste_notes)

print(f"La moyenne des éléments dans la liste est : {moyenne}")
