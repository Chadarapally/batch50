import json
import psycopg2

def get_pg_con():
	f=open("config.json")
	data=json.load(f)
	db_data=data.get("dbdetails")
	user=db_data.get("username")
	print user
	pwd=db_data.get("password")
	print pwd
	host=db_data.get("host")
	database=db_data.get("dbname")
	port=db_data.get("port")
	con=psycopg2.connect(database=database,host=host,port=port,user=user,password=pwd )
	cur=con.cursor()
	return con,cur
