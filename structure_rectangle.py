# Programmation Oriente Objet
# creation de classe est une structure compose de 
# methodes et des attributs
# une classe c'est le fait de regrouper des donnees(attributs et champs)
# et les traitement dans une meme entite
# la premiere lettre du nom d'une classe commence par une lettre
# majuscule

class Rectangle:
    def __init__(self,longueur,largeur): 
        self.longueur=longueur
        self.largeur=largeur
    def surface(self): # on a pas besoin d'envoyer en parametres longueur et largeur grace au lien semantique
        return self.longueur*self.largeur
    def perimetre(self):
        return (self.longueur*self.largeur)*2
    def demiperimetre(self):
        return (self.longueur*self.largeur)
    def diagonale(self):
        return (self.longueur**2+self.largeur**2)**(1/2)
    





