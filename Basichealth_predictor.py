from tkinter import *
from tkinter import ttk
import mysql.connector

base=Tk()
base.geometry("900x780")


connect_pd=mysql.connector.connect(host='localhost',user='root',port='3306',database='healthpredicter')
cpd=connect_pd.cursor()

# connect_hd=mysql.connector.connect(host='localhost',user='base',port='3306',database='healthpredicter')
# chd=connect_pd.cursor()

#background canvas
back_cv = Canvas(base, bg="#363062",height=790, width=1600)
back_cv.place(x=0,y=0)

#headercanvas
head_cv=Canvas(back_cv,bg="#F5E8C7",height=50,width=1480)
head_cv.place(x=30,y=5)

heading=Label(head_cv,text="BASIC HEALTH PREDICTOR",bg="#F5E8C7",fg="#363062",font=("Cinzel Black",35,"bold"))
heading.place(x=400,y=0)

#function for displaying personal details
def display_pd():
    p_id=id_e.get()
    p_name=id_n.get()
    p_email=id_eid.get()
    p_phone=id_phno.get()
    p_addr=id_ad.get()
    p_gen=gender_combox.get()
    p_age=id_ag.get()
    p_pin=id_pin.get()

    tree = ttk.Treeview(pd_cvo)
    tree["columns"] = ("ID","NAME", "EMAIL","PHONE NO","ADDRESS", "GENDER","AGE", "PINCODE", )

    tree.heading("#0", text="", anchor="w")
    tree.column("#0", anchor="w", width=0)
    tree.heading("ID", text="ID")
    tree.column("ID", anchor="center",stretch=NO, width=50)
    tree.heading("NAME", text="NAME")
    tree.column("NAME", anchor="center",stretch=NO, width=100)
    tree.heading("EMAIL", text="EMAIL")
    tree.column("EMAIL", anchor="center",stretch=NO, width=100)
    tree.heading("PHONE NO", text="PHONE NO")
    tree.column("PHONE NO", anchor="center",stretch=NO, width=100)
    tree.heading("ADDRESS", text="ADDRESS")
    tree.column("ADDRESS", anchor="center",stretch=NO, width=100)
    tree.heading("GENDER", text="GENDER")
    tree.column("GENDER", anchor="center",stretch=NO, width=75)
    tree.heading("AGE", text="AGE")
    tree.column("AGE", anchor="center",stretch=NO, width=30)
    tree.heading("PINCODE", text="PINCODE")
    tree.column("PINCODE", anchor="center",stretch=NO, width=90)

    data = [(p_id,p_name,p_email,p_phone,p_addr,p_gen,p_age,p_pin)]

    for i, (id, name ,email,phone_no,address,gen,age,pin) in enumerate(data, start=1):
        tree.insert("", i, values=(id, name ,email,phone_no,address,gen,age,pin))

    tree.place(x=40,y=50)

    insert_query = "INSERT INTO `personal_details`(`id`, `Name`, `Email Id`, `Phone No`, `Address`, `Gender`, `Age`, `Pincode`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    vals = (p_id,p_name,p_email,p_phone,p_addr,p_gen,p_age,p_pin)
    cpd.execute(insert_query, vals)
    connect_pd.commit()

#function for displaying health details
def display_hd():
    p_id=id_e.get()
    p_temp=temp_e.get()
    p_hr=hr_n.get()
    p_bp=bp_e.get()
    p_chol=chol_e.get()
    p_fact=fact_combox.get()
    p_sug=sug_e.get()
    p_weg=weg_e.get()

    tree = ttk.Treeview(hd_cvo)
    tree["columns"] = ("ID","BODY TEMP","HEART RATE", "BLOOD PRESSURE","CHOLESTROL LEVEL","LIFESTYLE", "SUGAR LEVEL", "WEIGHT" )

    tree.heading("#0", text="", anchor="w")
    tree.column("#0", anchor="w", width=0)
    tree.heading("ID", text="ID")
    tree.column("ID", anchor="center", stretch=NO, width=50)
    tree.heading("BODY TEMP", text="BODY TEMP")
    tree.column("BODY TEMP", anchor="center",stretch=NO, width=50)
    tree.heading("HEART RATE", text="HEART RATE")
    tree.column("HEART RATE", anchor="center",stretch=NO, width=100)
    tree.heading("BLOOD PRESSURE", text="BLOOD PRESSURE")
    tree.column("BLOOD PRESSURE", anchor="center",stretch=NO, width=100)
    tree.heading("CHOLESTROL LEVEL", text="CHOLESTROL LEVEL")
    tree.column("CHOLESTROL LEVEL", anchor="center",stretch=NO, width=100)
    tree.heading("LIFESTYLE", text="LIFESTYLE")
    tree.column("LIFESTYLE", anchor="center",stretch=NO, width=100)
    tree.heading("SUGAR LEVEL", text="SUGAR LEVEL")
    tree.column("SUGAR LEVEL", anchor="center",stretch=NO, width=100)
    tree.heading("WEIGHT", text="WEIGHT")
    tree.column("WEIGHT", anchor="center",stretch=NO, width=50)

    data = [(p_id,p_temp,p_hr,p_bp,p_chol,p_fact,p_sug,p_weg)]

    for i, (id,temp, heart_rate ,bp,chol,fact,sugar,wegight) in enumerate(data, start=1):
        tree.insert("", i, values=(id,temp, heart_rate ,bp,chol,fact,sugar,wegight))

    tree.place(x=20,y=50)

    insert_query ="INSERT INTO `health_details`(`id`, `Body temperature`, `Heart rate`, `Blood pressure`, `Cholestrol Level`, `Lifestyle`, `Sugar Level`, `Previous/any issues`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    vals = (id,p_temp,p_hr,p_bp,p_chol,p_fact,p_sug,p_weg)
    cpd.execute(insert_query, vals)
    connect_pd.commit()


#personal details canvas
pd_cv=Canvas(back_cv,bg="#435585",height=320,width=740)
pd_cv.place(x=20,y=65)

pd_head=Label(pd_cv,text="PERSONAL DETAILS :",bg="#F5E8C7",fg="#363062",font=("Cinzel Black",15,"bold"))
pd_head.place(x=5,y=5)

id=Label(pd_cv,text="PATIENT iD :",bg="#818FB4",fg="#363062",font=("Cinzel Black",10,"bold"))
id.place(x=40,y=55)
id_e=Entry(pd_cv)
id_e.place(x=40,y=85)

full_name=Label(pd_cv,text="NAME :",bg="#818FB4",fg="#363062",font=("Cinzel Black",10,"bold"))
full_name.place(x=200,y=55)
id_n=Entry(pd_cv)
id_n.place(x=200,y=85)

email=Label(pd_cv,text="EMAIL iD :",bg="#818FB4",fg="#363062",font=("Cinzel Black",10,"bold"))
email.place(x=350,y=55)
id_eid=Entry(pd_cv)
id_eid.place(x=350,y=85)

phone=Label(pd_cv,text="PHONE No :",bg="#818FB4",fg="#363062",font=("Cinzel Black",10,"bold"))
phone.place(x=530,y=55)
id_phno=Entry(pd_cv)
id_phno.place(x=530,y=85)

addr=Label(pd_cv,text="ADDRESS :",bg="#818FB4",fg="#363062",font=("Cinzel Black",10,"bold"))
addr.place(x=40,y=125)
id_ad=Entry(pd_cv)
id_ad.place(x=40,y=155)

gender=Label(pd_cv,text="GENDER :",bg="#818FB4",fg="#363062",font=("Cinzel Black",10,"bold"))
gender.place(x=200,y=125)
gender_combox=ttk.Combobox(pd_cv,values=[" ","Male","Female"])
gender_combox.place(x=200,y=155)
#id_gen=Entry(pd_cv).place(x=200,y=155)

age=Label(pd_cv,text="AGE :",bg="#818FB4",fg="#363062",font=("Cinzel Black",10,"bold"))
age.place(x=350,y=125)
id_ag=Entry(pd_cv)
id_ag.place(x=350,y=155)

pincode=Label(pd_cv,text="PINCODE:",bg="#818FB4",fg="#363062",font=("Cinzel Black",10,"bold"))
pincode.place(x=530,y=125)
id_pin=Entry(pd_cv)
id_pin.place(x=530,y=155)

enter=Button(pd_cv,text="ENTER",bg="#F5E8C7",fg="#363062",font=("Cinzel Black",10,"bold"),command=display_pd)
enter.place(x=320,y=250)

# for widget in pd_cv.winfo_children():
#     widget.grid_configure(padx=0, pady=0)


#health details canvas
hd_cv=Canvas(back_cv,bg="#435585",height=320,width=740)
hd_cv.place(x=20,y=400)

hd_head=Label(hd_cv,text="HEALTH DETAILS :",bg="#F5E8C7",fg="#363062",font=("Cinzel Black",15,"bold"))
hd_head.place(x=5,y=5)

id=Label(hd_cv,text="PATIENT iD :",bg="#818FB4",fg="#363062",font=("Cinzel Black",10,"bold"))
id.place(x=40,y=55)
id_e=Entry(hd_cv)
id_e.place(x=40,y=85)

temp=Label(hd_cv,text="BODY TEMP :",bg="#818FB4",fg="#363062",font=("Cinzel Black",10,"bold"))
temp.place(x=200,y=55)
temp_e=Entry(hd_cv)
temp_e.place(x=200,y=85)

heart_rate=Label(hd_cv,text="HEART RATE :",bg="#818FB4",fg="#363062",font=("Cinzel Black",10,"bold"))
heart_rate.place(x=350,y=55)
hr_n=Entry(hd_cv)
hr_n.place(x=350,y=85)

bp=Label(hd_cv,text="BLOOD PRESSURE(BP) :",bg="#818FB4",fg="#363062",font=("Cinzel Black",10,"bold"))
bp.place(x=530,y=55)
bp_e=Entry(hd_cv)
bp_e.place(x=530,y=85)

cholestrol=Label(hd_cv,text="CHOLESTROL LEVEL :",bg="#818FB4",fg="#363062",font=("Cinzel Black",10,"bold"))
cholestrol.place(x=40,y=125)
chol_e=Entry(hd_cv)
chol_e.place(x=40,y=155)

factors=Label(hd_cv,text="LIFESTYLE(DIET,GYM/\nSMOKING etc) :",bg="#818FB4",fg="#363062",font=("Cinzel Black",10,"bold"))
factors.place(x=200,y=125)
fact_combox=ttk.Combobox(hd_cv,values=[" ","DIET","SMOKING","GYM","ALCOHOL","EXERCISE","YOGA"])
fact_combox.place(x=200,y=170)
#fact_id=Entry(hd_cv).place(x=40,y=170)

sugar=Label(hd_cv,text="SUGAR LEVEL :",bg="#818FB4",fg="#363062",font=("Cinzel Black",10,"bold"))
sugar.place(x=365,y=125)
sug_e=Entry(hd_cv)
sug_e.place(x=365,y=155)

# sym=Label(hd_cv,text="ANY SYMPTOMS/\nCHANGES :",bg="#818FB4",fg="#363062",font=("Cinzel Black",10,"bold"))
# sym.place(x=365,y=125)
# sym_e=Entry(hd_cv)
# sym_e.place(x=365,y=170)

weg=Label(hd_cv,text="WEIGHT :",bg="#818FB4",fg="#363062",font=("Cinzel Black",10,"bold"))
weg.place(x=530,y=125)
weg_e=Entry(hd_cv)
weg_e.place(x=530,y=155)

submit=Button(hd_cv,text="SUBMIT",bg="#F5E8C7",fg="#363062",font=("Cinzel Black",10,"bold"),command=display_hd)
submit.place(x=320,y=250)

#PD display canvas

pd_cvo=Canvas(back_cv,bg="#818FB4",height=320,width=740)
pd_cvo.place(x=780,y=65)

pdb_head=Label(pd_cvo,text="PERSONAL DETAILS(pre-view) :",bg="#F5E8C7",fg="#363062",font=("Cinzel Black",15,"bold"))
pdb_head.place(x=5,y=5)

#HD display canvas
hd_cvo=Canvas(back_cv,bg="#818FB4",height=320,width=740)
hd_cvo.place(x=780,y=400)

hdb_head=Label(hd_cvo,text="HEALTH DETAILS(pre-view) :",bg="#F5E8C7",fg="#363062",font=("Cinzel Black",15,"bold"))
hdb_head.place(x=5,y=5)

#footer canvas
foot_cv=Canvas(back_cv,bg="#F5E8C7",height=50,width=1480)
foot_cv.place(x=30,y=730)

predict=Button(foot_cv,text="PREDICT",bg="#F5E8C7",fg="#363062",font=("Cinzel Black",20,"bold"))
predict.place(x=665,y=0)




mainloop()