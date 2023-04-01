import streamlit as st
from db_Fntx import *
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
def run_manage():
    

    submenu = ['Delete Task','Analytics']
    choice = st.sidebar.selectbox('submenu',submenu)

    if choice == 'Delete Task' :
        st.subheader('Delete')
        tasks_to_delete = view_all_tasks()
        df_tasks_to_delete = pd.DataFrame(tasks_to_delete,columns=['Task Assigned To','Task Details','Status','Due Date'])
        st.table(df_tasks_to_delete)
        
        
        unique_list = [i[0] for i in view_unique_task_name()]
        delete_by_task_name = st.selectbox('Task To Delete',unique_list)
        st.warning('You are About to Delete "{}"'.format(delete_by_task_name))
        if st.button('Delete'):

            delete_task(delete_by_task_name)

            with st.expander('Remaining Tasks'):
                tasks_left = view_all_tasks()
                df_task_left = pd.DataFrame(tasks_left,columns=['Task Assigned To','Task Details','Status','Due Date'])
                st.table(df_task_left)

    else:
        st.subheader('Analyse' )
        task_view = view_all_tasks()
        df_tasks_view = pd.DataFrame(task_view,columns=['Task Assigned To','Task Details','Status','Due Date'])

        with st.expander('View All Tasks'):
            st.table(df_tasks_view)

        with st.expander('Stats: Task Assigned To'):
            st.dataframe(df_tasks_view['Task Assigned To'].value_counts(),use_container_width=True)
            new_df = df_tasks_view['Task Assigned To'].value_counts().to_frame()
            new_df = new_df.reset_index()
            #st.dataframe(new_df)

            pi_plot = px.pie(new_df,names='index',values='Task Assigned To')
            st.plotly_chart(pi_plot,use_container_width=True)
        
        with st.expander('Stats: Task Status'):
            st.dataframe(df_tasks_view['Status'].value_counts(),use_container_width=True)
            new_df_status = df_tasks_view['Status'].value_counts().to_frame()
            new_df_status = new_df_status.reset_index()
            st.dataframe(new_df_status)

            pi_plot_status = px.pie(new_df_status,names='index',values='Status')   
            st.plotly_chart(pi_plot_status,use_container_width=True)


