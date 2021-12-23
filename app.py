#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 01:29:06 2021

@author: Abhinav Reddy Mandli
"""

from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import sklearn
import json
import pickle

app=Flask(__name__,template_folder='template')
                                                
model = pickle.load(open('classifier.pkl','rb'))
                                                
@app.route('/',methods=['GET'])
def home():
    return render_template('/index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        
        Age = int(request.form['Age'])
        
        RestingBP = int(request.form['RestingBP'])
        
        Cholesterol = int(request.form['Cholesterol'])
        
        FastingBS= request.form['FastingBS']
        if(FastingBS == 'Yes'):
            FastingBS =1
        elif(FastingBS == 'No'):
            FastingBS = 0
        
        MaxHR= int(request.form['MaxHR'])
        
        Oldpeak_reciprocal= float(request.form['Oldpeak_reciprocal'])
        
        #Taking inputs for cholesterol type
        ChestPaintype = request.form['ChestPainType']
        
        if(ChestPaintype == 'TA'):
            ChestPainType_ATA= 0
            ChestPainType_NAP= 0
            ChestPainType_TA = 1
        elif(ChestPaintype=='NAP'):
            ChestPainType_ATA = 0
            ChestPainType_NAP = 1
            ChestPainType_TA = 0
        elif(ChestPaintype == 'ATA'):
            ChestPainType_ATA = 0
            ChestPainType_NAP = 0
            ChestPainType_TA =   1
        elif(ChestPaintype == 'ASY'):
            ChestPainType_ATA = 0
            ChestPainType_NAP = 0
            ChestPainType_TA =   0
            
        #Taking inputs for Resting ECG
        RestingECG = request.form['RestingECG']
        
        if(RestingECG == 'Normal'):
            RestingECG_Normal = 1
            RestingECG_ST=0
        elif(RestingECG== 'ST'):
            RestingECG_Normal = 0
            RestingECG_ST= 1
        elif(RestingECG == 'LVH'):
            RestingECG_Normal = 0
            RestingECG_ST= 0
           
        #Taking input for exercise Angina
        ExcerciseAngina = request.form['ExcerciseAngina']
    
        if(ExcerciseAngina == 'Yes'):
            ExerciseAngina_Y = 1
        elif(ExcerciseAngina== 'No'):
            ExerciseAngina_Y = 0
        
        #Taking inputs for ST feature
        ST_Slope = request.form['ST_Slope'] 
        
        if(ST_Slope == 'Flat'):
            ST_Slope_Flat = 1
            ST_Slope_Up = 0
        elif(ST_Slope== 'Up'):
            ST_Slope_Flat = 0
            ST_Slope_Up = 1
        elif(ST_Slope== 'Down'):
            ST_Slope_Flat = 0
            ST_Slope_Up = 0
            
        # Taking inputs for sex feature
        Sex = request.form['Sex']  
        if(Sex == 'Male'):
            Sex_M=1
        elif(Sex== 'Female'):
            Sex_M=0
        
        features_input = np.array([Age, RestingBP, Cholesterol, FastingBS, MaxHR, Oldpeak_reciprocal, ChestPainType_ATA, ChestPainType_NAP, ChestPainType_TA, RestingECG_Normal, RestingECG_ST, ExerciseAngina_Y, ST_Slope_Flat, ST_Slope_Up, Sex_M])
        
        features_input = features_input.reshape(1,-1)
        
        prediction = model.predict(features_input)
        
            
        if prediction == 1:
            return render_template('/index.html',prediction_text = "HEART DISEASE CONDITION EXISTS")
        else:
            return render_template('/index.html',prediction_text = "HEART DISEASE CONDITION DOESN'T EXIST")
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
           
    
            
        
