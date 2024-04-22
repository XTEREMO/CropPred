import numpy as np
import pickle
import streamlit as st


model = pickle.load(open('Crop_Recommendation.pkl','rb'))

def prediction(N,P,K,Temp,Humidity,Ph,Rain):
    return model.predict([[N,P,K,Temp,Humidity,Ph,Rain]])

def  main():
    st.title("Crop Pred")
    N = st.text_input("Nitrogen :","")
    P = st.text_input("Phosphorus :","")
    K = st.text_input("Potassium :","")
    Temp = st.text_input("Temperature :","")
    Humidity = st.text_input("Humidity :","")
    Ph = st.text_input("Ph :","")
    Rain = st.text_input("RainFall :","")
    crop_dicts = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
                 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
                 14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
                 19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}
    if st.button("Predict"):
        result = prediction(N,P,K,Temp,Humidity,Ph,Rain)
        st.success(crop_dicts[result[0]])
    
    

if __name__ == '__main__' :
    main()
    