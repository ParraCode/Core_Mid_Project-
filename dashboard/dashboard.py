import streamlit as st
from data.get import get_all_country

st.title('Coviboard Core Core')

country = st.selectbox('Pick one', get_all_country())
