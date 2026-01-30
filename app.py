import streamlit as st
from fruit_manager import *

st.title("Gestionnaire de Fruits")

inventaire = ouvrir_inventaire()
prix = ouvrir_prix()
tresorerie = ouvrir_tresor()

st.header("Trésorerie")
st.metric(label="Montant actuel", value=f"{tresorerie:.2f} $")

st.header("Inventaire des Fruits")
st.table(inventaire)
