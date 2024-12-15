import sqlite3


con=sqlite3.connect("mentor.db")
cur=con.cursor()

                                      #create mentor table
cur.execute("create table men (student_name char(20), student_id number, mentor_name char(20), mentor_mobile number, parent_name char(20), parent_mobile number)")


                    #TO INSERT DATA
student_name = []
student_id=[]
mentor_name=[] 
mentor_number=[]
parent_name=[]
parent_number=[]
#newstu=[]
      
for i in range(4):
   cur.execute("update men set parent_name=?,parent_mobile=? where student_id=?",(parent_name[i],parent_number[i],newstu[i]))
con.commit()


                        #create password table
cur.execute("create table password(mentor_name char(20), password varchar(10))")

mentor_name=[]
password=[]
for i in range(11):
 cur.execute("insert into password values(?,?)",(mentor_name[i],password[i]))

con.commit()
