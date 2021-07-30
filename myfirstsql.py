import mysql.connector as connector

def __init__():
    conn=connector.connect(host="localhost",user="root",password="1234",database="pythontest")
    query='create table if not exists user(userId int primary key, userName varchar(200))'
    cur=conn.cursor()
    cur.execute(query)
    print("Created")
    conn.close()

def insert_user(userid,username):
    conn=connector.connect(host="localhost",user="root",password="1234",database="pythontest")
    query="insert into user(userId,userName) values({},'{}')".format(userid,username)
    print(query)
    cur=conn.cursor()
    cur.execute(query)
    conn.commit()
    #print("user saved to database")

insert_user(14,"dev")



# conn=connector.connect(user='root',password='Devank123',host='localhost',database='pythontest')

#     #creating a cursor
# cursor=conn.cursor()
#     # # drop the table if already present
# # cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# # sql='''CREATE TABLE EMPLOYEE(FIRST_NAME CHAR(20) NOT NULL,AGE INT)'''
# # cursor.execute(sql)


# # cursor=conn.cursor()
# sql="""INSERT INTO EMPLOYEE(FIRST_NAME,AGE) VALUES("DEVANK",23)"""
# cursor.execute(sql)
# print(sql)
# print("created")
# conn.commit()   # pushing changes into database







