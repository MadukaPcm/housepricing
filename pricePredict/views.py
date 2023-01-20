from django.shortcuts import render,redirect
import pickle
from django.conf import settings
import os

from model import *
import numpy as np

#Audio
# import pyttsx3
# engine = pyttsx3.init('sapi5') 
# voices = engine.getProperty('voices')
# rate = engine.getProperty('rate')
# engine.setProperty('rate', rate-20)
# engine.setProperty('voice',voices[0].id)

# Create your views here.
def PredictionPageView(request):
    price = ""
    
    if request.method == "POST":
        try:
            var1 = float(request.POST.get('n1'))
            var2 = float(request.POST.get('n2'))
            var3 = float(request.POST.get('n3'))
            var4 = float(request.POST.get('n4'))
            var5 = float(request.POST.get('n5'))
            
            predict_data = np.array([var1,var2,var3,var4,var5]).reshape(1,-1)
            print(predict_data)
        except Exception as e:
            print(e)
        
        #loading the trained model file from the folder. called Model.
        try:
            path_file = os.path.join(settings.MODELS, 'my_model.pkl')
            with open(path_file, 'rb') as pickled:
                get_my_model = pickle.load(pickled)  
        except Exception as e:
            print(e)
        
        try:
            # filename = 'model/my_model.pkl'
            # get_my_model = pickle.load(open(filename, 'rb'))
            # get_my_model = housepricing.load("model/my_model.pkl")
            # get_my_model = pickle.load('my_model.pkl','rb')
            pred = get_my_model.predict(predict_data)
            pred = round(pred[0])
        except Exception as e:
            print(e)

        try:
            errormsg = "Entered value is out or range."
            pric = "The house predicted price is Tsh: "+str(pred)+"/="
            if pred > 0:
                price = pric
            else:
                price = errormsg
        except Exception as e:
            print(e)
            
    # if price:
    #     speak(price)
    #     speak("Done by Frank Kessi, Thanks")
    
    context = {'result':price}
    return render(request, 'pages/predictionPage.html',context)

# def speak(audio): 
# 	engine.say(audio) 
# 	engine.runAndWait()