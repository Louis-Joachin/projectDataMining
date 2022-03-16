import os
import json
from turtle import width
from PIL import Image


with open('label.json','w') as jsonfile :
    liste=[]
    for dossier in os.listdir('./images'):
        for image in os.listdir('./images/'+dossier):
            file='./images/'+dossier+'/'+image
            imgfile=Image.open(file)
            [width,height] = [imgfile.width,imgfile.height]
            if width/height > 1.1:
                format='paysage'
            elif height/height > 1.1:
                format='portrait'
            else:
                format='carre'

            dictionnaire = {}
            dictionnaire["lien"]=file
            dictionnaire["auteur"]=dossier
            dictionnaire["largeur"]=str(width)
            dictionnaire["hauteur"]=str(height)
            dictionnaire["format"]=format
            dictionnaire["tags"]=[]
            dictionnaire["likes"]=0
            liste.append(dictionnaire)
    string=str(liste)
    jsonfile.write(json.dumps(liste, ensure_ascii=False))
    jsonfile.close()

    
with open('user.json','w') as jsonfile :
    liste=[]
    dictionnaireUser={}
    for userId in range(100):
        dictionnaireUser["id"]=userId
        dictionnaireUser["likes"]=[]




