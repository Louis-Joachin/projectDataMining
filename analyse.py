from pandas import json_normalize
import pandas as pd
import json
import numpy
from sklearn.cluster import MiniBatchKMeans
import math

jsonTab=open("label.json",'r')
dataTab = json.load(jsonTab)
jsonTab.close()
dataframeTab = json_normalize(dataTab)

jsonUser=open("user.json",'r')
dataUser = json.load(jsonUser)
jsonUser.close()
dataframeUser = json_normalize(dataUser)

def ComparaisonCouleur(couleur1, couleur2):
    dif = []
    for i in range (3):
        dif.append(couleur1[i] - couleur2[i])
    #mise au carré pour être sûr d'avoir des valeurs de diférence positive 
    return dif[0]**2+dif[1]**2+dif[2]**2

couleursPref = []
#récupération des couleurs dominates des tableaux likés par l'utilisateur 0
for tab in dataTab:
    if tab['lien'] in dataUser[0]['likes']:
        couleursPref.append(tab['couleur'])

#partitionement des couleurs dominantes de tous les tableaux en 3 cluster
couleursPref = MiniBatchKMeans(3).fit(couleursPref)
#création d'un numpyarray
npbins = numpy.arange(0, 4)
#création d'un histogramme qui classe les clusters par odre croissant
histogram = numpy.histogram(couleursPref.labels_, bins=npbins)
imax = numpy.argmax(histogram[0])

R = math.ceil(couleursPref.cluster_centers_[imax][0])
G = math.ceil(couleursPref.cluster_centers_[imax][1])
B = math.ceil(couleursPref.cluster_centers_[imax][2])

dataUser[0]['couleurPref']=[R,G,B]

listeTag=[]
compteTag=[]
for tableau in dataUser[0]['tags']:
    tag=dataUser[0]['tags'][tableau]
    
    
    if tag in listeTag:
        compteTag[listeTag.index(tag)]+=1
    else:
        compteTag.append(1)
        listeTag.append(tag)

print(listeTag,compteTag)


tagPref=listeTag[compteTag.index(max(compteTag))]
dataUser[0]['tagPref']=tagPref


jsonUser=open("user.json",'w')
jsonUser.write(json.dumps(dataUser, ensure_ascii=False))
jsonUser.close()



