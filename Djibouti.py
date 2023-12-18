#import the required libraries 

import streamlit as st
import pandas as pd
import numpy as np 
import plotly.express as px  
import json
from streamlit_lottie import st_lottie


st.set_page_config(
    page_title="اســتـبـيـان المجتمع العربي",
    page_icon= "🇺🇳",
    layout='wide'
)

st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)



left_co, cent_co,last_co = st.columns(3)
with last_co:
    st.image("https://i2.wp.com/ummah-futures.net/wp-content/uploads/2019/12/%D8%A7%D9%84%D9%84%D8%AC%D9%86%D8%A9-%D8%A7%D9%84%D8%A7%D9%82%D8%AA%D8%B5%D8%A7%D8%AF%D9%8A%D8%A9-%D9%88%D8%A7%D9%84%D8%A7%D8%AC%D8%AA%D9%85%D8%A7%D8%B9%D9%8A%D8%A9-%D9%84%D8%BA%D8%B1%D8%A8%D9%8A-%D8%A2%D8%B3%D9%8A%D8%A7-1.jpg?w=500&ssl=1")
with left_co:
    st.image("https://m.media-amazon.com/images/I/51P-e1yYpGL._AC_UF894,1000_QL80_.jpg")
st.image("title.PNG")

# Create an empty container
placeholder = st.empty()

actual_email = "Djiboutii"
actual_password = "djiboutii"

# Insert a form in the container
with placeholder.form("login"):
    #st.markdown("#### الرجاء ادخال اسم المستخدم")
    st.markdown('<div style="text-align: right; font-size: 28px; font-weight: bold; color: blue;">الرجاء ادخال اسم المستخدم وكلمة المرور</div>', unsafe_allow_html=True)
    email = st.text_input("Username - اسم المستخدم")
    email = email.lower()
    password = st.text_input("Password - كلمة المرور", type="password")
    password = password.lower()
    submit = st.form_submit_button("Login - تسجيل الدخول")

if submit and email == actual_email and password == actual_password:
    # If the form is submitted and the email and password are correct,
    # clear the form/container and display a success message
    placeholder.empty()
    st.success("تم تسجيل الدخول بنجاح")
    leftt_co, centt_co,lastt_co = st.columns([1,1,2])
    with lastt_co :
        st.title('جيبوتي')
        st.image("SUB HEADER.PNG")
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    with col1:
        st.write("[Population - السكان](https://docs.google.com/spreadsheets/d/1uTGnK11FNjO4kLW4crmGpMak_JBPZJBk/edit?usp=drive_link&ouid=111028980933962818091&rtpof=true&sd=true)")
    with col2:
        st.write("[Labor - العمالة](https://docs.google.com/spreadsheets/d/17G8kQBgcCGAArGyR_d200AxmEYtOuiop/edit?usp=drive_link&ouid=111028980933962818091&rtpof=true&sd=true)")
    with col3:
        st.write("[Poverty - الفقر](https://docs.google.com/spreadsheets/d/138aqu0tKOoHzHZLn7SfhmZjYt2PcoMB-/edit?usp=drive_link&ouid=111028980933962818091&rtpof=true&sd=true)")
    with col4:
        st.write("[Education - التعليم](https://docs.google.com/spreadsheets/d/1E9Qyf1-MrY_Y9XvJs_I8n3KgVBADzWpm/edit?usp=drive_link&ouid=111028980933962818091&rtpof=true&sd=true)")
    with col5:
        st.write("[Culture - الثقافة](https://docs.google.com/spreadsheets/d/1p6enZxH2JnE_Rz-8LzzVYQertHJImsDP/edit?usp=drive_link&ouid=111028980933962818091&rtpof=true&sd=true)")
    with col6:
        st.write("[Health - الصحة](https://docs.google.com/spreadsheets/d/1NgYkl28FqsD9qkPuVqkoYE0J0b3n3m-R/edit?usp=drive_link&ouid=111028980933962818091&rtpof=true&sd=true)")
    with col7:
        st.write("[Housing Conditions - المساكن](https://docs.google.com/spreadsheets/d/10WXo1MyEdiWQwee9d3XsDlJzBJozGsUa/edit?usp=drive_link&ouid=111028980933962818091&rtpof=true&sd=true)")   

    st.title("Questionnaires in English Language are availble below:")

    
    coll1, coll2, coll3, coll4, coll5, coll6, coll7 = st.columns(7)
    with coll1:
        st.write("[Population - السكان](https://docs.google.com/spreadsheets/d/1za0M8e5F64GqHl0BirTHnIC_KABxEBK9/edit?usp=drive_link&ouid=111028980933962818091&rtpof=true&sd=true)")
    with coll2:
        st.write("[Labor - العمالة](https://docs.google.com/spreadsheets/d/1fG3F1vPMe1Hwcyq08DbsR4FC1SAyrHiT/edit?usp=drive_link&ouid=111028980933962818091&rtpof=true&sd=true)")
    with coll3:
        st.write("[Poverty - الفقر](https://docs.google.com/spreadsheets/d/1BdSGNN4i4y0--74NMptt-fle4IjckWcr/edit?usp=drive_link&ouid=111028980933962818091&rtpof=true&sd=true)")
    with coll4:
        st.write("[Education - التعليم](https://docs.google.com/spreadsheets/d/1LDdYjllR3aIBbt_srIJMNm7DDUMbdPbx/edit?usp=drive_link&ouid=111028980933962818091&rtpof=true&sd=true)")
    with coll5:
        st.write("[Culture - الثقافة](https://docs.google.com/spreadsheets/d/1JpNW2NlFszDKPsBpnfNs7dEeBA-4xFVc/edit?usp=drive_link&ouid=111028980933962818091&rtpof=true&sd=true)")
    with coll6:
        st.write("[Health - الصحة](https://docs.google.com/spreadsheets/d/1Rq9R1rCCaHB8y3XpV7dlWOegs8tcCsi4/edit?usp=drive_link&ouid=111028980933962818091&rtpof=true&sd=true)")
    with coll7:
        st.write("[Housing Conditions - المساكن](https://docs.google.com/spreadsheets/d/1q3ViZq4kNhq53NVXU9QnAm7Sdyd_Pn1e/edit?usp=drive_link&ouid=111028980933962818091&rtpof=true&sd=true)")

elif submit and email != actual_email and password != actual_password:
    st.error("هناك خطأ في اسم المستخدم او كلمة المرور، الرجاء المحاولة من جديد")
    
else:
    pass



#edit footer
page_style= """
    <style>
    footer{
        visibility: visible;
        }
    footer:after{
        content: 'Developed by ESCWA Statistics, Information Society and Technology Cluster';
        display:block;
        position:relative;
        color:#1e54e4;
    }
    </style>"""

st.markdown(page_style, unsafe_allow_html=True)
