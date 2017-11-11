from tkinter import *

w=Tk()
w.geometry("780x700")
w.title("5TH SEM")
#class for tab press event
class App(object):
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False

    def keyPressed(self,event):
        print("HERE")
        if event.keysym =='Escape':
            root.destroy()
        elif event.keysym == 'Right':
            self.right = True
        elif event.keysym == 'Left':
            self.left = True
        elif event.keysym == 'Up':
            self.up = True

    def keyReleased(self,event):
        if event.keysym == 'Right':
            self.right = False
        elif event.keysym == 'Left':
            self.left = False
        elif event.keysym == 'Up':
            self.up = False

application = App()

#METHODS
def calcu():
    s1=es1.get()
    s2=es2.get()
    s3=es3.get()
    s4=es4.get()
    s5=es5.get()
    s6=es6.get()
    s7=es7.get()
    s8=es8.get()
    s9=es9.get()
    ct=4
    cp=2
    chs=1
    tcredit=27
    p1=int(s1)*ct
    p2=int(s2)*ct
    p3=int(s3)*ct
    p4=int(s4)*ct
    p5=int(s5)*ct
    p6=int(s6)*cp
    p7=int(s7)*cp
    p8=int(s8)*cp
    p9=int(s9)*chs
    gpa=((p1+p2+p3+p4+p5+p6+p7+p8+p9)/tcredit)
    print("Your Gpa of this sem is :",gpa)
    ef.insert(END,gpa)



#HEADER LABEL
lt0=Label(w,text="DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING",font=("algerian",20,"bold"),bg="purple",fg="white")
lt0.grid(row=0,column=0,columnspan=5)
lt1=Label(w,text="GPA calculator for 5th sem",font=("algerian",18,"bold"),bg="purple",fg="white")
lt1.grid(row=1,column=0,columnspan=5)
lt2=Label(w,text="PONDICHERRY UNIVERSITY",font=("algerian",15,"bold"),bg="purple",fg="white")
lt2.grid(row=2,column=0,columnspan=5,pady=5,padx=5)
#column headings
l0=Label(w,text="CODE",font=("age",16,"bold"),bg="purple",fg="white")
l0.grid(row=3,column=0)
l1=Label(w,text="SUBJECTS",font=("age",16,"bold"),bg="purple",fg="white")
l1.grid(row=3,column=1)
l2=Label(w,text="GRADE",font=("age",16,"bold"),bg="purple",fg="white")
l2.grid(row=3,column=3)

#code number
lc1=Label(w,text="CST 51",font=("times",16),bg="purple",fg="white")
lc1.grid(row=4,column=0)
lC2=Label(w,text="CS T52",font=("times",16),bg="purple",fg="white")
lC2.grid(row=5,column=0)
lC3=Label(w,text="CS T53",font=("times",16),bg="purple",fg="white")
lC3.grid(row=6,column=0)
lC4=Label(w,text="CS T54",font=("times",16),bg="purple",fg="white")
lC4.grid(row=7,column=0)
lC5=Label(w,text="CS T55",font=("times",16),bg="purple",fg="white")
lC5.grid(row=8,column=0)
lp0=Label(w,text="PRACTICALS",font=("times",16),bg="purple",fg="white")
lp0.grid(row=9,column=0)
lP1=Label(w,text="CS P51",font=("times",16),bg="purple",fg="white")
lP1.grid(row=10,column=0)
lP2=Label(w,text="CS P52",font=("times",16),bg="purple",fg="white")
lP2.grid(row=11,column=0)
lP3=Label(w,text="CS P53",font=("times",16),bg="purple",fg="white")
lP3.grid(row=12,column=0)
lP4=Label(w,text="HS P54",font=("times",16),bg="purple",fg="white")
lP4.grid(row=13,column=0)
#THEORY SUBJECT NAME
lS1=Label(w,text="OPERATING SYSTEM",font=("times",16),bg="purple",fg="white")
lS1.grid(row=4,column=1)
lS2=Label(w,text="COMPUTER NETWORKS",font=("times",16),bg="purple",fg="white")
lS2.grid(row=5,column=1)
lS3=Label(w,text="DATABASE MANAGEMENT SYSTEM",font=("times",16),bg="purple",fg="white")
lS3.grid(row=6,column=1)
lS4=Label(w,text="LANGUAGE TRANSLATOR",font=("times",16),bg="purple",fg="white")
lS4.grid(row=7,column=1)
lS5=Label(w,text="SOFTWARE ENGINEERING",font=("times",16),bg="purple",fg="white")
lS5.grid(row=8,column=1)
#PRACTICAL SUBJECT NAME
lS6=Label(w,text="OPERATING SYSTEM LAB",font=("times",16),bg="purple",fg="white")
lS6.grid(row=10,column=1)
lS7=Label(w,text="COMPUTER NETWORKS LAB",font=("times",16),bg="purple",fg="white")
lS7.grid(row=11,column=1)
lS8=Label(w,text="DATABASE MANAGEMENT SYSTEM LAB",font=("times",16),bg="purple",fg="white")
lS8.grid(row=12,column=1)
lS9=Label(w,text="GENERAL PROFICIENCY-1",font=("times",16),bg="purple",fg="white")
lS9.grid(row=13,column=1)

#ENTRYS OR TEXT BOXES
es1=Entry(w)
es1.grid(row=4,column=3)
es2=Entry(w)
es2.grid(row=5,column=3)
es3=Entry(w)
es3.grid(row=6,column=3)
es4=Entry(w)
es4.grid(row=7,column=3)
es5=Entry(w)
es5.grid(row=8,column=3)
es6=Entry(w)
es6.grid(row=10,column=3)
es7=Entry(w)
es7.grid(row=11,column=3)
es8=Entry(w)
es8.grid(row=12,column=3)
es9=Entry(w)
es9.grid(row=13,column=3)

#final gui gpa result shower

bf=Button(text=" CLICK FOR GPA",fg="white",bg="green",font=("algerian",20,'bold'),command=calcu)
bf.grid(row=18,column=1,rowspan=20,columnspan=2)
ef=Entry(w)
ef.grid(row=14,column=3 ,rowspan=20)


#tab press binding
w.bind_all('<Key>', application.keyPressed)
w.bind_all('<KeyRelease>', application.keyReleased)
w.bind('<Return>',lambda e:calcu())
#windows executions
w.config(bg="purple")
w.mainloop()
