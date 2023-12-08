
# Affichage de tous les nombres entiers pairs entre 0 et 10 inclus
print("Nombres entiers pairs :")
for i in range(0, 11):
    if i % 2 == 0:
        print(i)

# Affichage de tous les nombres entiers impairs entre 0 et 10 inclus
print("\nNombres entiers impairs :")
for i in range(0, 11):
    if i % 2 != 0:
        print(i)

# Exercice 2

# Déclaration de la liste
ma_liste = [1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4]

# Affichage de tous les éléments de la liste grâce à la boucle
print("Tous les éléments de la liste :")
for element in ma_liste:
    print(element)

#gi Affichage uniquement des éléments positifs grâce à une boucle combinée à un if
print("\nLes éléments positifs de la liste :")
for element in ma_liste:
    if element > 0:
        print(element)

# Calcul du nombre d'éléments positifs et affichage
nombre_elements_positifs = sum(1 for element in ma_liste if element > 0)
print("\nNombre d'éléments positifs dans la liste :", nombre_elements_positifs)
