"""
print('hello word')"""
"""
#age
age = input ('c est quoi votr age ?')
print ('mon age est '+ age)
#string
name='sami'
print('sami')
#float
pi=3.14
print(pi)
#variable
x,y,z = 13,14,15
print(x)
print(y)
print(z)

a,b,c = 'wafa','raya','maya'
print(a)
#list
voitures=['range','bmw','tesla']
print(voitures)

#affichage nom et prenom
NOM = input ('quel est votre Nom ')
PRENOM = input('quel est votre Prenom ')

print('votre nom et prenom :' + PRENOM +' '+ NOM ) 

first_name='jhon'
last_name='Smith'
full_name=first_name.capitalize() +' '+ last_name.upper()
print(full_name)
print(len(full_name))
print(len(first_name))
print(full_name.endswith('SMITH'))

addition=4+4
print(addition)
soustraction=5-2
print(soustraction)
multiplication=3*3
print(multiplication)
division=10/2
print(division)
mod=10%3
print(mod)




print (10<=10)
print(2==2)
print(5<8)
print('wafa'.endswith('e'))
print('wafa'.endswith('a'))
#variable sochés
is_adult = True
is_teenager= False


x= '5'
y='wafa'
print(x + y)


x="awesome"
def myfunction():
    global x
    x= 'fantatic'
myfunction()
print ("python is" + x)

x= 'wafa'
print(type(x))

x=3+5j
y=5j
z=-5j
print(type(x))
print(type(y))
print(type(z))

x=1
y=2.8
z=1j

a=float(x)
b=int(y)
c=complex(z)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

a='hello , word'
print(a[-2:-7])

a=' hello , word '
print(a.strip())

a=' Hello , word '
print(a.lower())

a='Hello , word'
print(a)
print(a.split('.'))

#existe
txt='the rain in spain stays mainly in the plain'
x='ain' in txt
print(x)
#notExiste
txt='the rain in spain stays mainly in the plain'
x='ain' not in txt
print(x)

quantity=3
itemNo=567
price=49.95
myorder='i want {2} peaces of item {0} for {1} dollars'
print(myorder.format(quantity,itemNo,price))


from datetime import datetime
from tkinter import TRUE


TXT ="we are so-called \"viking\" from north"
print(TXT)
TXT ="we are so-called \"viking\" from north"
print(TXT)

x=datetime.now()
print(x.year)

IS_ADULT=False

if IS_ADULT:
    print('IS_ADULT')

else:
  print('is not an adult')      



age=15

if age>=23:
   print('adult')
else:
   print('not adult')  

   names=['wafa' , 'lara', 'houda','maya']
   print(len(names))


names=['wafa' , 'lara', 'houda','maya']
for name in names:
       print(name.capitalize())
       

volume = int (input('donner le volume')) 
if volume >= 70:
    print('eau gaziffié')
elif 0 < volume <= 10:
    print('eau normal')
else:
    print('Glassée')

    
    

fruits=['fraise','banane','kiwi']
for fruit in fruits:
    print(fruit)

nums=[17,38,10,25,72]

for num in nums:
   print(num)
nums.append(12)
print(nums)

List = [17,38,10,25,72]
print("Liste initiale :  ") 
print(List) 
  
# Ajout d'un élément à position spécifique (en utilisant la méthode d'insertion)  
List.insert(72, 12) 
print("\nListe après avoir effectué l'opération d'insertion : ") 
print(List)
List.insert(0,0) 
for i in List:
 print(i) 

thislist=['fraise','banane','kiwi']
thislist[1]='orange'
print(thislist)

thislist=['fraise','banane','kiwi']
thislist.remove("banane")
print(thislist)

thislist=['fraise','banane','kiwi']
thislist.pop
print(thislist)

thislist=['fraise','banane','kiwi']
del thislist[0]
print(thislist)

thislist=['fraise','banane','kiwi']
del thislist
print(thislist)

thislist=['fraise','banane','kiwi']
thislist.clear()
print(thislist)

thislist=['fraise','banane','kiwi']
mylist = thislist.copy()
print(mylist)

thislist=['fraise','banane','kiwi']
mylist = list(thislist)
print(mylist)

list1=[1, 2, 3, 4]
list2=["a","b","c"]

list3=list1+list2
print(list3)

list1=[1, 2, 3, 4]
list2=["a","b","c"]
for x in list2:
    list1.append(x)
print(list1)

list1=[1, 2, 3, 4]
list2=["a","b","c"]
list1.extend(list2)
print(list1)

list1=[1, 2, 3, 4]
list1.reverse()

list=list1.copy()
print(list)

x=('fraise','banane','kiwi')
y=list(x)
y[1]="kiwi"
x=tuple(y)
print(x)

thistuple=("apple",)
print(type(thistuple))

thisset={'fraise','banane','kiwi'}
print(thisset)


thisdisct = {
    'brand':'ford',
    'model':'mostang',
    'year' :1964
}
print(thisdisct)

x = thisdisct['model']
print(x)

y = thisdisct.get('model')
print(y)

for x in thisdisct.values():
   print(x)
for x in thisdisct.items():
   print(x)

thisdisct['color']='red'

persondict = {

    'nom':'mekni',
    'prenom ' :'ahmed',
    'sexe' : 'homme',
    'age': 23

}

for x in persondict.values():
    print(x)
if 'age' in persondict:
    print('existe')
persondict['mail']='ahmed@gmail.com'
persondict['age']='30'
print(persondict)
x= print(len(persondict))
print(x)
persondict.pop('mail')
print(persondict)

user=persondict.copy()
print(user)

myfamily = {
       'child1' : {
        'name':'wafa',
        'age':   25
    },
       'child2' : {
        'name':'ahmed',
        'age':   23
    },
       'child3' : {
        'name':'sourour',
        'age':   28
    }
}
print(myfamily)

i=1
while i<6:
   print(i)
   i +=1
else: 
   print ('is notlonger less than 6 ')


i=0
while i<6:
    i +=1
    if i==3:
        continue

    print (i)

i=1
while i<6:
   print(i)
   if i==3:
        break
   i +=1

i=1
while i<6:
   print(i)
   i +=1

def my_function():
    print('hello in my function')

def my_function():
    print('hello in my function')   
my_function()

def my_function(fname):
    print(fname +   'hello in my function')   

my_function('Emil')
my_function('tobias')
my_function('linux')



x = 5
try:
    print(x)
except:
    print('an exception occurred')
"""

