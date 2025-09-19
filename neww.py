import streamlit as st, pandas as pd
import requests
from bs4 import BeautifulSoup
import time

st.header('Indian Trade Dashboard')

ticker = st.sidebar.text_input('Symbol Code','INFY')
exchange = st.sidebar.text_input('Exchange','NSE')

url = f'https://www.google.com/finance/quote/{ticker}:{exchange}'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

current_price = float(soup.find(class_= 'YMlKec fxKbKc').text.strip()[1:].replace(",",""))
previous_price = float(soup.find(class_= 'P6K39c').text.strip()[1:].replace(",",""))
revenue = soup.find(class_='QXDnM').text
opportunities = soup.find(class_='Yfwt5').text
about = soup.find(class_='bLLb2d').text

dict1=dict = {'current Price':current_price,'Previous price':previous_price,'Revenue':revenue,'opportunities':opportunities,'About':about}
df = pd.DataFrame(dict1,index=['Extracted Data']).T
st.write(df)
