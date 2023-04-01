import streamlit  as st
import pandas as pd
from db_Fntx import *

def run_home():
    st.subheader('Home Page')

    choice = st.sidebar.selectbox('submenu',['My Tasks','Search'])

    
    with st.expander("View All Tasks"):
            view_data = view_all_tasks()
            df_view_data = pd.DataFrame(view_data,columns=['Task Assigned To','Task Details','Status','Due Date'])
            st.dataframe(df_view_data,use_container_width=True)

    if choice == 'My Tasks':
          
        c1,c2 = st.columns([1,3])

        with c1:
            st.info("Task List")
            task_decsription = [i[0] for i in view_unique_task_name()]
            selected_task = st.selectbox('Your Task',task_decsription)
        with c2:
            st.info("Task Details")   
            task_result = get_task_by_task_name(selected_task)
            #st.write(task_result)
            Task_Assigned_To = task_result[0][0]
            Task_Details = task_result[0][1]
            Status = task_result[0][2]
            Due_Date = task_result[0][3]

            st.text('Task Assigned To : {}'.format(Task_Assigned_To),)
            st.text('Task Details : {}'.format(Task_Details))
            st.text('Status : {}'.format(Status))
            st.text('Due Date : {}'.format(Due_Date))

    else:
        st.subheader('Search')

        search_term = st.text_input('Search Term')
        search_choice = st.radio('Field To Search',('Task Assigned To','Task Details'))

        if st.button("Search!"):
            if search_choice == 'Task Details':
                search_result_desc = get_task_by_task_name(search_term)
                df_search_result = pd.DataFrame(search_result_desc,columns=['Task Assigned To','Task Details','Status','Due Date'])
                st.table(df_search_result)
            else:
                search_result_assign = get_task_by_task_assignment(search_term)
                #st.write(search_result)
                df_search_result = pd.DataFrame(search_result_assign,columns=['Task Assigned To','Task Details','Status','Due Date'])
                st.table(df_search_result)



                

