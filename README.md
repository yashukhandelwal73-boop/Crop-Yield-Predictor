**Project name- Crop Yield Predictor 
**Introduction - This AIML project which uses environmental variables like rainfall , soiltype , weather and temperature to predict yield of crop in tons
**Dataset - 
  - Trained on 1M rows of agricultural data
  - Features used:
  - Rainfall (mm)
  - Weather type
  - Soil type
  - Temperature(C)
  - Target variable: Crop Yield (tons)
**Data Processing -
- True and False were converted to 1 and 0 respectively as soil type and weather type selected (one-hot encoding)
- Negative noise is and uneccessary columns were cleaned from dataset (preprocessing)
- Dummy variables was produced for different soil type and weather 
- For differenr crop type different model was used (ensembling) 
**Model Used -  
- Linear Regression  
- Random Forest Regressor  
**Model Evaluation - 
Random Forest Regressor showed lower RMSE compared to Linear Regression during evaluation, so it was selected as the final model.
