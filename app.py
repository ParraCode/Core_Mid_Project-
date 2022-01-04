import streamlit as st
from multiapp import MultiApp
from apps import dashboard_variant, dashboard_covid

app = MultiApp()

st.markdown("""
# Multi-Page App
""")

# Add all your application here
app.add_app("Dashboard of Covid Country Vs Country", dashboard_covid.app)
app.add_app("Dashboard of Variants in different Country", dashboard_variant.app)
# The main app
app.run()

