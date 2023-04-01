import streamlit as st
from db_Fntx import *
import pandas as pd

def run_taskPage():
    st.header('Task Page')

    submenu = st.sidebar.selectbox('submenu',['Add Task','Edit Task'])

    if submenu == 'Add Task':
        st.subheader('Add Task')
        c1,c2 = st.columns([2,1])

        with c1:
            task_assignment = st.text_input('Task Assigned To')
            task_description = st.text_area('Task Details',help='Every Task Detail Must Be Unique')

        with c2:
            task_status = st.selectbox('Status',['Todo','Completed','Continued','Uncertain'])
            task_due_date = st.date_input('Due Date',help='Select date with in a week')

        if st.button("ADD TASK!"):
            add_task(task_assignment,task_description,task_status,task_due_date)
            st.success('Task "{}" Is Assigned To "{}"'.format(task_description,task_assignment))
        
        task_added = view_all_tasks()
        df_task_added = pd.DataFrame(task_added,columns=['Task Assigned To','Task Details','Status','Due Date'])
        st.table(df_task_added)
        
    else:
        st.subheader('Update/Edit Task')
        list_of_tasks = [i[0] for i in view_unique_task_name()]
        selected_task = st.selectbox('Select Task You Want To Update',list_of_tasks)
        task_result = get_task_by_task_name(selected_task)
        #st.write(task_result)
        if task_result:

            task_assignment = task_result[0][0]
            task_description = task_result[0][1]
            task_status = task_result[0][2]
            task_due_date = task_result[0][3]

            c1,c2 = st.columns([2,1])

            with c1:
                new_task_assignment = st.text_input('Task Assigned To',task_assignment)
                new_task_description = st.text_area('Task Details',task_description)

            with c2:
                new_task_status = st.selectbox('Status',['Todo','Completed','Continued','Uncertain'])
                new_task_due_date = st.date_input(task_due_date)

            if st.button("Update Task!"):
                update_task(new_task_assignment,new_task_description, new_task_status ,new_task_due_date,
                task_assignment,task_description,task_status ,task_due_date)
                st.success('Task "{}" Is Updated To "{}"'.format(task_description,new_task_description))