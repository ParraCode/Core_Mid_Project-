import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from utils.process_data import *

from dashboard.data.get_data_covid import *

def app():

     # ---------------------------------------------------------------------------------------------------------------------------------------
    st.set_page_config(page_title="Compare Shows", layout="wide") 

    # Division en columnas 

    col1, col2= st.columns(2)

    # ---------------------------------------------------------------------------------------------------------------------------------------

    # Titulo

    col1.title('Variants')

    # ---------------------------------------------------------------------------------------------------------------------------------------
