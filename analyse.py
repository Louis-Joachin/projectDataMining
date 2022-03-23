from pandas import json_normalize
import pandas as pd
import json
import numpy
from sklearn.cluster import MiniBatchKMeans

dataTab = json.load(open("label.json"))
dataframeTab = json_normalize(dataTab)

dataUser = json.load(open("user.json"))
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

