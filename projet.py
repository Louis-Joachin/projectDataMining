import os
import json
from PIL import Image
import numpy
import math
import matplotlib.pyplot as plot
from sklearn.cluster import KMeans
import random

def Couleur(path):
    
    imgfile = Image.open(path)
    numarray = numpy.array(imgfile.getdata(), numpy.uint8)

    cluster_count = 2
    clusters = KMeans(n_clusters = cluster_count)
    clusters.fit(numarray)

    npbins = numpy.arange(0, cluster_count + 1)
    histogram = numpy.histogram(clusters.labels_, bins=npbins)

    imax = numpy.argmax(histogram[0])
    R = math.ceil(clusters.cluster_centers_[imax][0])
    G = math.ceil(clusters.cluster_centers_[imax][1])
    B = math.ceil(clusters.cluster_centers_[imax][2])
    return [R,G,B]

with open('label.json','w') as jsonfile :
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
            dictionnaire["tags"]=[]
            dictionnaire["likes"]=0
            #dictionnaire["couleur"]=Couleur(file)
            listeTableau.append(dictionnaire)
            
    string=str(listeTableau)
    jsonfile.write(json.dumps(listeTableau, ensure_ascii=False))
    jsonfile.close()

    
with open('user.json','w') as jsonfile :
    tags = ["impressionnisme","abstrait","emouvant","decevant","chef-d'oeuvre","acrylique","aquarelle","printanier"]
    listeUser=[]
    dictionnaireUser={}
    for userId in range(100):
        dictionnaireUser["id"]=userId
        dictionnaireUser["likes"]=[]
        for i in range(20):
            randint=random.randint(0,len(listeTableau)-1)
            like=listeTableau[randint]
            dictionnaireUser["likes"].append(like["lien"])
            listeTableau[randint]["likes"]+=1
    print(listeTableau)
            
        