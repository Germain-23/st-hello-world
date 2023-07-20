import io
import streamlit as st
import datetime
from PIL import Image
import io
from streamlit_option_menu import option_menu
from pandas import*
import pandas as pd
import numpy as np


with st.sidebar:
    selected = option_menu(
    menu_title="Main Page",
    options=["New Patient", "Statistics",'About us','Logout'],
    icons=["house", "house", "book",'house'],
    menu_icon="cast",
    default_index=0,
    orientation="vertical",
    )
#MAIN PAGE OPTION
if selected == "New Patient":
    col1, col2, col3, col4 = st.columns(4)
    col1.text_input("Name:")
    col1.text_input("First ame:")
    col2.number_input("Tax Number ID :")
    col1.radio("Select  :", ('Age','Birthday','description'))
    col2.date_input("Date de naissance :")
    col2.text_input("Next of kin")
    col1.radio("Your sex",('Male','Female'))

    col3.text_input("Address")
    col3.text_input("City")
    
    col3.number_input("Telephone:")
    col3.text_input("Email:")
    col4.selectbox("Blood Type:",('A+','B+','unknown'))
    col4.multiselect('Marital Status:',
                             ('Celibataire','Maried','Unknown'))
    col4.selectbox('Profession:',('Driver','Student','Worker'))
    col4.text_area("Note:")
    an1,an2=st.columns(2)
    #an1.button('Envoyer')
    #an2.button('Annuler')
   # my_form = st.form(key='form')
    
    st.button(label='Submit')
    st.button(label='Print as pdf')
    #colu = my_form.form_submit_button(label='Annuler')
    

#STATISTICS OPTIONS
#if selected == "Statistics":
    # defining random values in a dataframe using pandas and numpy
    #df = pd.DataFrame(
   # np.random.randn(30, 10),
   # columns=('col_no %d' % i for i in range(10)))
# defining data in table
    #st.table(df)



   
#ABOUT US OPTIONS
if selected == "About us":
    st.header("Hospital Management System (HMS)")
    st.text(" This Project Hospital management Software is a web application for hospital service")
    st.text("for managing all data in hospital : the patient registration, databases dor doctor, ")
    st.text("for managing data for pharmacy , for laboratory .")
    st.text("AS student we are working for developing the open source application for everyone: ")
    st.text("so anyone can copy and share this source code because we have philosophy is free ")
    st.text("code.")
    st.text("")
    
    st.text("")
    st.text("")




# LOGOUT OPTIONS
if selected == "Logout":
    st.snow()
    st.header("❤️❤️❤️❤️❤️❤️THANK for visiting ❤️❤️❤️❤️❤️")






#st.title("NEW PATIENT")
#st.sidebar.button("clic here")
#Image uploader
#st.title("Upload Image")
#image_file = st.file_uploader("Upload Images",
#type=["png","jpg","jpeg"])
#check_details = st.button("Check Details")
#if check_details:
 #if image_file is not None:
 # To See details
    #image_details = {"file_name":image_file.name,
   # "file_type":image_file.type,
    #"file_size":image_file.size}
   # st.write(image_details)
 # To View Uploaded Image
   # image_data = image_file.read()
  #  image = Image.open(io.BytesIO(image_data))
    #st.image(image, width=250)
#else:
   # st.write("No Image File is Uploaded")
#with st.form(key="my_form"):
   
