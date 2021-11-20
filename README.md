# Cats_and_dogs_recognition
Repository for a student project. The aim is to build an AI model capable of recognizing cats and dogs in a picture.


##The Data

For that project we will use a dataset of cats and dogs picture. This dataset can be downloaded at https://www.kaggle.com/biaiscience/dogs-vs-cats

The train data is composed of 25 000 pictures. 12500 cats and 12500 dogs.

![cat 1](https://user-images.githubusercontent.com/65913620/142731548-ac6e409e-f3e5-499f-b988-19bc80e495f3.jpg)
![dog 12423](https://user-images.githubusercontent.com/65913620/142731554-5cb37c89-8a32-4df3-a15a-4f1038928ea2.jpg)

##Pytorch Model
In the Cats_and_dog_pytorch notebook you can follow our step in selecting and testing model. The goal of that notebook is to build a from scratch model in the purpose to understand how convolutional network work and how to evaluate them.

After that we also built a resnet50 model for production purpose. That model obtains an accuracy of 97% on validation data after a few training epoch. This model has been saved and is the one being used in our website page. (see later)

In the end, we also tested data augmentation on our self-made model.

## Autogluon model
In the dogcat_autogluon notebook we learned how to use an auto ml libraries to solve our problem. That was made during the first days of our project; it gave us knowledge about how to preprocess data, wich model architecture to choose, etc.

## API and website page
After realising our 2 research notebook we decided to push our model into some "production" environment. This is a website api, available at https://dogs-and-cats-recognition.herokuapp.com/. There you can post a picture and get the model prediction.

The api is based on the FASTapi framework with jinja2template for html page.

We then use heroku to host our website. Because we used the free version of heroku the service can crash if there is too many request. This is due to the memory usage limit we have.
