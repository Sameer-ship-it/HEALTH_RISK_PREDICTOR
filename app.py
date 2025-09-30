import streamlit as st
import pickle
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

model = pickle.load(open("Health_RiskPredictor.pkl","rb"))
encoders = pickle.load(open("label_encoder.pkl","rb"))

st.title("Health Risk Predictor")
age = st.slider("Age(18-80)",18,80,22) #giving limits in age from 18-80, default is 22
diet = st.selectbox("Diet Qualtity",['Poor','Average','Good'])
exercise=st.slider("Exercise Day (Per Week)",0,7,3)
sleep=st.slider("Sleep Hours",2,12,8)
stress= st.selectbox("Stress Level",['Low','Medium','High'])
bmi = st.number_input("BMI",10.0,40.0,22.0)
smoking=st.selectbox("Smoking",['Yes','No'])
alcohol=st.selectbox("Alcohol Consumption",['Low','Medium','High'])
family_history=st.selectbox("Family History of Disease",['Yes','No'])

if st.button("Predict Risk"):
    input_data=[age,
                encoders['diet'].transform([diet])[0],
                exercise,
                sleep,
                encoders['stress'].transform([stress])[0],
                bmi,
                encoders['smoking'].transform([smoking])[0],
                encoders['alcohol'].transform([alcohol])[0],
                encoders['family_history'].transform([family_history])[0],
               ]
    
    prediction = model.predict([input_data])
    probs = model.predict([input_data])

    risk_lebel = encoders['risk_level'].inverse_transform([prediction[0]])[0]
    st.success(risk_lebel)

    #Making visualisation for the output

factors = {
    'Diet': encoders['diet'].transform([diet])[0],
    'Exercise': exercise,
    'Sleep': sleep,
    'Stress': encoders['stress'].transform([stress])[0],
    'BMI': bmi,
}

x = list(factors.keys())
y = list(factors.values())

fig, ax = plt.subplots()
colors = plt.cm.tab10.colors  
ax.pie(y, labels=x, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
ax.set_title("Factors Contributing In Your Health")

st.pyplot(fig)

