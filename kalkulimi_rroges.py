import streamlit as st

def pay_weekly(hours, rate):
    pay = hours*rate
    return pay

name = st.text_input("Shkruani emrin")
hours = st.number_input("Shkruani oret")
rate = st.number_input("Shkruani ratingun")
result = pay_weekly(hours,rate)

if st.button('Kalkulo pagen!'):
    st.write(f'{name} your wage is: ',result)


