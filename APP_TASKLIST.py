import streamlit as st
from app_taskpage import *
from app_managepage import *
from app_homepage import *
from db_Fntx import creat_table


def main():
    st.header('CRUD (TASK LIST)')
    creat_table()
    menu = ['Home','Task','Manage','About']

    choice = st.sidebar.selectbox('Menu',menu)

    if choice == 'Home':
        run_home()
    elif choice == 'Task':
        run_taskPage()
    elif choice == 'Manage':
        run_manage()
    else:
        pass

if __name__ == '__main__':
    main()
