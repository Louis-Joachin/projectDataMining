import os,sys
import csv
from turtle import width
from PIL import Image


with open('label.csv','w',newline='') as csvfile :
    label = csv.writer(csvfile, delimiter=',')
    for dossier in os.listdir('./images'):
        for image in os.listdir('./images/'+dossier):
            label.writerow(['./images/'+dossier+'/'+image]+[dossier])
            width=image.width()
            height=image.height()
            



        



