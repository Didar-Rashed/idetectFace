from tkinter import*
from tkinter import ttk 
from PIL import Image,ImageTk
from Student import Student

class Face_recognization_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognation System")

        # Zeroth Image
        img = Image.open(r"D:\IdetectFace\images\img.jpg")
        img = img.resize((500,130))
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=-30,y=0,width=500,height=130)

        # First Image
        img1 = Image.open(r"D:\IdetectFace\images\img1.jpg")
        img1 = img1.resize((500,130))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=470,y=0,width=500,height=130)

        # Second Image
        img2 = Image.open(r"D:\IdetectFace\images\img2.jpg")
        img2 = img2.resize((500,130))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=970,y=0,width=500,height=130)

        # Background Image
        img3 = Image.open(r"D:\IdetectFace\images\img-bg.jpg")
        img3 = img3.resize((1920,1080))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=-65,y=130,width=1500,height=700)


        # Attention

        title_lbl = Label(bg_img,text="AN AUTOMATED ATTENDANCE SYSTEM",font=("Gotham",25,"bold"),bg="#121212",fg="white")
        title_lbl.place(x=0,y=0,width=1500,height=45)

        # Student Details Button
        img4 = Image.open(r"D:\IdetectFace\images\img4.jpg")
        img4 = img4.resize((120,120))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=250,y=100,width=120,height=120)

        b_1 = Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("Nexa",10),bg="#121212",fg="white")
        b_1.place(x=250,y=200,width=120,height=25)

        # Face Detector Button
        img5 = Image.open(r"D:\IdetectFace\images\img5.jpg")
        img5 = img5.resize((130,160))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=550,y=100,width=120,height=120)

        b_1 = Button(bg_img,text="Face Detector",cursor="hand2",font=("Nexa",10),bg="#121212",fg="white")
        b_1.place(x=550,y=200,width=120,height=25)

        # Attendance Button
        img6 = Image.open(r"D:\IdetectFace\images\img6.jpg")
        img6 = img6.resize((120,120))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=850,y=100,width=120,height=120)

        b_1 = Button(bg_img,text="Attendance",cursor="hand2",font=("Nexa",10),bg="#121212",fg="white")
        b_1.place(x=850,y=200,width=120,height=25)

        # Help Desk Button
        img7 = Image.open(r"D:\IdetectFace\images\img7.jpg")
        img7 = img7.resize((120,120))
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1150,y=100,width=120,height=120)

        b_1 = Button(bg_img,text="Help Desk",cursor="hand2",font=("Nexa",10),bg="#121212",fg="white")
        b_1.place(x=1150,y=200,width=120,height=25)

        # Train Button
        img8 = Image.open(r"D:\IdetectFace\images\img8.jpg")
        img8 = img8.resize((120,120))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=250,y=320,width=120,height=120)

        b_1 = Button(bg_img,text="Train Data",cursor="hand2",font=("Nexa",10),bg="#121212",fg="white")
        b_1.place(x=250,y=420,width=120,height=25)

        # Photos Button
        img9 = Image.open(r"D:\IdetectFace\images\img9.jpg")
        img9 = img9.resize((120,120))
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=550,y=320,width=120,height=120)

        b_1 = Button(bg_img,text="Photos",cursor="hand2",font=("Nexa",10),bg="#121212",fg="white")
        b_1.place(x=550,y=420,width=120,height=25)

        # Developer Button
        img10 = Image.open(r"D:\IdetectFace\images\img10.jpg")
        img10 = img10.resize((120,120))
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=850,y=320,width=120,height=120)

        b_1 = Button(bg_img,text="Developer",cursor="hand2",font=("Nexa",10),bg="#121212",fg="white")
        b_1.place(x=850,y=420,width=120,height=25)

        # Exit Button
        img11 = Image.open(r"D:\IdetectFace\images\img11.jpg")
        img11 = img11.resize((120,120))
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1150,y=320,width=120,height=120)

        b_1 = Button(bg_img,text="Exit",cursor="hand2",font=("Nexa",10),bg="#121212",fg="white")
        b_1.place(x=1150,y=420,width=120,height=25)

    # ******* Fucntion Buttons********

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)






if __name__ == "__main__":
    root = Tk()
    obj = Face_recognization_System(root)
    root.mainloop()