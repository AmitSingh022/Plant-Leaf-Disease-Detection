from django.http import HttpResponse
from django.shortcuts import render
from service.models import Service
from contactForm.models import ContactForm


import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from keras import preprocessing
import cv2

 # Load model
cnn = tf.keras.models.load_model('trained_plant_disease_model9.keras')

def homepage(request):
     serviceData= Service.objects.all().order_by('-service_title')
     dtat={
          'data': 'this is home page',
          'servicedata':serviceData,
     }
     return render(request,"index.html",dtat)
def aboutus(request):
     return render(request,"about.html")
def imageForm(request):
     try:
         if request.method=="POST":
           image=request.POST.get('image')
     except:
         pass
     return render(request,"contact.html",{'image',image})
def contactus(request):
     try:
      model_prediction = None  
      if request.method=="POST":

           image_file=request.FILES.get('image')
           if image_file:

            # Save to database
             en = ContactForm(
              
                image=image_file
             )
             en.save()
             image_path = en.image.path 

            # Preprocess image
             image = tf.keras.preprocessing.image.load_img(image_path, target_size=(128,128))
             input_arr = tf.keras.preprocessing.image.img_to_array(image)
             input_arr = np.array([input_arr])
             predictions = cnn.predict(input_arr)
             result_index = np.argmax(predictions)
             print(result_index)
             class_name=['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy']
             model_prediction = class_name[result_index]
# Output predictions
     except Exception as e:
          print("Error:", e) 
     imge=ContactForm.objects.last()
     data={
               'im': imge,
               'prediction': model_prediction
           }
     return render(request,"contact.html",data)
