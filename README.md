# The goal of the project

The goal of this project is to recommend images based on the preferences of the user. The final goal is to create a recommendation system that suggests images to a user. In order to do this, we must create a user-preference profile and a file that stores information about the images to predict the perfect image that will be liked by our user.

# Size of the data and license

We choose a dataset from Kaggle :
https://www.kaggle.com/datasets/binukandagedon/paintings-from-10-different-popular-artists

There are 605 different paintings that are organized in a few folders. Each folder represents an artist and we have 10 different artists. The license is not specified on the website. 

# Information that we decided to store for each image

We chose to store all information about our images in a json file because it is commonly used for data mining in many companies. This is label.json in our project.
The following informations are available for each image :

- lien : the path to access to the files from the notebook
- auteur : the name of the folder where the file is. This is the artist's name.
- largeur : the width of the image
- hauteur : the height of the image
- format : the image orientation
- tags : a dictionary of each tag available as keys and the number of users that used it on this image as values.
- likes : the number of users that liked this image after seeing it.
- unlike : the number of users that did not like this image after seeing it.
- couleur : the dominant color of the image.






# Information concerning user preferences

We decided to create a json file to simulate 100 different users. It is called user.json in our project. For each user we have a dictionary were the following informations are the keys :
- id : the number that identified each user.
- likes : a list of each “lien” of the images liked by the user.
- tags : a dictionary that contains the “lien” of the image tagged as a key and the tag chosen as a value.
- couleurPref : The dominant color of the K-means of each dominant color of the images liked. 
- tagPref : the tag that is the most used by the user.
- unlikes : a list of each “lien” of the images not liked by the user.


# Data mining and/or machine learning models that we used along with the metrics obtained.

In this part, we will explain each part of the project and how we used algorithms that were presented during laboratory courses. 

## Labeling and Annotation

The EXIF of our data were useless, because most of them were removed by Kaggle. Moreover they were irrelevant for label paintings.</br>
The predominant color is determined with a MiniBatchKMeans algorithm. We chose it because it is faster than the standardKmeans algorithm. In order to reduce the time of execution of the program we chose to analyze the first three dominant colors with 3 clusters and to add the most predominant in the label.json file for each image.</br>
The folder of the image gave us the name of the artist and for the image orientation, the height and the width were measured and compared.</br>
The process of tagging images is fully automated with the user simulation. Each user will randomly choose a label for each image they liked. This information will be stored in user.json and label.json. </br>

## Data Analyses

As previously said, we created 100 users in the file user.json. We used a K-means algorithm to analyze their favorite color and did a simple counter in order to choose their favorite tag and image orientation.

## Data Visualization

We choose to visualize the information that we found the most relevant.

As you can see on the  final notebook they are :
- a pie chart with the five most dominant colors for every image
- a bar graph with the number of images by artists
- a bar graph with the number of images by format
- a bar graph with the number of images by like.

At the end of the notebook, we choose to share with the user all information about them and each image that they liked.

## Recommendation System

Our recommendation system is based on two dataframes. The first one contains all the liked and unliked images with the author, the image orientation and the most used tag. The second contains a 1 if the image is liked by the user and a -1 if not.</br>
At the end of the decision tree, we will have 10 recommendations. We will now use our fonction comparaisonCouleur that we created to find the closest dominant color from the favorite color of our user.</br>
This image will be displayed after the title “Notre recommandation”. The nine other will be displayed after the title “Les tableaux qui pourraient aussi vous plaire :”.</br>
We used every characteristic that we had for each user. One way to improve our recommendation system would  be to store more information. The favorite colors were not taken into account in the beginning but thanks to our comparaisonColor function, we manage to bypass this issue.</br>

