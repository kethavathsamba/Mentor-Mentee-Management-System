from tkinter import *
import tkinter as root
from backend import *
from PIL import ImageTk, Image
from tkinter import messagebox,simpledialog


def admin():
    password=simpledialog.askstring("PASSWORD","PASSWORD")
    if password== "@admin":
        view=Button(root,text="View Data",command=view_data,width=10,font=("bold",10),bg="sky BLUE")
        change=Button(root,text="Change Mentor",command=change_mentor,width=10,font=("bold",10),bg="sky BLUE")
        view.place(x=100,y=650)
        change.place(x=300,y=650)
    
if __name__ == "__main__":

    main=Tk()
    
    width= main.winfo_screenwidth()               
    height= main.winfo_screenheight()               
    main.geometry("%dx%d" % (width, height))
    main.title("mentor and mentee book")
                        # replace bgimg.png  with any image address which you to be background
    #filename=Image.open('bgimg.png')
    #photo = ImageTk.PhotoImage(filename)
    #lab=Label(main,image=photo)
    #lab.place(x=0,y=0,width=1000,height=800)
    
    

    root=Frame(main,width=430,height=430,bg="sky blue")
    root.place(x=1000,y=0,height=800,width=1000)
    mm_l=Label(root,text='MENTOR AND MENTEE BOOK',font=("bold",20),bg="sky blue")
    

    m_l=Label(root,text="MENTOR NAME",font=("bold",12),bg="sky blue")
    m_e=Entry(root,width=25,highlightbackground="sky blue",border=3)
    m_b=Button(root,text="VIEW STUDENTS",command=lambda:student_data(m_e.get()),bg="sky blue")

    s_l=Label(root,text="STUDENT ID",font=("bold",12),bg="sky blue")
    s_e=Entry(root,width=25,highlightbackground="sky blue",border=3)
    s_b=Button(root,text="VIEW MENTOR",command=lambda:mentor_data(s_e.get()),bg="sky blue")


    update_b=Button(root,text="update",command=update,width=10,font=("bold",10),bg="sky BLUE")
    admin_b=Button(root,text="admin",command=admin,width=10,font=("bold",10),bg="sky BLUE")


    
    mm_l.place(x=100,y=100)

    m_l.place(x=50,y=200)
    m_e.place(x=200,y=200)
    m_b.place(x=380,y=200)

    s_l.place(x=50,y=350)
    s_e.place(x=180,y=350)
    s_b.place(x=350,y=350)
    update_b.place(x=100,y=550)
    admin_b.place(x=300,y=550)


    root.mainloop()


