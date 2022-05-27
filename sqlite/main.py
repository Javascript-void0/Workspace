import sqlite3 as sql
from sqlite3 import Error

def create_connection(db_file):
	con = None
	try:
		con = sql.connect(db_file)
	except Error as e:
		print(e)
	return con

# def create_table(con, create_table_sql):
# 	try:
# 		c = con.cursor()
# 		c.execute(create_table_sql)
# 	except Error as e:
# 		print(e)

def create_project(con, project):
	sql = ''' INSERT INTO projects(name,begin_date,end_date)
			  VALUES(?,?,?) '''
	cur = con.cursor()
	cur.execute(sql, project)
	con.commit()
	return cur.lastrowid

def create_task(con, task):
	sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
			  VALUES(?,?,?,?,?,?) '''
	cur = con.cursor()
	cur.execute(sql, task)
	con.commit()
	return cur.lastrowid

def update_task(con, task):
	sql = ''' UPDATE tasks
			  SET priority = ?,
				  begin_date = ?,
				  end_date = ?
			  WHERE id = ? '''
	cur = con.cursor()
	cur.execute(sql, task)
	con.commit()

def delete_task(con, id):
	sql = 'DELETE FROM tasks WHERE id=?'
	cur = con.cursor()
	cur.execute(sql, (id,))
	con.commit()

def delete_all_tasks(con):
	sql = 'DELETE FROM tasks'
	cur = con.cursor()
	cur.execute(sql)
	con.commit()

def select_all_tasks(con):
	cur = con.cursor()
	cur.execute('SELECT * FROM tasks')
	rows = cur.fetchall()
	for row in rows:
		print(row)

def select_task_by_priority(con, priority):
	cur = con.cursor()
	cur.execute('SELECT * FROM tasks WHERE priority=?', (priority,))
	rows = cur.fetchall()
	for row in rows:
		print(row)

def main():
	database = './sqlite/data.db'
	con = create_connection(database)
	with con:
		print('1. Query task by priority: ')
		select_task_by_priority(con, 1)
		print('2. Query all tasks: ')
		select_all_tasks(con)
		# delete_task(con, 6)
		# delete_all_tasks(con)

		# update_task(con, (2, '2015-01-04', '2015-01-06', 2))
		
		# project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30')
		# project_id = create_project(con, project)
		# task_1 = ('Analyze the reqirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
		# task_2 = ('Confirm the user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')
		# create_task(con, task_1)
		# create_task(con, task_2)
	# sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
	# 									id integer PRIMARY KEY,
	# 									name text NOT NULL,
	# 									begin_date text,
	# 									end_date text
	# 								); """

	# sql_create_tasks_table = """ CREATE TABLE IF NOT EXISTS tasks (
	# 								id integer PRIMARY KEY,
	# 								name text NOT NULL,
	# 								priority inger,
	# 								status_id integer NOT NULL,
	# 								project_id integer NOT NULL,
	# 								begin_date text NOT NULL,
	# 								end_date text NOT NULL,
	# 								FOREIGN KEY (project_id) REFERENCES prjects (id)
	# 							)
	# 							"""
	# con = create_connection(database)

	# if con is not None:
	# 	create_table(con, sql_create_projects_table)
	# 	create_table(con, sql_create_tasks_table)
	# else:
	# 	print('Error! cannot create the database connection. ')

if __name__ == '__main__':
	main()