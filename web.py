import streamlit as st
from main import*

st.set_page_config(page_title='RS3 Grand Exchange', layout='centered')

st.title("RS3 Grand Exchange")

items = itemList.keys()
selectedItem = st.selectbox("Search an item", options=items)

button2 = st.button("Look Up Price")
if button2:
    number_with_commas = "{:,}".format(fetchPrice(selectedItem))
    st.markdown("Current price for "+ selectedItem +" is "+ number_with_commas +" GP" + ":moneybag:")
    st.line_chart(fetchGraph(selectedItem))
