# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 21:34:11 2022

@author: Ayo
"""

print("Welcome To Body Mass Index Calculator\nProgram, Programed By Ayobami Alaran")
print("Instructions\nIf you have no idea of your height and weight figures please go back to get it\nand come back here to get your BMI\nthank you. ")

start = input("Do you wish to continue? Y/N:")

if start == "Y":
    print("continue")
   
    height = int(input("What is your height in cm:"))
    weight = int(input("What is your current weight In Kg:"))
    BMI = weight/((height/100) ** 2)
    
    rounded_Bmi = round(BMI, 1)
    
    print(f"Your BMI is" + " " + str(rounded_Bmi) + "kg/m^2")
    print("You dey Kampee")

print("Goodbye!")
