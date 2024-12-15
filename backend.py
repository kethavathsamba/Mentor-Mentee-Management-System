import sqlite3
from tkinter import *
from tkinter import messagebox,simpledialog
from tkinter import ttk
from frontend import *

con=sqlite3.connect("mentor.db")

cur=con.cursor()

def student_data(val):

    val = val.upper()
    cur.execute("select student_id,student_name,parent_name,parent_mobile from men where mentor_name=?",(val,))
    m=cur.fetchall()
   
    if(val == ''):
        messagebox.showwarning("WARNING", "PLEASE ENTER MENTOR NAME",)
    elif len(m)==0:
        messagebox.showwarning("WARNING", "NO DATA FOUND",) 
    else:
        root=Tk()
        root.geometry("800x210")
        root.title("student data")
        Label(root,text="MENTEES LIST",font=("bold",10)).pack()
        TREE=ttk.Treeview(root,columns=("student pin","student name","parent name","mobile number"),show="headings")
        TREE.heading("student name",text="STUDENT NAME")
        TREE.heading("student pin",text="STUDENT PIN")
        TREE.heading("parent name",text="PARENT NAME")
        TREE.heading("mobile number",text="MOBILE NUMBER")
        TREE.column("student name", anchor="center")  
        TREE.column("student pin", anchor="center")
        TREE.column("parent name", anchor="center")  
        TREE.column("mobile number", anchor="center") 
        TREE.pack()
        for i in m:
            TREE.insert("","end",values=(i))

    
        root.mainloop()

    
    
def mentor_data(val):
    

    cur.execute("select mentor_name from men where student_id=?",(val,))
    tmname=cur.fetchall()
    

    if(val == ''):
        messagebox.showwarning("WARNING", "PLEASE ENTER STUDENT ROLL NUMBER",)

    elif len(tmname)==0:
        messagebox.showwarning("WARNING", "NO DATA FOUND",)
    
    else:
        root=Tk()  
        root.geometry("400x400")
        root.title("MENTEE DATA")
        
        Label(root,text="DETAILS",font=("bold",13)).place(x=130,y=0)
        mname=Label(root,text="MENTOR NAME: ",font=("bold",10))
        mphn=Label(root,text="MENTOR PHN:",font=("bold",10))
        sname=Label(root,text="STUDENT NAME:",font=("bold",10))
        pname=Label(root,text="PARENT NAME:",font=("bold",10))
        pphn=Label(root,text="PARENT PHN:",font=("bold",10))

        emname=Entry(root,width=25,font=("bold",12))
        emphn=Entry(root,width=25,font=("bold",12))
        esname=Entry(root,width=25,font=("bold",12))
        epname=Entry(root,width=25,font=("bold",12))
        epphn=Entry(root,width=25,font=("bold",12))
        

        mname.place(x=45 ,y=50 ) 
        emname.place(x=150 ,y=50 ) 
        mphn.place(x=53,y=100 ) 
        emphn.place(x=150 ,y=100 ) 
        sname.place(x=40 ,y=150 ) 
        esname.place(x= 150,y=150 ) 
        pname.place(x=45,y=200 ) 
        epname.place(x= 150,y=200 ) 
        pphn.place(x= 53,y=250 ) 
        epphn.place(x=150 ,y=250 ) 

        
        cur.execute("select mentor_mobile from men where student_id=?",(val,))
        tmphn=cur.fetchall()
        cur.execute("select student_name from men where student_id=?",(val,))
        tsname=cur.fetchall()
        cur.execute("select parent_name from men where student_id=?",(val,))
        tpname=cur.fetchall()
        cur.execute("select parent_mobile from men where student_id=?",(val,))
        tpphn=cur.fetchall()
        
        emname.insert(0,tmname[0][0])
        esname.insert(0,tsname[0][0])
        emphn.insert(0,tmphn)
        epname.insert(0,tpname[0][0])
        epphn.insert(0,tpphn)

        emname.config(state=DISABLED)
        esname.config(state=DISABLED)
        emphn.config(state=DISABLED)
        epname.config(state=DISABLED)
        epphn.config(state=DISABLED)
        
        root.mainloop()


def updatetable(namem,studentlist):
    
    root=Tk()
    root.geometry("300x210")

    root.title(namem[0])

    s_pin=Label(root,text="student pin:")
    s_name=Label(root,text="student name:")
    p_name=Label(root,text="parent name:")
    p_phn=Label(root,text="parent mobile:")
    es_pin=Entry(root)
    es_name=Entry(root)
    ep_name=Entry(root)
    ep_phn=Entry(root)
    submit=Button(root,text="submit",command=lambda:change(es_pin.get(),es_name.get(),ep_name.get(),ep_phn.get(),studentlist,root))

    s_pin.grid(row=0,column=0,padx=10,pady=5)
    es_pin.grid(row=0,column=1)
    s_name.grid(row=1,column=0,padx=20,pady=10)
    es_name.grid(row=1,column=1)
    p_name.grid(row=2,column=0,padx=20,pady=10)
    ep_name.grid(row=2,column=1)
    p_phn.grid(row=3,column=0,padx=20,pady=10)
    ep_phn.grid(row=3,column=1)
    submit.grid(row=4,column=1)
    root.mainloop()


def change(sid,sname,pname,pmobile,studentlist,root):
    for i in studentlist:
        if(sid == i):
            cur.execute("update men set student_name=?,parent_name=?,parent_mobile=? where student_id=?",(sname,pname,pmobile,sid))
            con.commit()
            messagebox.showinfo("update", "STUDENT DETAILS ARE UPDATED")
            
    if(sid !=i):
        messagebox.showerror("error","you cannot change the above student details")
    root.destroy()
 

def update():

    password=simpledialog.askstring("enter password","enter password")
    cur.execute('select mentor_name from password where password=?',(password,))
    mname=cur.fetchall()
    student = ''
    for i in mname:
        namem=i
        cur.execute("select student_id from men where mentor_name=?",(namem))
        student=cur.fetchall()
    if(student == ''):
        messagebox.showerror("error","no data found")
    else:
        updatetable(namem,student)

def view_data():
    cur.execute("select student_id,student_name,parent_name,parent_mobile,mentor_name,mentor_mobile from men")
    m=cur.fetchall()
    root=Tk()
    root.geometry("800x500")
    root.title("student data")
    Label(root,text="MENTEES LIST",font=("bold",10)).pack()
    TREE=ttk.Treeview(root,columns=("student pin","student name","parent name","mobile number","mentor name","mentor number"),show="headings",height=400)
    TREE.heading("student name",text="STUDENT NAME")
    TREE.heading("student pin",text="STUDENT PIN")
    TREE.heading("parent name",text="PARENT NAME")
    TREE.heading("mobile number",text="MOBILE NUMBER")
    TREE.heading("mentor name",text="MENTOR NAME")
    TREE.heading("mentor number",text="MENTOR NUMBER")
    TREE.column("student name", anchor="center")  
    TREE.column("student pin", anchor="center")
    TREE.column("parent name", anchor="center")  
    TREE.column("mobile number", anchor="center") 
    TREE.column("mentor name", anchor="center") 
    TREE.column("mentor number", anchor="center") 
    TREE.pack(fill="both")
    for i in m:
        TREE.insert("","end",values=(i))

    root.mainloop()

def new_mentor(oname,opassword,nname,npassowrd,root):
    nam=cur.execute("select password from password where mentor_name=?",(oname,))
    if (nam==opassword):
        cur.execute("update men set mentor_name=? where mentor_name=?",(oname,nname))
        cur.execute("update password set mentor_name=? where mentor_name=?",(oname,nname))
        cur.execute("update password set password=? where password=?",(opassword,npassowrd))
        messagebox.showinfo("UPDATE","MENTOR DATA UPDATED")
        root.destroy()
    else:
        messagebox.showinfo("ERROR","INVALID NAME AND PASSWORD")
        root.destroy()

def change_mentor():
    root=Tk()
    root.geometry("300x210")


    oname=Label(root,text="EXISTING MENTOR NAME:")
    opassowrd=Label(root,text="EXISTING PASSWORD:")
    nname=Label(root,text="NEW MENTOR NAME:")
    npassword=Label(root,text="NEW PASSWORD:")
    oname_e=Entry(root)
    opassowrd_e=Entry(root)
    nname_e=Entry(root)
    npassword_e=Entry(root)
    submit=Button(root,text="Update",command=lambda:new_mentor(oname_e.get(),opassowrd_e.get(),nname_e.get(),npassword_e.get(),root))

    oname.grid(row=0,column=0,padx=10,pady=5)
    oname_e.grid(row=0,column=1)
    nname.grid(row=1,column=0,padx=20,pady=10)
    nname_e.grid(row=1,column=1)
    opassowrd.grid(row=2,column=0,padx=20,pady=10)
    opassowrd_e.grid(row=2,column=1)
    npassword.grid(row=3,column=0,padx=20,pady=10)
    npassword_e.grid(row=3,column=1)
    submit.grid(row=4,column=1)
    
    root.mainloop()

    