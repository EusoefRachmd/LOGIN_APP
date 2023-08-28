import streamlit as st

import pandas as pd

import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()

def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS usertable(username TEXT, password TEXT)')

def add_userdata(username,password):
    c.execute('INSERT INTO usertable(username,password) VALUES (?,?)',(username,password))
    conn.commit()

def login_user(username,password):
    c.execute('SELECT * FROM usertable WHERE username =? AND password =?',(username,password))
    data = c.fetchall()
    return data


def main():

    st.title('Simple Login App')

    menu = ['Home', 'Login', 'Signup']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Home':
        st.subheader('Home')

    elif choice == 'Login':
        st.subheader('Login Section')

        username = st.sidebar.text_input('Username')
        password = st.sidebar.text_input('Password', type='password')
        if st.sidebar.checkbox('Login'):
            # if password == '12345':

            create_usertable()
            result = login_user(username,password)
            if result:

                st.success('Loged in as {}'.format(username))

                task = st.selectbox('Task', ['Addpost', 'Analytics', 'Profiles'])
                if task == 'Addpost':
                    st.subheader('Add Your Post')

                elif task == 'Analytics':
                    st.subheader('Analytics')

                # elif task == 'profiles':
                #     st.subheader('user profile')    
                #     user_result = view_all_users()
                #     clean_db = pd.DataFrame(user_result, columns=['username', 'password'])
                #     st.dataframe(clean_db)


            else:
                st.warning('Incorrect Usename/Password')             

    elif choice == 'Signup':
        st.subheader('Create New Account')
        new_user = st.text_input('Username')
        new_password = st.text_input('Password',type='password')

        if st.button('Signup'):
            create_usertable()
            add_userdata(new_user,new_password)
            st.success('You Have Successfully Create An Valid Account')
            st.info('go to login menu to login')

if __name__ == '__main__':
    main()
              