# Face-recognition-app
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Steps](#steps)
* [Result](#Result)

## General info
This face recognition project  involves using computer algorithms and machine learning techniques to identify and verify individuals 
based on their facial features  it can be used in a wide range of potential applications in fields such as security, entertainment, and healthcare.
The project is based on  face_recognition library : it's a powerful and versatile tool  presenting a high accuracy and speed result, which are achieved by using a deep learning model trained
on millions of faces. The model uses a neural network architecture called a Convolutional Neural Network (CNN),
which is able to extract high-level features from images and make accurate predictions.


## Technologies
Project is created with:
* python 3.+(in my case 3.7)
* differents libraries 

## Steps
1. Collect and preprocess a dataset of labelled faces: his involves gathering images of individual faces,preferably  cleaning, cropping, and standardizing images 
to ensure consistency and accuracy.
2. Train  the a face recognition model: This involves  training a machine learning model to recognize faces,in our case the convolutional neural networks (CNNs) implemented in face recognition library. 
The model is trained on our  labeled dataset of faces, learning to extract features and patterns that distinguish one face from another by deploying a distance metric to compare these features to the known faces in the database.
3.Test and evaluate the model: This involves evaluating the accuracy and performance of the trained model using a separate set of unlabelled test images 
4. web implementation : a simple html web page is used to show result , you browse first  your local machine to choose the image and passed  as image test in our model
5. Save result: After identifying a known face, we save the result in a JSON file that includes the name of the person, and the link of the input image that may be relevant.
for  each  new recognition , we append result to the existing JSON file, so that it acts as a record of all the recognitions that have been made.

## Result 
* face detection, our library is able to detect faces in images and videos, and return the location of the face in the image or video frame.
The library is able to detect faces with high accuracy, even in challenging conditions such as low light, occlusion, and variations in pose and expression.

* face recognition, the library is able to identify individuals in images or videos by comparing them to a known database of faces. 
The result is a list of potential matches, ranked by their similarity to the input face.
The accuracy of the face recognition results depends on the quality of the input data and the size and quality of the database of known faces.  
This exemple of result :  
![detection and recognition face](https://github.com/oumaima-sboui/Face-recognition-app/blob/master/output.jpg)
