from pandas import json_normalize
import pandas as pd
import matplotlib.pyplot as plt
import json
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
import operator
import random


#Fonction de comparaison de couleurs
#Entrées : deux codes RGB de deux couleurs
#Sorties : un indice de proximité des couleurs
def ComparaisonCouleur(couleur1, couleur2):
    dif = []
    for i in range (3):
        dif.append(couleur1[i] - couleur2[i])
    #mise au carré pour être sûr d'avoir des valeurs de diférence positive 
    return dif[0]**2+dif[1]**2+dif[2]**2

#ouverture des fichiers précédemment créés
with open("label.json",'r') as jsonTab:
    dataTabCustom = json.load(jsonTab)

with open("user.json",'r') as jsonUser:
    dataUser = json.load(jsonUser)


data=[]
result=[]
auteur_vu=[]
dataTab = dataTabCustom
for lien in dataUser[0]["likes"]:
    for tableau in dataTab:
        if lien == tableau["lien"]:
            tag = max(tableau["tags"].items(), key=operator.itemgetter(1))[0]
            data.append([tableau["auteur"],tableau["format"],tag])
            result.append(1)
            auteur_vu.append(tableau["auteur"])
            dataTabCustom.remove(tableau)
            

for lien in dataUser[0]["unlikes"]:
    for tableau in dataTab:
        if lien == tableau["lien"]:
            tag = max(tableau["tags"].items(), key=operator.itemgetter(1))[0]
            data.append([tableau["auteur"],tableau["format"],tag])
            result.append(-1)
            auteur_vu.append(tableau["auteur"])
            dataTabCustom.remove(tableau)



dataframe = pd.DataFrame(data, columns=['auteur', 'format', 'tags'])
resultframe = pd.DataFrame(result, columns=['like'])

le1 = LabelEncoder()
dataframe['auteur'] = le1.fit_transform(dataframe['auteur'])

le2 = LabelEncoder()
dataframe['format'] = le2.fit_transform(dataframe['format'])

le3 = LabelEncoder()
dataframe['tags'] = le3.fit_transform(dataframe['tags'])

le4 = LabelEncoder()
resultframe['like'] = le4.fit_transform(resultframe['like'])

#Use of decision tree classifiers
dtc = tree.DecisionTreeClassifier()
dtc = dtc.fit(dataframe, resultframe)

recommandation = []
while len(recommandation)<10:
    tab = random.choice(dataTabCustom)
    if tab["auteur"] not in auteur_vu:
        continue
    prediction = dtc.predict([
            [le1.transform([tab["auteur"]])[0], le2.transform([tab["format"]])[0],
            le3.transform([max(tableau["tags"].items(), key=operator.itemgetter(1))[0]])[0]]])
    if prediction == 1:
        recommandation.append(tab)
        
for tab in recommandation:
    tab["indice_couleur"]=ComparaisonCouleur(dataUser[0]["couleurPref"],tab["couleur"])
