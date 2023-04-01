import sqlite3

conn = sqlite3.connect('my_db.db',check_same_thread=False)

c = conn.cursor()

def creat_table():
    c.execute('CREATE TABLE IF NOT EXISTS tasktable(task_assigned TEXT,task_details TEXT,task_status TEXT,task_date DATE)')

def add_task(task_assigned,task_details,task_status,task_date):
    c.execute('INSERT INTO tasktable(task_assigned,task_details,task_status,task_date) VALUES(?,?,?,?)',
              (task_assigned,task_details,task_status,task_date))
    conn.commit()


def view_all_tasks():
    c.execute('SELECT * FROM tasktable')
    data = c.fetchall()
    return data

def view_unique_task_name():
    c.execute('SELECT DISTINCT task_details FROM tasktable')
    data = c.fetchall()
    return data

def get_task_by_task_name(task_details):
    c.execute('Select * FROM tasktable WHERE task_details = "{}"'.format(task_details))
    data = c.fetchall()
    return data
def get_task_by_task_assignment(task_details):
    c.execute('Select * FROM tasktable WHERE task_assigned = "{}"'.format(task_details))
    data = c.fetchall()
    return data

def update_task(new_task_assignment,new_task_description, new_task_status ,new_task_due_date,
                task_assignment,task_description,task_status ,task_due_date):
    c.execute('UPDATE tasktable SET task_assigned=?,task_details=?,task_status=?,task_date =? WHERE task_assigned=? AND task_details=? AND task_status=? AND task_date =?  ',
              (new_task_assignment,new_task_description, new_task_status ,new_task_due_date,task_assignment,task_description,task_status ,task_due_date))
    conn.commit()
    data = c.fetchall()
    return data

def delete_task(task):
    c.execute('DELETE FROM tasktable WHERE task_details="{}"'.format(task))
    conn.commit()
