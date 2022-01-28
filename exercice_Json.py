def saisie():
  h = "oui"
fichier = open("wafa.txt","a")
decision = {"a:admis(e)","r:refuse(e)","aj;ajourne(e)"}
x = "oui"
while x == "oui":
       nom = input('saisie le nom:')
       
       prenom = input('saisie le prenom:')
       
       CIN=input('saisie le CIN:')
       
       Age=input('saisie le age:')
      
       decision=input("saisie une decicion:a:admis(e),r:refuse(e),aj;ajourne(e)")
       break
info= nom +","+prenom+","+CIN+","+Age+","+decision
print(info)
fichier.write(info)

saisie()

fichier_Admis = open("zq.txt","w")

fichier_Collab = open("wafa.txt","r")
for infos in fichier_Collab:
    variable=infos.split(",")
    print(variable)
    for i in variable:
     if decision =="a":    
        fichier_Admis.write(variable)
        print("fiche",fichier_Admis)
fichier_Admis.close()
fichier_Collab.close()





  



    




