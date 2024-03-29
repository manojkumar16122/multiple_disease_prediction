# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 16:47:31 2022

@author: Acer
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav','rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav','rb'))
autism_model = pickle.load(open('autism_model.sav','rb')) 



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction Using ML',                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction',
                           'Autism Prediction'
                          ,'About us','Contact'],
                          icons = ['activity','suit-heart','person-circle','caret-right-square-fill','house','cast'],
                          default_index=0)
                   
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)
    
if (selected == 'Autism Prediction'):

st.title('Autism Disease Prediction Using ML')

A1_Score = st.text_input('Whether the child looks at you when you call his/her name? (Yes-1/No-0)')
A2_Score = st.text_input('How easy it is for you to get eye contact with the child? (Yes-1/No-0)')
A3_Score = st.text_input('Does your child point to indicate that he/she wants something? (Yes-1/No-0)')
A4_Score = st.text_input('Does your child point to share interest with you? (Yes-1/No-0)')
A5_Score = st.text_input('Does your child pretend? (Yes-1/No-0)')
A6_Score = st.text_input('Does your child follow when you are looking? (Yes-1/No-0)')
A7_Score = st.text_input('If you or someone else in the family is visibly upset, does your child show signs of wanting to comfort them? (Yes-1/No-0)')
A8_Score = st.text_input('Does your child talk back when you talk? (Yes-1/No-0)')
A9_Score = st.text_input('Does your child use simple gestures? (Yes-1/No-0)')
A10_Score = st.text_input('Does your child stare at nothing with no apparent purpose? (Yes-1/No-0)')
age = st.text_input('Age')
jundice = st.text_input('Whether the child was born with jaundice? (Yes-1/No-0)')

autism_diagnosis = ''

if st.button("AUTISM TEST RESULT"):
    # Convert input values to integers
    input_data = [
        int(A1_Score),
        int(A2_Score),
        int(A3_Score),
        int(A4_Score),
        int(A5_Score),
        int(A6_Score),
        int(A7_Score),
        int(A8_Score),
        int(A9_Score),
        int(A10_Score),
        int(age),
        int(jundice)
    ]

    # Predict autism using your model
    autism_prediction = autism_model.predict([input_data])

    if autism_prediction[0] == 1:
        autism_diagnosis = "The person has a risk of Autism"
    else:
        autism_diagnosis = "The person does not have Autism Disease"
        st.success(autism_diagnosis)
        st.markdown("For further consultation, kindly use:")
        st.markdown("1. ABA Therapy Centre for Autism link: [http://www.youcanautism.com/](http://www.youcanautism.com/)")
        st.markdown("2. Third Eye - A learning center for Autism Link: [http://www.thirdeyecenter.org/](http://www.thirdeyecenter.org/)")
        st.markdown("3. Vatsalyam Centre For Autism Link: [http://www.vatsalyam.in/](http://www.vatsalyam.in/)")
        st.markdown("4. Sparks Vidyalaya Link: [http://sparksautismschool.com/](http://sparksautismschool.com/)")

if (selected == 'About us'):
    st.title('About us')
    st.text('This application is designed to predict whether a person has the listed multiple disease or not.')
    st.text('It works by the principle of applying machine learning techniques. When the user')
    st.text('gives the inputs regarding the person, it gets tested by the machine learning model.')
    st.text('The proposed model is based on the Support Vector Machine.The input data gets tested')
    st.text(' and predicts the result.')
if (selected == 'Contact'):
    st.title('FURTHER CONTACT DETAILS')
    st.text('For further details contact us at mkinfotechology2022@gmail.com')
    st.text('Developed by Manojkumar V')

    
