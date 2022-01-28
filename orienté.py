"""


class Person:
 def __init__(self,name,age):
     self.name = name
     self.age = age

p1= Person("jhon",36)
print(p1.name)
print(p1.age)

"""
"""
class Person:
 def __init__(self,name,age):
     self.name = name
     self.age = age

 def wafa(self):
         print('hello my name is : ' + self.name)
     

p1 = Person("jhon",36)
p1.wafa()



class Voiture:

  voiture_crees = 0
  def __init__(self,modele,prix=1):
        self.modele = modele
        self.prix = prix 
        Voiture.voiture_crees += 1

  def roule (self):
        print("la voiture roule")

  def marche_en_arriere(self):
        print("la voiture marche arriere")
    
  def info():
        print("methode static")

  info = staticmethod(info)
Voiture.info()

class Pizza:
    def __init__ (self, ingredients):
        self.ingredients = ingredients

    def __repr__ (self, ingredients):
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls):
        return cls (['mozzarella', 'tomatoes'])
    
    @classmethod
    def prosciuto(cls):
        return cls (['mozzarella','tomatoes','ham'])

class Voiture:

    def __init__(self,vitesse):
        self.__vitesse = vitesse
    
    @property
    def vitesse (self):
        print("hello from getter vitesse")
        return self.__vitesse

    def __str__(self):
        return"la voiture a le vitesse {}".format(self.__vitesse)

v1 = Voiture (10)
print(v1.vitesse)
v1.__vitesse =5
print(v1.vitesse)

class Voiture:

    def __init__(self,vitesse):
        self.__vitesse = vitesse
    def __go__(self):
     print("hello from go")
    
    @property
    def vitesse (self):
     
        return self.__vitesse
    
    @vitesse.setter
    def vitesse (self,vitesse):
        if self.__vitesse < vitesse:
            print("can t change vitesse")
        else:
            print("changement du vitesse")
            self.vitesse = vitesse
    def _str_(self):
        return "la voiture a le vitesse{}".format(self.__vitesse)

    

v1= Voiture(10)
v1.__go__()

"""
class Vehicule:
  def __init__(self,marque,couleur):
     self.marque = marque
     self.couleur = couleur

  def printname(self):
     print(self.marque , self.couleur)
marque = input('c est quoi la marque ?')
print('bonjour, je suis une vehicule ' +marque)

class voiture(Vehicule):
 def __init__(self,marque,couleur,vitesse):
     self.vitesse = vitesse
     super().__init__(marque,couleur)
 def message(self):
       print(self.vitesse)
vitesse = input ('c est quoi la vitesse ? ' )
couleur = input('c est quoi la couleur ?')
print('bonjour, je suis une vehicule de la marque ' +marque+' de couleur '+couleur+ ' avec une vitesse de '+vitesse)
print("bonjour, je suis une voiture")
    




     

