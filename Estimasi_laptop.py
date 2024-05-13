import pickle
import streamlit as st

# Load the model
model = pickle.load(open('estimasi_laptop.sav', 'rb'))

# Set up the app title
st.title('Estimasi Harga Laptop')

# Input for memory and internal storage
Inches = st.number_input('Input Inches Laptop')
Ram    = st.number_input('Input Ram Laptop')

predict = ''

# Button to trigger the prediction
if st.button('Estimasi Harga'):
    predict = model.predict([[Inches, Ram]])
    st.write('Estimasi harga Laptop dalam Rp:', predict)