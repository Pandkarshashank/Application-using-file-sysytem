from tkinter import *
import random
import string
from turtle import bgcolor, delay

l=[]

window=Tk()
window.geometry("1890x1890")
window.title("Application name")
labelframe = LabelFrame(window)
labelframe.pack(fill="both", expand="yes")
 
#
# 
# 
# ow.wm_attributes('-transparentcolor', '#ab23ff')

photo=PhotoImage(file='index.png')
label=Label(window,image=photo)
label.pack()

left = Label(labelframe, text="Tenate Record",bg="light yellow",fg ='black',font=('arial',25,"bold"))
left.place(x=550,y=170)
"""
lebelframe = LabelFrame(window,text='Tenant Record',bg="light yellow",fg ='red',font=('arial',25,"bold"))
lebelframe.pack(expand="yes", fill="both")
left = Label(LabelFrame,text="tenant record")
left.pack()"""

def login():
    # window.destroy()  
    login_window = Tk() 
    login_window.title("LogIn")
    login_window.geometry("1890x1890") 
    
    label=Label(login_window,text="Enter flat number :",font=(500),bg="light yellow",fg ='blue')
    label.place(x=200,y=250)
    enterflatno=Entry(login_window)
    enterflatno.place(x=550,y=250)
   

    label=Label(login_window,text="Enter password :",font=(500),bg="light yellow",fg ='blue')
    label.place(x=200,y=270)
    enterpassword=Entry(login_window,show="*")
    enterpassword.place(x=550,y=270)
   
        
    def check():
        file1=open("Tenant_records.txt","r")
        for line in file1:
            str=line[0:3]
            str1=line[4:9]
        if(str==enterflatno.get() and str1==enterpassword.get()):
            print(str+str1)
            login_window.destroy()
            choice_window=Tk()
            choice_window.title("LogIn") 
            choice_window.geometry("1890x1890")

            def lodge_complaint():
                choice_window.destroy()
                complaint_window=Tk()
                complaint_window.geometry("1890x1890")
                complaint_window.title("Application name")
                label=Label(complaint_window,text="Enter Complaint :",font=(500))
                label.place(x=200,y=270)
                
                entercomplaint=Entry(complaint_window)
                entercomplaint.place(x=550,y=270)
                def okay():
                    # FIRST CHANGE
                    # complaint_window.destroy()
                    file1=open("Complaint_records.txt","a")
                    str1=entercomplaint.get()
                    file1.write(str1+"\n")
                    file1.close()
                buttton=Button(complaint_window,text="Lodge Complaint",command=okay,font=(30),width=50,height=5)
                buttton.place(x=500,y=300)
                # BACK BUTTON
                def back():
                    complaint_window.destroy()
                    login()
                buttton_back=Button(complaint_window,text="Back",command=back,bg="light yellow",fg= "green",font=('arial',20,"bold"))
                buttton_back.place(x=600,y=700)

                complaint_window.mainloop()

                

            buttton=Button(choice_window,text="Lodge Complaint",command=lodge_complaint,font=(30),width=50,height=5)
            buttton.place(x=400,y=200)

            def view_complaint():
                choice_window.destroy()
                view_complaint_window=Tk()
                view_complaint_window.geometry("1890x1890")
                view_complaint_window.title("Application name")
            # SECOND CHANGE
                # file1=open("Complaint_records.txt","r")
                # i=0
                # for line in file1:
                #     str="\nComplaints: "+line
                my_label1 = Label(view_complaint_window,
                        text="Complaints: ",
                        font=("Helvetica",18),
                        bd=1)
                my_label1.pack(pady=50)
            # SECOND CHANGE
                j=0
                with open("Complaint_records.txt", "r") as topo_file:
                    complaint_view = Label(view_complaint_window,text=topo_file.read(),font=(20), padx=140,pady=20).pack()    
                    # label=Label(view_complaint_window,text=complaint_view,font=(500),bg="light yellow",fg ='red')
                    # label.place(x=200,y=150+j)
                    # j=j+20

                def back():
                    view_complaint_window.destroy()
                    choice_window()
                buttton_back=Button(view_complaint_window,text="Back",command=back,bg="light yellow",fg= "green",font=('arial',20,"bold"))
                buttton_back.place(x=600,y=700)

                view_complaint_window.mainloop()

            buttton=Button(choice_window,text="View Complaint",command=view_complaint,font=(30),width=50,height=5)
            buttton.place(x=400,y=600)

            def view_records():
                choice_window.destroy()
                records_window=Tk()
                records_window.geometry("1890x1890")
                records_window.title("Application name")
                file1=open("Tenant_records.txt","r")
                j=0
                for line in file1:
                    str="\nName: "+line[16:]+"Contact :"+line[10:15]+"\nFlat number: "+line[0:3]
                    label=Label(records_window,text=str,font=(500))
                    label.place(x=200,y=50+j)
                    j=j+20
                # print(str)
                records_window.mainloop()

            buttton1=Button(choice_window,text="View Records",command=view_records,font=(30),width=50,height=5)
            buttton1.place(x=400,y=400)

            choice_window.mainloop()
        else:
            login_window.destroy()
            error_window=Tk()
            error_window.geometry("1890x1890")
            error_window.title("Application name")
            label=Label(error_window,text="Enter correct info!!!",font="times 70")
            label.place(x=200,y=50)

    buttton1=Button(login_window,text="Enter",command=check,bg="light yellow",fg= "green",font=('arial',20,"bold"))
    buttton1.place(x=700,y=400)
    def back():
        login_window.destroy()
        # new_window = window
        # new_window()
        window()
    # BACK BUTTON 
    buttton_back=Button(login_window,text="Back",command=back,bg="light yellow",fg= "green",font=('arial',20,"bold"))
    buttton_back.place(x=500,y=400)
    # buttton_back.pack()
   

    login_window.mainloop()

def signup():
    window.destroy()
    signup_window=Tk()
    signup_window.geometry("1890x1890")
    signup_window.title("Signup")
    
    label=Label(signup_window,text="Enter Name :",font=(500),bg="light yellow",fg ='red')
    label.place(x=300,y=270)
    entername=Entry(signup_window)
    entername.place(x=550,y=270)

    label=Label(signup_window,text="Enter Contact(5 digits only) :",font=(500),bg="light yellow",fg ='red')
    label.place(x=300,y=290)
    entercontact=Entry(signup_window)
    entercontact.place(x=550,y=290)

    label=Label(signup_window,text="Enter flat number(3 digits only) :",font=(500),bg="light yellow",fg ='red')
    label.place(x=300,y=310)
    enterflat=Entry(signup_window)
    enterflat.place(x=550,y=310)

    password=''.join(random.choices(string.ascii_uppercase+string.digits,k=5))

    def ok():
        file1=open("Tenant_records.txt","a")
        space=" "
        str1=enterflat.get()+space+password+space+entercontact.get()+space+entername.get()
        file1.write(str1+"\n")
        file1.close() 
        display_window=Tk()
        display_window=Tk()
        display_window.geometry("1890x1890")
        display_window.title("Display")
        str="\nFlatno: "+enterflat.get()+"\nPassword :"+password
        label=Label(display_window,text=str)
        label.pack()
        display_window.mainloop()
        signup_window.destroy()
        display_window.destory()

    buttton=Button(signup_window,text="OK",command=ok,bg="light yellow",fg= "green",font=('arial',20,"bold"))
    buttton.place(x=500,y=400)#400,350

buttton=Button(window,text="Signup",bg="#ab23ff",fg= "green",font=('arial',20,"bold"),command=signup,)#font="times 20")
buttton.place(x=500,y=400)#400,200

buttton1=Button(window,text="Login",bg="#ab23ff",fg ='green',font=('arial',20,"bold"), command=login)#,font="times 20")
buttton1.place(x=700,y=400)#600,200

window.mainloop()