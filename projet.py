import os
import json
from PIL import Image
import numpy
import math
from sklearn.cluster import MiniBatchKMeans
import random

#Fonction permettant de déterminer la couleur dominante d'une image
#Entrées : chemin vers un de nos tableaux
#Sorties : Les codes RGB de la couleur dominante
def Couleur(path):
    
    imgfile = Image.open(path)
    numarray = numpy.array(imgfile.getdata(), numpy.uint8) #ouverture et stockage de l'image dans un tableau

    #utilisation de l'algorithme MiniBatchKMeans pour déterminer la couleur dominante de l'image
    cluster_count = 2
    clusters = MiniBatchKMeans(n_clusters = cluster_count)
    clusters.fit(numarray)

    #création de l'histogramme pour classer les différentes couleurs dominantes par ordre d'importance
    npbins = numpy.arange(0, cluster_count + 1)
    histogram = numpy.histogram(clusters.labels_, bins=npbins)

    #récupération des codes RBB de la couleur dominante
    imax = numpy.argmax(histogram[0])
    R = math.ceil(clusters.cluster_centers_[imax][0])
    G = math.ceil(clusters.cluster_centers_[imax][1])
    B = math.ceil(clusters.cluster_centers_[imax][2])
    return [R,G,B]

#génération des tableaux
#on stocke les éléments suivants : le chemin vers l'image, l'auteur, la largeur, la hauteur
#le format, les tags mis par les utilisateurs, le nombre de likes et la couleur dominante
listeTableau=[]
for dossier in os.listdir('./images'):
    for image in os.listdir('./images/'+dossier):
        file='./images/'+dossier+'/'+image
        imgfile=Image.open(file)
        [width,height] = [imgfile.width,imgfile.height]
        if width/height > 1.1:
            format='paysage'
        elif height/width > 1.1:
            format='portrait'
        else:
            format='carre'

        dictionnaire = {}
        dictionnaire["lien"]=file
        dictionnaire["auteur"]=dossier
        dictionnaire["largeur"]=str(width)
        dictionnaire["hauteur"]=str(height)
        dictionnaire["format"]=format
        dictionnaire["tags"]=[] #la liste des tags est vide mais sera complétée plus tard 
        dictionnaire["likes"]=0 #idem
        dictionnaire["unlikes"]=0 #idem
        dictionnaire["couleur"]=Couleur(file)
        listeTableau.append(dictionnaire)
        


#on génère une liste de 100 utilisateurs qui vont rajouter 20 likes et 20 tags sur des tableaux aléatoires
#un utilisateur est composé des éléments suivants : une id, la liste de ses lies, la liste de ses tableaux taggés
#sa couleur préférée, son tag préféré
#la liste des tags possibles
tags = ["impressionnisme","abstrait","emouvant","decevant","chef-d'oeuvre","acrylique","aquarelle","printanier"] 
listeUser=[]
for userId in range(100):
    dictionnaireUser={}
    dictionnaireUser["id"]=userId
    dictionnaireUser["likes"]=[]
    dictionnaireUser["tags"]={}
    dictionnaireUser['couleurPref']=[]
    dictionnaireUser['tagPref']=''
    dictionnaireUser["unlikes"]=[]
    for i in range(20):
        #génération des likes
        randint=random.randint(0,len(listeTableau)-1)
        like=listeTableau[randint]
        dictionnaireUser["likes"].append(like["lien"]) #on ajoute le lien du tableau liké à la liste des likes
        listeTableau[randint]["likes"]+=1 #on ajoute un like sur le tableau
        
        #génération des unlikes
        randint=random.randint(0,len(listeTableau)-1)
        unlike=listeTableau[randint]
        if unlike["lien"] not in dictionnaireUser["likes"] :
            dictionnaireUser["unlikes"].append(unlike["lien"]) #on ajoute le lien du tableau unliké à la liste des likes
            listeTableau[randint]["unlikes"]+=1 #on ajoute un unlike sur le tableau

        #génération des tags
        randint=random.randint(0,len(listeTableau)-1)
        randint2=random.randint(0,len(tags)-1)
        tableauTag=listeTableau[randint]
        tag=tags[randint2]
        dictionnaireUser["tags"][tableauTag["lien"]]=tag 
        if tag not in listeTableau[randint]["tags"]:
            #on ajoute le tag au tableau s'il n'est pas déjà présent
            listeTableau[randint]["tags"].append(tag) 
    listeUser.append(dictionnaireUser)

    
with open('user.json','w') as jsonfile2:   
    jsonfile2.write(json.dumps(listeUser, ensure_ascii=False))
with open('label.json','w') as jsonfile :
    jsonfile.write(json.dumps(listeTableau, ensure_ascii=False))





    
            
        