import os,sys
import csv
from turtle import width
from PIL import Image


with open('label.csv','w',newline='') as csvfile :
    label = csv.writer(csvfile, delimiter=',')
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
            
            label.writerow([file]+[dossier]+[width]+[height]+[format])
            

    
        



