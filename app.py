import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
from PIL import Image

model = pickle.load(open('ML_MODEL_3.sav', 'rb'))

st.title('Bulldozer Auction Price')
st.sidebar.header('Bulldozer Data')

def user_report():
    SalesID = st.sidebar.slider('SalesID', 1227829,1228198,5)
    MachineID = st.sidebar.slider('MachineID', 1006309,103626,5)
    datasource = st.sidebar.slider('Data source', 121,149,1)
    auctioneerID = st.sidebar.slider('auctioneerID', 10,100,1)
    YearMade =  st.sidebar.slider('YearMade', 2004,2012,1000)
    saleyear =  st.sidebar.slider('Saleyear',2004,2012,2000)    


    user_report_data= {
        'SalesID': SalesID,
        'MachineID': MachineID,
        'datasource' : datasource,
        'auctioneerID' : auctioneerID,
        'YearMade' : YearMade,
        'saleyear' :  saleyear
     }

    report_data = pd.DataFrame(user_report_data, index=[0])
    return report_data



user_data = user_report()
st.header('Auction Data')
st.write(user_data)

price= model.predict(user_data)
st.subheader('Price of the Bulldozer')
st.subheader('$'+ str(np.round(price[0],2)))
