#import libraries
import streamlit as st
import pickle 
import sklearn  
import pandas as pd 
import numpy as np 
from sklearn.linear_model import LinearRegression
from PIL import Image 

#loading the machine learning model from pickle
model=pickle.load(open('model_pickle','rb'))


#streamlit title
st.title('Singapore Realstate Price Detection')


month=st.selectbox('Enter Month :',(1,2,3,4,5,6,7,8,9,10,11,12))
town=st.selectbox('Choose Town:',('punggol','bukit timah','sengkang','bishan','pasir ris','sembawang','bukit merah','choa chu kang','central area',
                                  'marine parade','tampines','bukit panjang','serangoon','kallang/whampoa','hougang','woodlands','toa payoh','queenstown',
                                  'jurong west','clementi','jurong east','bukit batok','bedok','geylang','yishun','ang mo kio','lim chu kang'))  
flat_type=st.selectbox('Choose Room_Type:',('1 room','2 room','3 rooom','4 room','5 room','executive','multi generation'))
storey_range=st.selectbox('choose sotrey_range',('04 TO 06','07 TO 09','01 TO 03','10 TO 12','13 TO 15','16 TO 18','19 TO 21','22 TO 24','25 TO 27',
                                                    '01 TO 05','06 TO 10','28 TO 30','11 TO 15','31 TO 33','34 TO 36','37 TO 39','16 TO 20','40 TO 42',
                                                    '21 TO 25','43 TO 45','46 TO 48','26 TO 30','49 TO 51','36 TO 40','31 TO 35'))
Floor_area_sqm=st.text_input('Enter the area sqm value:')
Flat_model=st.selectbox('Choose the Flat_mode',('Model A','Improved','New Generation','Simplified','Premium Apartment','Standard','Apartment',
                                                'Maisonette','Model A2','DBSS','Model A-Maisonette','Adjoined flat','Terrace','Multi Generation',
                                                'Type S1','Type S2','Improved-Maisonette','2-room','Premium Apartment Loft','Premium Maisonette','3Gen'))
Lease_commence_date=st.text_input('Enter Lease Commence Year:')
year=st.text_input('Enter Year')
House_age=st.text_input('Enter Your House Age')            
df=pd.DataFrame({'month':[month],
      'Town': [town],
      'Flat_Type': [flat_type],
      'Storey_Range': [storey_range],
      'Floor_Area_Sqm': [Floor_area_sqm],
      'Flat_Model': [Flat_model],
      'Lease_commence_date':[Lease_commence_date],
      'Year':[year],
      'House_age':[House_age]},index=[0])


#encoding for categorical values:
df['Town']=df['Town'].map({'punggol':0,'bukit timah':1,'sengkang':2,'bishan':3,'pasir ris':4,'sembawang':5,'bukit merah':6,'choa chu kang':7,
                           'central area':8,'marine parade':9,'tampines':10,'bukit panjang':11,'serangoon':12,'kallang/whampoa':13,
                           'hougang':14,'woodlands':15,'toa payoh':16,'queenstown':17,'jurong west':18,'clementi':19,'jurong east':20,
                           'bukit batok':21,'bedok':22,'geylang':23,'yishun':24,'ang mo kio':25,'lim chu kang':26})
df['Flat_Type']=df['Flat_Type'].map({'multi generation':0,'executive':1,'5 room':2,'4 room':3,'3 room':4,'2 room':5,'1 room':6})
df['Storey_Range']=df['Storey_Range'].map({'49 TO 51':0,'46 TO 48':1,'43 TO 45':2,'40 TO 42':3,'37 TO 39':4,'34 TO 36':5,'31 TO 33':6,
                                           '36 TO 40':7,'28 TO 30':8,'31 TO 35':9,'26 TO 30':10,'21 TO 25':11,'25 TO 27':12,
                                           '16 TO 20':13,'22 TO 24':14,'11 TO 15':15,'19 TO 21':16,'06 TO 10':17,'01 TO 05':18,'16 TO 18':19,
                                           '13 TO 15':20,'10 TO 12':21,'07 TO 09':22,'04 TO 06':23,'01 TO 03':24})
df['Flat_Model']=df['Flat_Model'].map({'Type S2':0,'Type S1':1,'Premium Apartment Loft':2,'DBSS':3,'3Gen':4,'Premium Maisonette':5,'Multi Generation':6,
                                       'Terrace':7,'Apartment':8,'Maisonette':9,'Adjoined flat':10,'Model A-Maisonette':11,
                                       'Improved-Maisonette':12,'Premium Apartment':13,'Improved':14,'Model A':15,'Model A2':16,
                                       '2-room':17,'Standard':18,'Simplified':19,'New Generation':20})

st.write(df)
if st.button('predict'):
    makeprediction = model.predict(df)
    output=round(makeprediction[0])
    output_in_lakhs=output/10000
    formatted_output = '{:.2f} dollar'.format(output_in_lakhs)
    st.success('You can sell your house for {}'.format(formatted_output)) 

