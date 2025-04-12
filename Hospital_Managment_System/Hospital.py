from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1640x900+0+0")

        self.Nameoftablets = StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.PatientName=StringVar()
        self.nhsNumber=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()


        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)


     #   ====================DATAFRAME=======================
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1630,height=400)

        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",15,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=980,height=350)

        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",15,"bold"),text="Prescription")

        DataframeRight.place(x=990,y=5,width=600,height=350)

    #  ======================ButtonsFrame======================

        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1630,height=70)

    #  ======================DetailsFrame======================

        Detailframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailframe.place(x=0,y=600,width=1630,height=280)
    
    #  ======================DataFrameLeft======================
    
        lblNameTablet=Label(DataframeLeft,text="Names of Tablet",font=("arial",12,"bold"),padx=2,pady=6 )
        lblNameTablet.grid(row=0,column=0)

        comNametablet=ttk.Combobox(DataframeLeft,textvariable=self.Nameoftablets,state="readonly",font=("arial",12,"bold"),width=33)
        comNametablet["values"]=("Corona Vacacine","Acetaminophen","Adderall","Amitriptyline","Amlodipine","Amoxicillin","Ativan","Atorvastatin","Azithromycin")
        comNametablet.current(0)
        comNametablet.grid(row=0,column=1)

        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Reference No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft,textvariable=self.ref,font=("arial",12,"bold"),width=35)
        txtref.grid(row=1,column=1)

        lblDose=Label(DataframeLeft,font=("arial",12,"bold"),text="Dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,textvariable=self.Dose,font=("arial",12,"bold"),width=35)
        txtDose.grid(row=2,column=1)

        lblNoOftablets=Label(DataframeLeft,font=("arial",12,"bold"),text="No of Tablets:",padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        lblNoOftablets=Entry(DataframeLeft,textvariable=self.NumberofTablets,font=("arial",12,"bold"),width=35)
        lblNoOftablets.grid(row=3,column=1)

        lblLot=Label(DataframeLeft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        lblLot=Entry(DataframeLeft,textvariable=self.Lot,font=("arial",12,"bold"),width=35)
        lblLot.grid(row=4,column=1)

        lblissueDate=Label(DataframeLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        lblissueDate=Entry(DataframeLeft,textvariable=self.Issuedate,font=("arial",12,"bold"),width=35)
        lblissueDate.grid(row=5,column=1)

        lblExpDate=Label(DataframeLeft,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        lblExpDate=Entry(DataframeLeft,textvariable=self.ExpDate,font=("arial",12,"bold"),width=35)
        lblExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataframeLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        lblDailyDose=Entry(DataframeLeft,textvariable=self.DailyDose,font=("arial",12,"bold"),width=35)
        lblDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(DataframeLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        lblSideEffect=Entry(DataframeLeft,textvariable=self.sideEffect,font=("arial",12,"bold"),width=35)
        lblSideEffect.grid(row=8,column=1)

        lblFurtherinfo=Label(DataframeLeft,font=("arial",12,"bold"),text="Further Information:",padx=2)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        lblFurtherinfo=Entry(DataframeLeft,textvariable=self.FurtherInformation,font=("arial",12,"bold"),width=35)
        lblFurtherinfo.grid(row=0,column=3)

        lblBloodPressure=Label(DataframeLeft,font=("arial",12,"bold"),text="Blood Pressure:",padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        lblBloodPressure=Entry(DataframeLeft,textvariable=self.DrivingUsingMachine,font=("arial",12,"bold"),width=35)
        lblBloodPressure.grid(row=1,column=3)

        lblStorage=Label(DataframeLeft,font=("arial",12,"bold"),text="Storage Advice:",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        lblStorage=Entry(DataframeLeft,textvariable=self.StorageAdvice,font=("arial",12,"bold"),width=35)
        lblStorage.grid(row=2,column=3)

        lblMedicine=Label(DataframeLeft,font=("arial",12,"bold"),text="Medication:",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        lblMedicine=Entry(DataframeLeft,textvariable=self.HowToUseMedication,font=("arial",12,"bold"),width=35)
        lblMedicine.grid(row=3,column=3)

        lblPatientId=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Id:",padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        lblPatientId=Entry(DataframeLeft,textvariable=self.PatientId,font=("arial",12,"bold"),width=35)
        lblPatientId.grid(row=4,column=3)

        lblnhsNumber=Label(DataframeLeft,font=("arial",12,"bold"),text="NHS Number:",padx=2,pady=6)
        lblnhsNumber.grid(row=5,column=2,sticky=W)
        lblnhsNumber=Entry(DataframeLeft,textvariable=self.nhsNumber,font=("arial",12,"bold"),width=35)
        lblnhsNumber.grid(row=5,column=3)

        lblPatientname=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Name:",padx=2,pady=6)
        lblPatientname.grid(row=6,column=2,sticky=W)
        lblPatientname=Entry(DataframeLeft,textvariable=self.PatientName,font=("arial",12,"bold"),width=35)
        lblPatientname.grid(row=6,column=3)

        lblDateOfBirth=Label(DataframeLeft,font=("arial",12,"bold"),text="Date of Birth:",padx=2,pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        lblDateOfBirth=Entry(DataframeLeft,textvariable=self.DateOfBirth,font=("arial",12,"bold"),width=35)
        lblDateOfBirth.grid(row=7,column=3)

        lblPatientAddress=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Address:",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        lblPatientAddress=Entry(DataframeLeft,textvariable=self.PatientAddress,font=("arial",12,"bold"),width=35)
        lblPatientAddress.grid(row=8,column=3)

     #  ======================DataFrameRight======================

        self.txtPrescription=Text(DataframeRight,font=("arial",12,"bold"),width=62,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)


    #   ===========================Buttons========================

        btnPrescription=Button(Buttonframe,command=self.iPrectioption,font=("arial",12,"bold"),text="Prescription",background="green",foreground="white",width=25,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData=Button(Buttonframe,command=self.iPrescriptionData,font=("arial",12,"bold"),text="Prescription Data",background="green",foreground="white",width=25,padx=2,pady=6)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate=Button(Buttonframe,command=self.Update_data,font=("arial",12,"bold"),text="Update",background="green",foreground="white",width=26,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Buttonframe,command=self.idelete,font=("arial",12,"bold"),text="Delete",background="green",foreground="white",width=26,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(Buttonframe,command=self.clear,font=("arial",12,"bold"),text="Clear",background="green",foreground="white",width=25,padx=2,pady=6)
        btnClear.grid(row=0,column=4)

        btnExit=Button(Buttonframe,command=self.iExit,font=("arial",12,"bold"),text="Exit",background="green",foreground="white",width=25,padx=2,pady=6)
        btnExit.grid(row=0,column=5)

    #   ===========================Table===========================
    #   ===========================Scrollbar=======================

        scroll_x=ttk.Scrollbar(Detailframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailframe,columns=("nameoftablets","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack=(side:=BOTTOM,fill:=X)
        scroll_y.pack=(side:=RIGHT,fill:=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)
        
        self.hospital_table.heading("nameoftablets",text="Name of Tablets")
        self.hospital_table.heading("ref",text="Reference No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Date")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="Date of Birth")
        self.hospital_table.heading("address",text="Address")

        self.hospital_table["show"]="headings"

        self.hospital_table.column("nameoftablets",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fatch_data()

        

    #   ===========================Functionality Declaration===============

    def iPrescriptionData(self):
        if self.Nameoftablets  .get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="rushi@8793",database="rushi")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.Nameoftablets.get(),
                                                                                                    self.ref.get(),
                                                                                                    self.Dose.get(),
                                                                                                    self.NumberofTablets.get(),
                                                                                                    self.Lot.get(),
                                                                                                    self.Issuedate.get(),
                                                                                                    self.ExpDate.get(),
                                                                                                    self.DailyDose.get(),
                                                                                                    self.StorageAdvice.get(),
                                                                                                    self.nhsNumber.get(),
                                                                                                    self.PatientName.get(),
                                                                                                    self.DateOfBirth.get(),
                                                                                                    self.PatientAddress.get() 
                                                                                                    
                                                                                                    ))
                
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted")

    def Update_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="rushi@8793",database="rushi")
        my_cursor=conn.cursor()
        my_cursor.execute("update hospital set NameofTablets=%s,Dose=%s,Numbersoftablets=%s,lot=%s,issuedate=%s,expdate=%s,dailydose=%s,storage=%s,nhsnumber=%s,patientname=%s,DOB=%s,Patientaddress=%s where ReferenceNo=%s",(
                                                                                                                                                                                                                    self.Nameoftablets.get(),
                                                                                                                                                                                                                    
                                                                                                                                                                                                                    self.Dose.get(),
                                                                                                                                                                                                                    self.NumberofTablets.get(),
                                                                                                                                                                                                                    self.Lot.get(),
                                                                                                                                                                                                                    self.Issuedate.get(),
                                                                                                                                                                                                                    self.ExpDate.get(),
                                                                                                                                                                                                                    self.DailyDose.get(),
                                                                                                                                                                                                                    self.StorageAdvice.get(),
                                                                                                                                                                                                                    self.nhsNumber.get(),
                                                                                                                                                                                                                    self.PatientName.get(),
                                                                                                                                                                                                                    self.DateOfBirth.get(),
                                                                                                                                                                                                                    self.PatientAddress.get(), 
                                                                                                                                                                                                                    self.ref.get()
                                                                                                                                                                                                                        
                                                                                                                                                                                                                        ))
        conn.commit()
        self.fatch_data()
        conn.close()
        messagebox.showinfo("Update","Record has been updated Successfully")



    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="rushi@8793",database="rushi")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()


  

    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])


    def iPrectioption(self):
        self.txtPrescription.insert(END,"name Of Tablets:\t\t\t"+self.Nameoftablets.get()+"\n")
        self.txtPrescription.insert(END,"Reference No:\t\t\t" + self.ref.get() + "\n")
        self.txtPrescription.insert(END,"Dose:\t\t\t"+self.Dose.get() +"\n")
        self.txtPrescription.insert(END,"Number of Tablets:\t\t\t" + self.NumberofTablets.get() + "\n")
        self.txtPrescription.insert(END,"Lot: \t\t\t" + self.Lot.get() + "\n")
        self.txtPrescription.insert(END,"Issue Date: \t\t\t" + self.Issuedate.get() + "\n")
        self.txtPrescription.insert(END,"Exp Date:\t\t\t" + self.ExpDate.get() + "\n")
        self.txtPrescription.insert(END,"Daily Dose:\t\t\t" + self.DailyDose.get() + "\n")
        self.txtPrescription.insert(END,"Side Effect:\t\t\t" + self.sideEffect.get() + "\n")
        self.txtPrescription.insert(END,"Further Information:\t\t\t" + self.FurtherInformation.get() + "\n")
        self.txtPrescription.insert(END,"Storage Advice:\t\t\t" + self.StorageAdvice.get() + "\n")
        self.txtPrescription.insert(END,"DrivingUsingMAchine:\t\t\t" + self.DrivingUsingMachine.get() + "\n")
        self.txtPrescription.insert(END,"PatientId:\t\t\t" + self.PatientId.get() + "\n")
        self.txtPrescription.insert(END,"NHS Number:\t\t\t" + self.nhsNumber.get() + "\n")
        self.txtPrescription.insert(END,"Patient Name:\t\t\t" + self.PatientName.get() + "\n")
        self.txtPrescription.insert(END,"Date OF Birth:\t\t\t" + self.DateOfBirth.get() + "\n")
        self.txtPrescription.insert(END,"PatientAddress:\t\t\t" + self.PatientAddress.get() + "\n")


    def idelete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="rushi@8793",database="rushi")
        my_cursor=conn.cursor()
        query="delete from hospital where ReferenceNo=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fatch_data()
        messagebox.showinfo("Delete","Patient has been deleted Successfully!")


    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.sideEffect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0",END)

    def iExit(self):
        iExit=messagebox.askyesno("Hospital Management System","Confirm you want to exit")
        if iExit>0:
            root.destroy()
            return



root=Tk()
ob=Hospital(root)
root.mainloop()
