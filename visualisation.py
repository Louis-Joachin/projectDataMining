from pandas import json_normalize
import pandas as pd
import matplotlib.pyplot as plt
import json
import numpy
from sklearn.cluster import MiniBatchKMeans
import math

#ouverture des fichiers précédemment créés
with open("label.json",'r') as jsonTab:
    dataTab = json.load(jsonTab)
dataframeTab = json_normalize(dataTab)

with open("user.json",'r') as jsonUser:
    dataUser = json.load(jsonUser)
dataframeUser = json_normalize(dataUser)

grouped=dataframeTab.groupby("auteur").agg(['count'])
dataframeTab.plot()