# Singapore-Realstate-price-prediction 

The main of this project is to predict the price of the singapore realesate house price . So lets see the process of this project.
### Overflow
#### 1.Data collection:
1. Data is collected from the this website https://beta.data.gov.sg/collections/189/view.
2. After collecting the data we have to import the required libraries and then load the csv data into jupyter notbook
3. Data preprocessing like treating the null values, using statistical methods like IQR to treat the outliers in the dataset
#### 2.Data visualization:
1. Using Data visualization technique to find the pattern and design 
2. we have to perform two types of Data visualization one is distribution of feature and distribution of feature vs target
3. so finally based on the visualization we can able to see the patters and trends
#### 3. Encoding:
1. Basically machine learning packages performs on number so we have to encode the string datatypes
2. some of the encoding techniques are map function, label encoding and one hot encoding
#### 4. Building machine learning modles:
1. House price prediciton is the regression problem so we have to try all the regression machine learning models
2. We have to try Linear regression, Decision tree regressor, Random forest regressor and xgboost
3. After build the model we have to evaluate the model prediction for regression problem evalution metrics are r2 score
4. For this problem i am using rmse value to find the best rmse value we have to calculate the rmse score for each and evey model both train and test dataset
5. we choose the best model based on the difference between the train and test which model has the low difference we can consider that specific model as the best model.
6. After that store the best model using the pickle library
#### 5. Streamlit:
1. Using streamlit we can create the user interface for the house price prediction project
2. Loading the machine learning model using pickle file
3. we can see the output by give some of the input the model predicit the output based on our input
#### model deployment: 
1. Once we finished the Streamlit for user interface we use the render application for model deployment. So the user will just click the link provide by the render apllicaiton for our project we can share it to the user and every one uses the project to predict the house price.

#### check this link live Ml deployment of machine learning project https://singaporepricepredicition.onrender.com
