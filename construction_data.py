from pandas import json_normalize
import pandas as pd
import matplotlib.pyplot as plt
import json
from sklearn.preprocessing import LabelEncoder
from sklearn import tree

#ouverture des fichiers précédemment créés
with open("label.json",'r') as jsonTab:
    dataTab = json.load(jsonTab)

with open("user.json",'r') as jsonUser:
    dataUser = json.load(jsonUser)


data=[]
result=[]
for lien in dataUser[0]["likes"]:
    for tableau in dataTab:
        if lien == tableau["lien"]:
            data.append([tableau["auteur"],tableau["format"],tableau["tags"]])
            result.append(1)

for lien in dataUser[0]["unlikes"]:
    for tableau in dataTab:
        if lien == tableau["lien"]:
            data.append([tableau["auteur"],tableau["format"],tableau["tags"]])
            result.append(0)
            
print(data)


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

#prediction
prediction = dtc.predict([
        [le1.transform(['davinci'])[0], le2.transform(['carre'])[0],
         le3.transform(["['aquarelle','acrylique','printanier']"])[0]]])
print(le4.inverse_transform(prediction))
print(dtc.feature_importances_)