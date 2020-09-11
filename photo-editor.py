from tkinter import *
from tkinter import filedialog
import numpy as np
from tkinter import messagebox
from PIL import ImageTk,Image
import cv2
root=Tk()

class structure:
    imagelist=[]
    imageindex=0
    path = ""
    bright=0
    image=""
    original=()
    imageheight=0
    imagewidth=0
    height=root.winfo_screenheight()
    width=root.winfo_screenwidth()
    root.geometry(f"{width}x{height}")
    frame1=Frame(root,background="indigo",height=height,width=width)
    frame1.place(x=0,y=0)
    mymenu = Menu(root,font=("",10,"bold"))
    frameedit=PanedWindow(root,background="white",height=height-150,width=width*2/3,orient=HORIZONTAL)
    frameedit.place(x=20,y=80)
    frameedit.add(Label(frameedit))
    frameedit2 = PanedWindow(frameedit, background="blue", bd=5, orient=VERTICAL)
    frameedit2.add(Label(frameedit2))
    label1 =Canvas(frameedit2, bd=5)
    frameedit2.add(label1)

    frameedit.add(frameedit2)
    panel1=PanedWindow(bd=3,relief="raised",bg="gray",orient="vertical" ,width=(width*1/3)-50,height=height-150)
    panel1.place(x=40+width*2/3,y=80)
    frame2=Frame(panel1,bd=5)
    panel1.add(frame2)
    frame3= Frame(panel1,  bd=5)
    panel1.add(frame3)
    #Frame(frame1,background="gray",bd=5,relief="sunken",height=height-150,width=200).place(x=40+width*2/3,y=80)
    #Frame(frame1,background="gray",bd=5,relief="sunken",height=height-150,width=180).place(x=260+width*2/3,y=80)
    def __init__(self):
        root.config(menu=self.mymenu)
        file_menu = Menu(self.mymenu,font=("Times32",10,""),bd=0)
        self.mymenu.add_cascade(label="   File", menu=file_menu)
        file_menu.add_command(label="New", command=self.newa())
        file_menu.add_command(label="Open", command=lambda :self.open())
        file_menu.add_command(label="Save", command=self.newa())
        file_menu.add_command(label="Save As", command=lambda :self.save())
        file_menu.add_command(label="Exit", command=self.newa())
        file_menu.add_separator()
        edit_menu = Menu(self.mymenu, font=("Times32", 10, ""), bd=0)
        self.mymenu.add_cascade(label="   Edit", menu=edit_menu)
        edit_menu.add_command(label="Copy", command=self.newa())
        edit_menu.add_command(label="Cut", command=self.newa())
        edit_menu.add_command(label="Paste", command=self.newa())
        edit_menu.add_separator()
        help_menu = Menu(self.mymenu, font=("Times32", 10, ""), bd=0)
        self.mymenu.add_cascade(label="   Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.newa())
        help_menu.add_separator()
        self.bt1= Button(root,text="Zoom in",command=lambda: self.zoomin())
        self.bt1.place(x=500,y=50)
        self.bt2=Button(root, text="Zoom out", command=lambda: self.zoomout())
        self.bt2.place(x=700, y=50)
        Button(root, text="<<", command=lambda: self.redo(1)).place(x=200, y=50)
        Button(root, text=">>", command=lambda: self.redo(0)).place(x=350, y=50)

        Label(self.frame3,text="    Tools  ",bd=1,background="blue" ,font=("TimesNewRoman",20,"bold")).grid(row=0,column=1)
        Label(self.frame3, text="", bd=1, font=("TimesNewRoman", 20, "bold")).grid(row=1, column=1)

        self.b1=Button(self.frame3,text="    Filters    ",bd=1,background="Gray" ,font=("TimesNewRoman",20,"bold"),command=lambda:self.edit(1))
        self.b1.grid(row=2,column=0,pady=15,padx=10)
        self.b2=Button(self.frame3, text="Blur", bd=1, background="gray",font=("TimesNewRoman",20,"bold"),command=lambda :self.edit(3))
        self.b2.grid( row=2, column=2)
        self.b3=Button(self.frame3, text="Brightness", bd=1, background="gray", font=("TimesNewRoman", 20, "bold"),command=lambda :self.edit(2))
        self.b3.grid(row=3,
                                                                                                             column=0,pady=15,padx=10)
        self.b4=Button(self.frame3, text="Threshold", bd=1, background="gray", font=("TimesNewRoman", 20, "bold"),command=lambda :self.edit(4))
        self.b4.grid(row=4,column=0)
        self.b5=Button(self.frame3, text="Saturation", bd=1, background="gray", font=("TimesNewRoman", 20, "bold"))
        self.b5.grid(row=5,
                                                                                                                 column=0,
                                                                                                                 pady=15,padx=10)
        self.listbut=[self.b1,self.b2,self.b3,self.b4,self.b5,self.bt1,self.bt2]
        for i in self.listbut:
            i.config(state="disabled")

    def newa(self):
        pass
    def save(self):
            image = cv2.resize(self.image, self.original)
            image = Image.fromarray(image)
            top=Toplevel()
            top.geometry("600x400")
            tex1=Text(top,height=1,width=15,font=("Georgia",30,"bold"))
            tex1.pack(padx=20,pady=40)
            listbox=Listbox(top,height=5,width=100)
            listbox.pack(pady=20,padx=100)
            list1=["png","jpeg","jpg","gif","ico"]
            for i in range(0, len(list1)):
                listbox.insert(i, list1[i])
            Button(top,text="Save",command=lambda:versus()).pack()
            def versus():
                aa=str(tex1.get()) + "." + listbox.get(ANCHOR)
                print(aa)
                cv2.imwrite(aa, self.image)
                top.destroy()


            # if filesave is None:
            #      messagebox.showwarning("Error saving file","Unable to save the file.process failed sucessfully")
            # else:
            #     messagebox.showwarning("Saved", "File saved sucessfully")
            # image.save(filesave)



    def edit(self,variable):
        top=Toplevel()
        top.geometry("800x600")
        list1=["Gray Scale","horror red","Beyer rgb","HSV","High Lens","Hue down"]
        if variable==1:
            Label(top,text="Filters",font=("Georgia",15,"bold")).pack()
            listbox=Listbox(top,width=25,height=15,font=("Georgia",15,"bold"),selectmode=SINGLE)
            listbox.place(x=250,y=50)
            for i in range(0,len(list1)):
                listbox.insert(i,list1[i])
            Button(top,text="Apply",background="red",foreground="blue",command=lambda:self.setfilter(listbox.get(ANCHOR),top)).place(x=300,y=400)

        if variable==2:
            Label(top, text="Brightness", font=("Georgia", 15, "bold")).pack()
            slider=Scale(top,from_=0,to=200,orient=HORIZONTAL,length=250,bg="gray")
            slider.set(self.bright)
            slider.pack(padx=50,pady=30)
            Button(top, text="Apply", background="red", foreground="blue",
                 command=lambda: self.brightness(slider.get())).place(x=300, y=400)

        if variable == 3:
            Label(top, text="Blur", font=("Georgia", 15, "bold")).pack()
            slider = Scale(top, from_=0, to=10, orient=HORIZONTAL, length=250, bg="gray",label="blur amount")

            slider.pack(padx=50, pady=30)
            slider2 = Scale(top, from_=0, to=5, orient=HORIZONTAL,label="Sigma hex", length=250, bg="gray")

            slider2.pack(padx=50, pady=30)
            if slider.get()%2==0:
                slider.set(slider.get()+1)
            Button(top, text="Apply", background="red", foreground="blue",
                   command=lambda: self.blur(slider.get(),slider2.get(),top)).place(x=300, y=400)
        if variable == 4:
            Label(top, text="Threshold", font=("Georgia", 15, "bold")).pack()
            slider = Scale(top, from_=0, to=200, orient=HORIZONTAL, length=250, bg="gray", label="Amount:")
            slider.pack(padx=50)
            Button(top, text="Apply", background="red", foreground="blue",
                   command=lambda: self.threshold(slider.get(),top)).place(x=300, y=400)



    def threshold(self,value,box):
        box.destroy()
        temp=cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY)
        self.image=cv2.threshold(temp,value,value,cv2.THRESH_BINARY)
        self.backup()
        self.imageset()

    def setfilter(self,x,box):
        box.destroy()
        if(str(x).upper() == "GRAY SCALE"):
            self.image=cv2.imread(f"{self.path}")
            imggray=cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY)
        elif (str(x).upper() == "HORROR RED"):
            img = cv2.imread(f"{self.path}")
            imggray = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        elif (str(x).upper() == "BEYER RGB"):
            img = cv2.imread(f"{self.path}")
            imggray = cv2.cvtColor(img, cv2.COLOR_YUV2BGR)
        elif (str(x).upper() == "HSV"):
            img = cv2.imread(f"{self.path}")
            imggray = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
        elif (str(x).upper() == "HSV"):
            img = cv2.imread(f"{self.path}")
            imggray = cv2.cvtColor(img, cv2.COLOR_RGB2LUV)
        elif (str(x).upper() == "HIGH LENS"):
            img = cv2.imread(f"{self.path}")
            imggray = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
        elif (str(x).upper() == "HUE DOWN"):
            img = cv2.imread(f"{self.path}")
            imggray = cv2.cvtColor(img, cv2.COLOR_RGB2XYZ)
        self.image=imggray
        self.backup()
        self.imageset()
        #imggray = ImageTk.PhotoImage(imggray)
        #self.label1.image = imggray
        #self.label1.config(image=imggray)
    def brightness(self,x):
        self.bright=x
        self.image.set(10,self.bright)
        self.imageset()

    def blur(self, x,y,box):
        box.destroy()
        self.image=cv2.blur(self.image,(x,x))
        self.backup()
        self.imageset()

    def resize(self,image):
        #height=500
        #width=800
        image=Image.fromarray(image)
        im2 = image.resize((self.imagewidth, self.imageheight), Image.ANTIALIAS)
        return im2
    def imageset(self):
        image1 = self.resize(self.image)
        image2 = ImageTk.PhotoImage(image1)
        self.label1.image = image2
        self.label1.create_image(500,300,image=image2,anchor=CENTER)
    def backup(self):
        self.imagelist.insert(self.imageindex,self.image)
        self.imageindex += 1

    def open(self):
        filepath=filedialog.askopenfilename(initialdir="./",title="Select a image",filetypes=(("png/jpeg","*.jpeg *.png *.gif *.ico *.jpg"),("all","*.*")))
        self.path=filepath
        self.image = cv2.imread(filepath)
        self.image=cv2.cvtColor(self.image,cv2.COLOR_BGR2RGB)
        self.backup()
        imagedim=Image.fromarray(self.image)
        self.original=imagedim.size
        self.imagewidth,self.imageheight=imagedim.size
        self.imageset()

        for i in self.listbut:
            i.config(state="active")
    def redo(self,x):
        if( self.imageindex<=0):self.imageindex+=1
        elif(self.imageindex>len(self.imagelist) ):
            self.imageindex-=1

        else:
            if (x == 0):
                self.imageindex += 1
                self.image = self.imagelist[self.imageindex - 1]
            elif (x == 1):
                self.imageindex -= 1
                self.image = self.imagelist[self.imageindex - 1]
            self.imageset()


    def zoomin(self):
        self.imagewidth=round(self.imagewidth*1.5)
        self.imageheight = round(self.imageheight * 1.5)
        self.imageset()
    def zoomout(self):
        self.imagewidth=round(self.imagewidth*0.7)
        self.imageheight = round(self.imageheight * 0.7)
        self.imageset()

varia=structure()
root.mainloop()


