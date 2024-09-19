import streamlit as st
import csv
import pandas
import time
import random


st.set_page_config(page_title='Hypixel Tracker', layout="wide")

user = []
seeds= []

data = ''

st.title("Hypixel Task Manager")

sign_up, login = st.columns(2)

df = pandas.read_csv('Accounts.csv')

for i, row in df.iterrows():
    user.append(row['user'])
    seeds.append(row['seed'])

with sign_up:
    sign_up_form = st.form('sign_up_form')
    with sign_up_form:
        st.header('Sign Up')
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')
        confirm_password = st.text_input('Confirm Password', type='password')
        button = st.form_submit_button('submit')
        if button:
            if username.lower() not in user and password == confirm_password:
                # generates a unique seed for user
                seed = random.randint(10000,100000)
                while seed in seeds:
                    seed = random.randint(10000, 100000)

                # prepares user information to write to csv
                user_info = [username.lower(), str(hash(password)), seed]

                # writes user information to csv file
                with open('Accounts.csv', 'a') as file:
                    file_object = csv.writer(file)
                    file_object.writerow(user_info)

                st.write("Account Created!")
            # Error handling user inputs
            elif username.lower() in user:
                st.write("Username is taken.")
            elif password != confirm_password:
                st.write("Passwords do not match.")

with login:
    login_form = st.form('login_form')
    with login_form:
        st.header('Login')
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')
        button = st.form_submit_button('submit')

        if button:
            with open('Accounts.csv','r') as file:
                for line in file.readlines():
                    database_username, database_password, database_seed = line.split(',')

                    if database_username == username.lower():
                        if database_password == str(hash(password))[:53]:
                            data = str(database_seed)
                            result = f"logged in as {username}"

                        else:
                            result = "Credentials are incorrect"
                    else:
                        result = "Credentials are incorrect"

            st.write(result)