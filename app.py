import sys
import streamlit as st
import numpy as np
import pandas as pd
import joblib 
import plotly.express as px
@st.cache_resource
def load_models():
    m1 = joblib.load('rice.joblib')
    m2 = joblib.load('barley.joblib')
    m3 = joblib.load('cotton.joblib')
    m4 = joblib.load('wheat.joblib')

    
    return m1, m2, m3, m4
loaded_model1, loaded_model2, loaded_model3, loaded_model4 = load_models()
@st.cache_resource
def load_data():
   n1=joblib.load("cotton_data.joblib")
   n2=joblib.load("rice_data.joblib")
   n3=joblib.load("wheat_data.joblib")
   n4=joblib.load("barley_data.joblib")
   return n1,n2,n3,n4
dfc,dfr,dfw,dfb=load_data()
st.title("AGRO PREDICTOR")

Dict_test = {
    "Rainfall_mm": [0],
    "Temperature_Celsius": [0],
    "Fertilizer_Used": [0],
    "Irrigation_Used": [0],
    "Weather_Condition_Cloudy": [0],
    "Weather_Condition_Rainy": [0],
    "Weather_Condition_Sunny": [0],
    "Soil_Type_Chalky": [0],
    "Soil_Type_Clay": [0],
    "Soil_Type_Loam": [0],
    "Soil_Type_Peaty": [0],
    "Soil_Type_Sandy": [0],
    "Soil_Type_Silt": [0]
}
col1, col2 = st.columns(2)
j=True 
with col1:

    st.subheader("Soil & Farming")
    soil = st.selectbox("Soil Type", ["Chalky", "Clay", "Loam", "Peaty", "Sandy", "Silt"])
    Dict_test[f"Soil_Type_{soil}"]=[1]
    area=st.number_input("Enter the area of your farm (m2) ")
    if area<=0:
     st.warning("Area cannot be negative or zero ")
  

       
    fert = st.radio("Fertilizer Used?", ["Yes", "No"])
    if fert == "Yes":
      Dict_test["Fertilizer_Used"] = [1]
    irr = st.radio("Irrigation Used?", ["Yes", "No"])
    if irr == "Yes":
      Dict_test["Irrigation_Used"] = [1]


with col2:
    st.subheader(" Weather Conditions")
    weather = st.selectbox("Weather", ["Cloudy", "Rainy", "Sunny"])
    Dict_test[f"Weather_Condition_{weather}"] = [1]
    rainfall = st.slider("Rainfall (mm)", 0, 1000, 700)
    Dict_test["Rainfall_mm"]=[rainfall]
    temp = st.slider("Temperature (°C)", 0, 50, 25)
    Dict_test["Temperature_Celsius"]=[temp]
with st.sidebar:
    st.title("AGRO PREDICTOR")
    st.divider() 
    st.info(f"Name: Yashu\n\nEnroll No: 01176802725\n\nBranch: CSE-Evening")
if  area   > 0:
  if st.button("Predict") :
   Dict_test=pd.DataFrame(Dict_test)
   y_pred1=loaded_model1.predict(Dict_test)
   y_pred2=loaded_model2.predict(Dict_test)
   y_pred3=loaded_model3.predict(Dict_test)
   y_pred4=loaded_model4.predict(Dict_test)

   predictions = [y_pred1[0], y_pred2[0], y_pred3[0], y_pred4[0]]
   crop_names = ["Rice", "Barley", "Cotton", "Wheat"]
 
   best_index = np.argmax(predictions)
   best_crop = crop_names[best_index]
   best_yield = predictions[best_index]
 
   st.success(f"The best crop to grow is -{best_crop}- with a predicted yield of {best_yield:.2f} ton per hectare")
   calculation=[round(float((y_pred1[0]/10000)*area),8),round(float((y_pred2[0]/10000)*area),8),round(float((y_pred3[0]/10000)*area),8),round(float((y_pred4[0]/10000)*area),8)]
   results_df = pd.DataFrame({"Crop": crop_names, "Predicted Yield Per Ton Hectare": predictions,f"Total Yield Of Your Farm Of Area {round(float(area),2)} m2 In Tons":calculation})
   st.table(results_df)
   prediction_frame={"Crops":["Rice", "Barley", "Cotton", "Wheat"],

                    "Predictions":[round(float(y_pred1[0]),2), round(float(y_pred2[0]),2), round(float(y_pred3[0]),2),round(float( y_pred4[0]),2)]}

   graph_plot=pd.DataFrame(prediction_frame) 
   fig=px.line( graph_plot,x="Crops", 
   y="Predictions", 

   title="Comparitive yield comparision"
 )      
 
   st.plotly_chart(fig)

