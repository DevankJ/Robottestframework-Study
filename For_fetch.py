import mysql.connector as connector



def fetch_all():
    conn=connector.connect(host="localhost",user="root",password="1234",database="pythontest")
    query="select * from emp_data"
    cur=conn.cursor()
    cur.execute(query)
    
    
    for column in cur:
        print(column)
    # a=pd.Dataframe(column)
    # print(a)

fetch_all()