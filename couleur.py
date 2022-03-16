from PIL import Image
import numpy
import math
import matplotlib.pyplot as plot
from sklearn.cluster import KMeans
imgfile = Image.open("/fs03/share/users/baptiste.boiteux/home/Documents/S8/Data_Mining/projet/projetFouilledeDonnees/images/davinci/0.jpg")
numarray = numpy.array(imgfile.getdata(), numpy.uint8)

cluster_count = 5 
clusters = KMeans(n_clusters = cluster_count)
clusters.fit(numarray)

npbins = numpy.arange(0, cluster_count + 1)
histogram = numpy.histogram(clusters.labels_, bins=npbins)

imax = numpy.argmax(histogram[0])
R = math.ceil(clusters.cluster_centers_[imax][0])
G = math.ceil(clusters.cluster_centers_[imax][1])
B = math.ceil(clusters.cluster_centers_[imax][2])

print("La couleur dominante est r ="+str(R)+"g="+str(G)+"b="+str(B)+"d'indice :"+str(imax))
'''
for i in range(cluster_count):
    print(str(i)+" : "+str('#%02x%02x%02x' % (
    math.ceil(clusters.cluster_centers_[i][0]),
        math.ceil(clusters.cluster_centers_[i][1]), 
    math.ceil(clusters.cluster_centers_[i][2])))+" npbins: "+str(histogram[0][i]))
'''