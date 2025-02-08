
	
from tkinter import*
import csv
from tkinter.messagebox import*
from tkinter.scrolledtext import*
from sqlite3 import *
import pandas as pd
import matplotlib.pyplot as plt
import requests



def f1():
	root.withdraw()
	aw.deiconify()
def f2():
	aw.withdraw()
	root.deiconify()

def f3():
	root.withdraw()
	vw.deiconify()
	vw_st_data.delete(1.0,END)
	con = None
	try:
		con = connect("ke.db")
		cursor = con.cursor()
		sql = "select * from emp"
		cursor.execute(sql)
		data = cursor.fetchall()
		info = ""
		for d in data:
			info = info + "_id="+ str(d[0]) +"   name ="+ str(d[1]) + "   salary ="+ str(d[2]) +"\n"
		vw_st_data.insert(INSERT,info)
	except Exception as e:
		showerror("issue",e)
	finally:
		if con is not None:
			con.close()


def f4():
	vw.withdraw()
	root.deiconify()
def f5():
	con= None
	try:
		con= connect("ke.db")
		cursor=con.cursor()
		sql="insert into emp values('%d','%s','%f')"
		id= int(aw_ent_id.get())
		idstr= str(id)
		name= aw_ent_name.get()
		salary= float(aw_ent_salary.get())
		
		if id <= 0:
			raise Exception("Invalid id","enter positive integers")
		else:
			pass
		if name == "":
			raise Exception("please enter name")
		if (name.isalpha()): 	
			pass
		else:
			raise Exception("invalid name")
		if (len(name) >= 2):	
			pass
		else:
			raise Exception("invalid name","minimum 2 alphabetes")	
		
		if (salary <= 8000.0):
			raise Exception("invalid salary", "minimum salary should be 8000")
		else:
			pass
		cursor.execute(sql %(id,name,salary))
		con.commit()
		showinfo("Success","record created")
	except ValueError:
		showerror("Invalid ","input cannot be empty")
		
	except Exception as e:
		con.rollback()
		showerror("Failed",e)
	finally:
		if con is not None:
			con.close()
		aw_ent_id.delete(0,END)
		aw_ent_name.delete(0,END)
		aw_ent_salary.delete(0,END)
		aw_ent_id.focus()
def f6():
	root.withdraw()
	uw.deiconify()

def f7():
	uw.withdraw()
	root.deiconify()



def f8():
	con =None
	try:
		con = connect("ke.db")
		cursor = con.cursor()
		sql = "update emp set name ='%s', salary = '%d'where id ='%d'" 
		id = int(uw_ent_id.get())
		idstr = str(id)
		name= uw_ent_name.get()
		salary= float(uw_ent_salary.get())
		
		if id <= 0:
			raise Exception("Invalid id","enter only positive integers")
		else:
			pass
		if name == "":
			raise Exception("please enter name")
		if (name.isalpha()):  	
			pass
		else:
			raise Exception("invalid name")
		if (len(name) >= 2):
			pass
		else:
			raise Exception("invalid name","minimum 2 alphabetes")	
		
		if (salary <= 8000.0):
			raise Exception("invalid salary", "minimum salary should be 8000")
		else:
			pass
			cursor.execute(sql %(name,salary,id))
	
		if cursor.rowcount == 1:
			con.commit()
			showinfo("Success","record updated")
			
		else:
			
			raise Exception("failed","does not exists")
			
	except ValueError:
		showerror("Invalid ","input cannot be empty")
		
		
		
	except Exception as e:
		con.rollback()
		showerror("Failed",e)
	finally:
		if con is not None:
			con.close()
		uw_ent_id.delete(0,END)
		uw_ent_name.delete(0,END)
		uw_ent_salary.delete(0,END)
		uw_ent_id.focus()
		
		


def f9():
	root.withdraw()
	dw.deiconify()

def f10():
	dw.withdraw()
	root.deiconify()

def f11():
	con = None
	try:
		con = connect("ke.db")
		cursor = con.cursor()
		sql = "delete from emp  where id = '%d'"
		id = int(dw_ent_id.get())
		cursor.execute( sql % (id))
		if cursor.rowcount == 1:
			con.commit()
			showinfo("Success","record deleted")
		else:
			showerror("Wrong","record does not exists")
	except Exception as e:
		con.rollback()
		print("issue",e)
	finally:
		if con is not None:
			con.close()
		dw_ent_id.delete(0,END)
		dw_ent_id.focus()
	
	
def f12():
	root.withdraw()
	cw.deiconify()
	
	try:
		con = connect("ke.db")
		cursor = con.cursor()
		sql = "select id,name,salary from emp order by salary desc limit 5"
		cursor.execute(sql)
		with open("data.csv",'w',newline='') as csv_file:
			csv_writer = csv.writer(csv_file)
			csv_writer.writerow([i[0] for i in cursor.description])
			csv_writer.writerows(cursor)
			print("csv created")

		data= pd.read_csv("data.csv")
		id= data["id"]
		name= data["name"]
		salary=data["salary"]

		plt.bar(name,salary,width=0.30,color="green")
		plt.xlabel("name")
		plt.ylabel("salary")
		plt.title("Top 5 highest earning salaried employee")

		plt.show()	
	except Exception as e:
		print("issue",e)
	finally:
		if con is not None:
			con.close()
def f13():
	root.deiconify()
	cw.withdraw()





root = Tk()
root.title("E.M.S")
root.geometry("900x700+100+100")
f = ("Arial",30,"bold")
#root.iconbitmap("new.date.ico.ico")

bg = PhotoImage(file ="img1.png")
label1 = Label(root,image = bg)
label1.place(x = 0,y = 0)

btn_add = Button(root,text = "Add",font = f,bd = 2,width = 10,command = f1)
btn_add.pack(pady = 10)
btn_view = Button(root,text = "View",font = f,bd = 2,width = 10,command = f3)
btn_view.pack(pady = 10)
btn_update = Button(root,text = "Update",font = f,bd = 2,width = 10,command = f6)
btn_update.pack(pady = 10)
btn_delete = Button(root,text = "Delete",font = f,bd = 2,width = 10,command = f9)
btn_delete.pack(pady = 10)
btn_charts = Button(root,text = "Charts",font = f,bd = 2,width = 10,command = f12)
btn_charts.pack(pady = 10)


lab_loc = Label(root, text="Location:",font = f)
lab_loc.place(x = 10,y = 570)
text_msg = Entry(root,text ="",font = f,width = 10)
text_msg.place(x = 200,y = 570)

try:
	wa = "https://ipinfo.io/"
	res = requests.get(wa)
	data = res.json()
	city= data["city"]
	text_msg.insert(INSERT,city)
	
except Exception as e:
	print("issue",e)




lab_temp =Label(root,text ="Temp:",font = f)
lab_temp.place(x = 500 ,y = 570)
text_msg = Entry(root,font = f,text = "",width = 7)
text_msg.place(x = 630,y = 570)

try:
	api_key = '433f8ab0a1b3f81f3abe37a6fa2eb8eb'
	city = 'Thane,india'
	wa = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
	res = requests.get(wa)
	data = res.json()
	temp = data["main"]["temp"] - 273.15
	temp = round(temp,2)
	text_msg.insert(INSERT,temp)
except Exception as e:
	print("issue",e)


aw = Toplevel(root)
aw.title("Add Emp")
aw.geometry("500x700+50+50")
#aw.iconbitmap("new_emp.ico.ico")

aw_lab_id = Label(aw,text ="enter id:",font = f,width = 10)
aw_lab_id.pack(pady = 10)
aw_ent_id = Entry(aw,font = f)
aw_ent_id.pack(pady = 10)

aw_lab_name = Label(aw,text ="enter name:",font = f,width = 10)
aw_lab_name.pack(pady = 10)
aw_ent_name = Entry(aw,font = f)
aw_ent_name.pack(pady = 10)

aw_lab_salary = Label(aw, text ="enter salary:",font = f,width = 10)
aw_lab_salary.pack(pady = 10)
aw_ent_salary = Entry(aw,font = f)
aw_ent_salary.pack(pady = 10)

aw_btn_save = Button(aw,text ="Save",font = f,width = 7,command = f5)
aw_btn_save.pack(pady = 10)
aw_btn_back = Button(aw,text = "Back",font = f,width = 7,command = f2)
aw_btn_back.pack(pady = 10)

aw.withdraw()

vw = Toplevel(root)
vw.title("View Emp ")
vw.geometry("700x600+100+100")

vw_st_data = ScrolledText(vw,font = f,width = 30,height = 10)
vw_st_data.pack()
vw_btn_back = Button(vw,text ="Back",width = 7,font = f,command = f4)
vw_btn_back.pack(pady = 10)

vw.withdraw()

uw = Toplevel(root)
uw.title("Update Emp")
uw.geometry("500x700+50+50")


uw_lab_id = Label(uw,text ="enter id:",font = f,width = 15)
uw_lab_id.pack(pady = 10)
uw_ent_id = Entry(uw,font = f)
uw_ent_id.pack(pady = 10)


uw_lab_name = Label(uw,text ="enter name:",font = f,width = 15)
uw_lab_name.pack(pady = 10)
uw_ent_name = Entry(uw,font = f)
uw_ent_name.pack(pady = 10)


uw_lab_salary = Label(uw,text = "enter salary:",font = f,width = 15)
uw_lab_salary.pack(pady = 10)
uw_ent_salary = Entry(uw,font = f)
uw_ent_salary.pack(pady = 10)


uw_btn_save = Button(uw, text="Save",font = f,width = 7,command = f8)
uw_btn_save.pack(pady = 10)
uw_btn_back = Button(uw,text ="Back",font = f,width = 7,command = f7)
uw_btn_back.pack(pady = 10)


uw.withdraw()


dw = Toplevel(root)
dw.title("Delete Emp")
dw.geometry("500x600+50+50")


dw_lab_id = Label(dw,text ="enter id:",font = f,width = 15)
dw_lab_id.pack(pady = 10)
dw_ent_id = Entry(dw,font = f)
dw_ent_id.pack(pady = 10)

dw_btn_save = Button(dw,text ="Save",font = f ,width = 7,command = f11)
dw_btn_save.pack(pady = 10)
dw_btn_back = Button(dw,text ="Back",font = f,width = 7,command = f10)
dw_btn_back.pack(pady = 10)


dw.withdraw()


cw = Toplevel(root)
cw.title("Charts")
cw.geometry("500x600+50+50")


cw_btn_back = Button(cw,text ="Back",font = f,width = 7,command = f13)
cw_btn_back.pack(pady = 20)


cw.withdraw()


root.mainloop()