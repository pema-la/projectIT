
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading

diabetes_model = pickle.load(open('C:/Users/tone/Desktop/projectITS/saved models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/tone/Desktop/projectITS/saved models/heart_disease_model.sav','rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction'],
                          icons=['activity','heart'],
                          default_index=0)
    
    
# Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction')
    
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
    
    
    # code 
    diab_diagnosis = ''
    
    
    if st.button('Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'Sorry! You have diabetes'
        else:
          diab_diagnosis = "Good News! You don't have diabetes"
        
    st.success(diab_diagnosis)




# Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    st.title('Heart Disease Prediction ')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age') 
        
    with col2:
        sex = st.text_input('Sex') 
        
    with col3:
        cp = st.text_input('Chest Pain types') 
        
    with col1:
         thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col2:
         exang = st.text_input('Exercise Induced Angina')
        
    with col3:
         oldpeak = st.text_input('ST depression induced by exercise') 

    with col1:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col2:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col3:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # Prediction
    heart_diagnosis = ''
    
    if st.button('Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, thalach, exang, oldpeak, slope, ca, thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'Sorry! You have heart disease'
        else:
          heart_diagnosis = " Good News! You don't have heart disease"
        
    st.success(heart_diagnosis)
        

