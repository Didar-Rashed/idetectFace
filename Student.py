from tkinter import*
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Student Management System")

        #****** Variables*******
        
        self.var_id = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_department = StringVar()
        self.var_course = StringVar()
        #self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_sassion = StringVar()
        self.var_section = StringVar()
        self.var_gender = StringVar()
        self.var_birth_date = StringVar()
        self.var_phone_no = StringVar()
        self.var_email = StringVar()
        self.var_blood_group = StringVar()
        self.var_teacher = StringVar()
        self.var_address = StringVar()
        self.var_radio = StringVar()


        # Zeroth Image
        img = Image.open(r"D:\IdetectFace\images\student-img.jpg")
        img = img.resize((500,110))
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=-30,y=0,width=500,height=110)

        # First Image
        img1 = Image.open(r"D:\IdetectFace\images\student-img1.jpg")
        img1 = img1.resize((500,110))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=470,y=0,width=500,height=110)

        # Second Image
        img2 = Image.open(r"D:\IdetectFace\images\student-img2.jpg")
        img2 = img2.resize((500,110))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=970,y=0,width=500,height=110)


        # Background Image
        img3 = Image.open(r"D:\IdetectFace\images\student-img-bg.jpg")
        img3 = img3.resize((1920,1080))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=-65,y=110,width=1500,height=700)


        # Attention

        title_lbl = Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("Gotham",24,"bold"),bg="#F5F7F8",fg="#4793AF")
        title_lbl.place(x=0,y=-10,width=1500,height=35)

        main_frame = Frame(bg_img,bd=2,bg="#F5F7F8")
        main_frame.place(x=86,y=20,width=1324,height=550)

        # Left side label frame
        left_frame = LabelFrame(main_frame,bd=2,bg="#F5F7F8",relief=RIDGE,text="Student Details",font=("Nexa",12))
        left_frame.place(x=10,y=10,width=640,height=530)

        img_left = Image.open(r"D:\IdetectFace\images\student-img3.jpg")
        img_left = img_left.resize((600,60))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=5,width=630,height=70)
        
        # Current Course Informaion
        current_course_frame = LabelFrame(left_frame,bd=2,bg="#F5F7F8",relief=RIDGE,text="Current Course Informaion",font=("Nexa",12))
        current_course_frame.place(x=5,y=75,width=620,height=100)

        # Department
        dept_label = Label(current_course_frame,text="Department",font=("Nexa",10),bg="white")
        dept_label.grid(row=0,column=0,padx=8)

        dept_combo = ttk.Combobox(current_course_frame,textvariable=self.var_department,font=("Nexa",10),width=16,state="Read Only")
        dept_combo["values"] = ("Select Department", "CSE","BBA","MBA","MSC")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=2,pady=8,sticky=W)

        # Course
        course_label = Label(current_course_frame,text="Course",font=("Nexa",10),bg="white")
        course_label.grid(row=0,column=2,padx=8,sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("Nexa",10),width=16,state="Read Only")
        course_combo["values"] = ("Select Course", "ISM","PDA","NIS")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=8,sticky=W)

        # Semester
        semester_label = Label(current_course_frame,text="Semester",font=("Nexa",10),bg="white")
        semester_label.grid(row=1,column=0,padx=8,sticky=W)

        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("Nexa",10),width=16,state="Read Only")
        semester_combo["values"] = ("Select Semester", "1st Semester","2nd Semester","3rd Semester","4th Semester","5th Semester","6th Semester","7th Semester","8th Semester")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=1,padx=2,pady=8,sticky=W)

        # Sassion
        sassion_label = Label(current_course_frame,text="Sassion",font=("Nexa",10),bg="white")
        sassion_label.grid(row=1,column=2,padx=8,sticky=W)

        sassion_combo = ttk.Combobox(current_course_frame,textvariable=self.var_sassion,font=("Nexa",10),width=16,state="Read Only")
        sassion_combo["values"] = ("Select Sassion", "2024-25","2023-24","2022-23","2021-22","2020-21","2019-20","2018-19","2017-18")
        sassion_combo.current(0)
        sassion_combo.grid(row=1,column=3,padx=2,pady=8,sticky=W)

        # Student Informaion
        student_info_frame = LabelFrame(left_frame,bd=2,bg="#F5F7F8",relief=RIDGE,text="Student Informaion",font=("Nexa",12))
        student_info_frame.place(x=5,y=180,width=620,height=320)

        # Student ID
        student_id_label = Label(student_info_frame,text="Student ID",font=("Nexa",10),bg="white")
        student_id_label.grid(row=0,column=0,padx=8,sticky=W)

        student_id_entry = ttk.Entry(student_info_frame,textvariable=self.var_id,width=16,font=("Nexa",10))
        student_id_entry.grid(row=0,column=1,padx=8,pady=5,sticky=W)

        # Student Name
        student_name_label = Label(student_info_frame,text="Student Name",font=("Nexa",10),bg="white")
        student_name_label.grid(row=0,column=2,padx=8,pady=5,sticky=W)

        student_name_entry = ttk.Entry(student_info_frame,textvariable=self.var_name,width=25,font=("Nexa",10))
        student_name_entry.grid(row=0,column=3,padx=8,pady=5,sticky=W)

        # Student Roll
        roll_no_label = Label(student_info_frame,text="Roll No",font=("Nexa",10),bg="white")
        roll_no_label.grid(row=1,column=0,padx=8,sticky=W)

        roll_no_entry = ttk.Entry(student_info_frame,textvariable=self.var_roll,width=16,font=("Nexa",10))
        roll_no_entry.grid(row=1,column=1,padx=8,pady=5,sticky=W)

        # Student Section
        section_label = Label(student_info_frame,text="Section",font=("Nexa",10),bg="white")
        section_label.grid(row=1,column=2,padx=8,sticky=W)

        #section_entry = ttk.Entry(student_info_frame,textvariable=self.var_section,width=25,font=("Nexa",10))
        #section_entry.grid(row=1,column=3,padx=8,pady=5,sticky=W)

        section_combo = ttk.Combobox(student_info_frame,textvariable=self.var_section,font=("Nexa",10),width=23,state="Read Only")
        section_combo["values"] = ("A", "B","C")
        section_combo.current(0)
        section_combo.grid(row=1,column=3,padx=8,sticky=W)

        # Student Gender
        gender_label = Label(student_info_frame,text="Gender",font=("Nexa",10),bg="white")
        gender_label.grid(row=2,column=0,padx=8,sticky=W)

        #gender_entry = ttk.Entry(student_info_frame,textvariable=self.var_gender,width=16,font=("Nexa",10))
        #gender_entry.grid(row=2,column=1,padx=8,pady=5,sticky=W)

        gender_combo = ttk.Combobox(student_info_frame,textvariable=self.var_gender,font=("Nexa",10),width=13,state="Read Only")
        gender_combo["values"] = ("Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=8,pady=5,sticky=W)


        # Student Date of Birth
        dob_label = Label(student_info_frame,text="Birth Date",font=("Nexa",10),bg="white")
        dob_label.grid(row=2,column=2,padx=8,sticky=W)

        dob_entry = ttk.Entry(student_info_frame,textvariable=self.var_birth_date,width=25,font=("Nexa",10))
        dob_entry.grid(row=2,column=3,padx=8,pady=5,sticky=W)

        # Student Phone Number
        phone_no_label = Label(student_info_frame,text="Phone No",font=("Nexa",10),bg="white")
        phone_no_label.grid(row=3,column=0,padx=8,sticky=W)

        phone_no_entry = ttk.Entry(student_info_frame,textvariable=self.var_phone_no,width=16,font=("Nexa",10))
        phone_no_entry.grid(row=3,column=1,padx=8,pady=5,sticky=W)

        # Student Email
        email_label = Label(student_info_frame,text="Email",font=("Nexa",10),bg="white")
        email_label.grid(row=3,column=2,padx=8,sticky=W)

        email_entry = ttk.Entry(student_info_frame,textvariable=self.var_email,width=25,font=("Nexa",10))
        email_entry.grid(row=3,column=3,padx=8,pady=5,sticky=W)

        # Student Blood Group
        blood_group_label = Label(student_info_frame,text="Blood Group",font=("Nexa",10),bg="white")
        blood_group_label.grid(row=4,column=0,padx=8,sticky=W)

        blood_group_entry = ttk.Entry(student_info_frame,textvariable=self.var_blood_group,width=16,font=("Nexa",10))
        blood_group_entry.grid(row=4,column=1,padx=8,pady=5,sticky=W)

        # Techer Name
        teacher_name_label = Label(student_info_frame,text="Teacher",font=("Nexa",10),bg="white")
        teacher_name_label.grid(row=4,column=2,padx=8,sticky=W)

        teacher_name_entry = ttk.Entry(student_info_frame,textvariable=self.var_teacher,width=25,font=("Nexa",10))
        teacher_name_entry.grid(row=4,column=3,padx=8,pady=5,sticky=W)

        # Student Address
        address_label = Label(student_info_frame,text="Adress",font=("Nexa",10),bg="white")
        address_label.grid(row=5,column=0,padx=8,sticky=W)

        address_entry = ttk.Entry(student_info_frame,textvariable=self.var_address,width=16,font=("Nexa",10))
        address_entry.grid(row=5,column=1,padx=8,pady=5,sticky=W)

        # Radio Button
        self.var_radio = StringVar()
        radio_btn1 = ttk.Radiobutton(student_info_frame,variable=self.var_radio,text="Photo Sample, Yes", value="Yes")
        radio_btn1.place(x=5,y=190)

        radio_btn2 = ttk.Radiobutton(student_info_frame,variable=self.var_radio,text="Photo Sample, No", value="No")
        radio_btn2.place(x=237,y=190)

        # Button Frame
        btn_frame = Frame(student_info_frame,relief=RIDGE,bg="white")
        btn_frame.place(x=6,y=215,width=602,height=35)

        save_btn = Button(btn_frame,text="Save",command=self.add_data,width=11,font="Nexa",bg="#65B741",fg="white")
        save_btn.grid(row=0,column=0,padx=19)

        update_btn = Button(btn_frame,text="Update",command=self.update_data,width=11,font="Nexa",bg="#279EFF",fg="white")
        update_btn.grid(row=0,column=1,padx=19)

        delete_btn = Button(btn_frame,text="Delete",command=self.delete_data,width=11,font="Nexa",bg="#DD5746",fg="white")
        delete_btn.grid(row=0,column=2,padx=19)

        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=11,font="Nexa",bg="#413F42",fg="white")
        reset_btn.grid(row=0,column=3,padx=19)

        # Button Fram Bottom
        btn_frame1 = Frame(student_info_frame,relief=RIDGE,bg="white")
        btn_frame1.place(x=6,y=250,width=602,height=35)

        take_photo_btn = Button(btn_frame1,text="Take Photo",width=27,font="Nexa",bg="#50727B",fg="white")
        take_photo_btn.grid(row=0,column=2,padx=19)

        upload_photo_btn = Button(btn_frame1,text="Upload Photo",width=27,font="Nexa",bg="#50727B",fg="white")
        upload_photo_btn.grid(row=0,column=3,padx=23,pady=5)

        # Right side label frame
        right_frame = LabelFrame(main_frame,bd=2,bg="#F5F7F8",relief=RIDGE,text="Student Details",font=("Nexa",12))
        right_frame.place(x=668,y=10,width=640,height=530)

        img_right = Image.open(r"D:\IdetectFace\images\student-img4.jpg")
        img_right = img_right.resize((600,60))
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=5,width=630,height=70)

        # ******* Searching System ******** #

        search_frame = LabelFrame(right_frame,bd=2,bg="#F5F7F8",relief=RIDGE,text="Search System",font=("Nexa",12))
        search_frame.place(x=5,y=75,width=620,height=65)

        earch_label = Label(search_frame,text="Search By",font=("Nexa",10),bg="white")
        earch_label.grid(row=0,column=0,padx=8,sticky=W)

        search_combo = ttk.Combobox(search_frame,font=("Nexa",10),width=10,state="Read Only")
        search_combo["values"] = ("Select", "ID No","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=8,sticky=W)


        search_entry = ttk.Entry(search_frame,width=22,font=("Nexa",10))
        search_entry.grid(row=0,column=2,padx=8,pady=5,sticky=W)

        search_btn = Button(search_frame,text="Seaech",width=11,font="Nexa",bg="#50727B",fg="white")
        search_btn.grid(row=0,column=3,padx=10)
        
        show_all_btn = Button(search_frame,text="Show All",width=11,font="Nexa",bg="#50727B",fg="white")
        show_all_btn.grid(row=0,column=4,padx=10)

        # Table Frame
        table_frame = Frame(right_frame,bd=2,bg="#F5F7F8",relief=RIDGE)
        table_frame.place(x=5,y=150,width=620,height=350)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,columns=("ID","Roll","Name","Department","Course","Semester","Sassion","Section","Gender","Birth Date","Phone No","Email","Blood Group","Teacher","Address","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("ID",text="ID")
        self.student_table.heading("Roll",text="Roll")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course",text="Course")
        #self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("Sassion",text="Sassion")
        self.student_table.heading("Section",text="Section")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Birth Date",text="Birth Date")
        self.student_table.heading("Phone No",text="Phone No")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Blood Group",text="Blood Group")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Photo",text="Photo")
        self.student_table["show"] = "headings"

        self.student_table.column("ID",width=100)
        self.student_table.column("Roll",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Department",width=100)
        self.student_table.column("Course",width=100)
        #self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("Sassion",width=100)
        self.student_table.column("Section",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Birth Date",width=100)
        self.student_table.column("Phone No",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Blood Group",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Photo",width=100)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #**************Function Declaration*****************

    def add_data(self):
        if self.var_department.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error","Check all the required fields",parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="2684",database="I-detectface")
                my_cursor = conn.cursor()
                my_cursor.execute("Insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                
                                                                                                            self.var_id.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_department.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_sassion.get(),
                                                                                                            self.var_section.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_birth_date.get(),
                                                                                                            self.var_phone_no.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_blood_group.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_radio.get()
                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added",parent = self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent = self.root)

    

    #************* Fetch Data ************
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="2684",database="I-detectface")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from student")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    #************ Get Data ************
    def get_cursor(self,event = ""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_id.set(data[0])
        self.var_roll.set(data[1])
        self.var_name.set(data[2])
        self.var_department.set(data[3])
        self.var_course.set(data[4])
        self.var_semester.set(data[5])
        self.var_sassion.set(data[6])
        self.var_section.set(data[7])
        self.var_gender.set(data[8])
        self.var_birth_date.set(data[9])
        self.var_phone_no.set(data[10])
        self.var_email.set(data[11])
        self.var_blood_group.set(data[12])
        self.var_teacher.set(data[13])
        self.var_address.set(data[14])
        self.var_radio.set(data[15])


    #******* Update Function ********
    def update_data(self):
        if self.var_department.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error","Check all the required fields",parent = self.root)
        else:
            try:
                Update = messagebox.askyesno("Update","Do you want update this student details?",parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="2684",database="I-detectface")
                    my_cursor = conn.cursor()
                    my_cursor.execute("Update student set Roll=%s,Name=%s,Department=%s,Course=%s,Semester=%s,Sassion=%s,Section=%s,Gender=%s,Birth_Date=%s,Phone_number=%s,Email=%s,Blood_Group=%s,Teacher=%s,Address=%s,Photo=%s where ID=%s",(
                                                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                                        self.var_name.get(),
                                                                                                                                                                                                                        self.var_department.get(),
                                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                                        self.var_sassion.get(),
                                                                                                                                                                                                                        self.var_section.get(),
                                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                                        self.var_birth_date.get(),
                                                                                                                                                                                                                        self.var_phone_no.get(),
                                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                                        self.var_blood_group.get(),
                                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                                        self.var_radio.get(),
                                                                                                                                                                                                                        self.var_id.get()
                                                                                                                                                                                                                    ))
                    
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                self.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent = self.root)


    # ****** Delete Data ********
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student id must be filled",parent=self.root)
        else:
            try:
                delete =messagebox.askyesno("Student Delete Page","Do you want to delete this student details?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="2684",database="I-detectface")
                    my_cursor = conn.cursor()
                    sql="delete from student where ID=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                messagebox.showinfo("Delete","Succesfully deleted student details",parent=self.root)
                conn.commit()
                self.fetch_data()
                self.close()
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent = self.root)


    # ****** Reset Function *******
    def reset_data(self):
        self.var_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_department.set("Select Department")
        self.var_course.set("Select Course")
        self.var_semester.set("Select Semester")
        self.var_sassion.set("Select Sassion")
        self.var_section.set("A")
        self.var_gender.set("Male")
        self.var_birth_date.set("")
        self.var_phone_no.set("")
        self.var_email.set("")
        self.var_blood_group.set("")
        self.var_teacher.set("")
        self.var_address.set("")
        self.var_radio.set("")
        







if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()