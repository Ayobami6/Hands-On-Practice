import streamlit as st
import time


st.title("Welcome To Body Mass Index Calculator\n Programed By Ayobami Alaran")
st.text("Instructions\nIf you have no idea of your height and weight figures please go back to get it\nand come back here to get your BMI\nthank you. ")

st.subheader("Your height")
height = st.number_input('What is your height in cm?', 10, 300)
st.write(f'You height is' + " " + str(height) + 'cm')
st.subheader("Your weight")
weight = st.number_input('What is your weight in kg?', 10, 150)
st.write(f'You weight is' + " " + str(weight) + 'kg')


BMI = weight/((height/100) ** 2)
rounded_Bmi = round(BMI, 1)
if st.button('Calculate BMI'):
    with st.spinner('Calculating........'):
        time.sleep(0.5)
    st.write(f"Your BMI is" + " " + str(rounded_Bmi) + "kg/m^2")
    if rounded_Bmi <= 30:
        st.write('You dey Kampe!')
    else:
        st.write('Your BMI is high, You need to start working out!')


