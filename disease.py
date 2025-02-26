import pickle
import streamlit as st 
from streamlit_option_menu import option_menu

#loading a model
#C:/Users/janag/Desktop/heart wedsite/heart_desiase_model_sav,heart_desiase_model_sav
heart_model=pickle.load(open("heart_desiase_model_sav","rb"))
#"C:\Users\janag\Desktop\multiple disease\heart deasis\heart_model_sav"
diabetes=pickle.load(open("diabetes_prediction_model_sav","rb"))
#heart_desiase_model_sav
#diabetes_prediction_model_sav
#navigation bars

with st.sidebar:
    selected=option_menu("Multiple diases prediction system using ml",["Heart disease prediction",
                                                              "Diabetes prediction"],
                                                              icons=["heart","activity"],
                                                              default_index=0)

if selected == "Heart disease prediction":
    st.title("Heart disease prediction using michane learning algorithm")
    col1,col2,col3=st.columns(3)
    with col1:
        age=st.text_input("Age of the person")

    with col2:
        gender=st.text_input("Gender of the person ")

    with col3:
        cp=st.text_input("enter chest pain")

    with col1:
        trestbps=st.text_input("enter resting blood pressure value")

    with col2:
        chol=st.text_input("enter serum cholestorial vlaue")

    with col3:
        blood_sugar=st.text_input("enter blood sugar value")

    with col1:
        ecg=st.text_input("enter restecg value")

    with col2:
        thalach=st.text_input("enter thalach value")

    with col3:
        exang=st.text_input("enter exang value")

    with col1:
        oldpeak=st.text_input("enter old peak value")

    with col2:
        slope=st.text_input("enter slope value")

    with col3:
        ca=st.text_input("enter ca value")

    with col1:
        thal=st.text_input("enter thal  value")

    heart=""
    if st.button("Make a prediction"):
        heart=heart_model.predict([[age,gender,cp,trestbps,chol,blood_sugar,ecg,thalach,exang,oldpeak,slope,ca,thal]])
        if heart[0]==1:
            heart="The Person having a Heart Disease"
        else:
            heart="The Person Do Not Having Heart Disease"
    st.success(heart)


if selected == "Diabetes prediction":
    st.title("Diabetes prediction using michane learning algorithm")


    col1,col2,col3=st.columns(3)
    with col1:
        pregnancies=st.text_input("no of pregnancies")
    
    with col2:
        glucose=st.text_input("Glucose level")
    with col3:
        bloodpresure=st.text_input("Blood Presure value")
    with col1:
        skinthickness=st.text_input("Skin Thickness value")
    with col2:
        insulin=st.text_input("Insulin level")
    with col3:
        bmi=st.text_input("BMI value")
    with col1:
        DiabetesPedigreeFunction=st.text_input("Diabetes Pedigree Function value")
    with col2:
        age=st.text_input("Age of the person")

    dai_predict=""
    if st.button("Make a prediction"):
        dai_predict=diabetes.predict([[pregnancies,glucose,bloodpresure,skinthickness,insulin,bmi,DiabetesPedigreeFunction,age]])

        if dai_predict[0]==1:
            dai_predict="Person having a Diabetes"
        else:
            dai_predict="Person do not having a Diabetes"
    st.success(dai_predict)