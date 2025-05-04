# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define n = Character('Narateur', color="#c8ffc8")


# Le jeu commence ici
label start:

    n "Vous venez de créer un nouveau jeu Ren'Py."

    n "Après avoir ajouté une histoire, des images et de la musique, vous pourrez le présenter au monde entier !"

    #call screen arrowScreen
    #show screen arrowScreen

label checkingOnStudents:

    scene passenger

    n "something"

    return



