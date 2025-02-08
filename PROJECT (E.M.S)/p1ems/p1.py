from tkinter import *
from tkinter import messagebox
import sqlite3

# Initialize database
def init_db():
    con = sqlite3.connect("students.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS student (rno INTEGER PRIMARY KEY, name TEXT, s1 INTEGER, s2 INTEGER, s3 INTEGER)")
    con.commit()
    con.close()

# Add Student
def add_student():
    def save_student():
        try:
            con = sqlite3.connect("students.db")
            cursor = con.cursor()
            rno = int(entry_rno.get())
            name = entry_name.get()
            s1 = int(entry_s1.get())
            s2 = int(entry_s2.get())
            s3 = int(entry_s3.get())
            cursor.execute("INSERT INTO student VALUES (?, ?, ?, ?, ?)", (rno, name, s1, s2, s3))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Student Added Successfully!")
            add_win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Could not add student. {e}")

    add_win = Toplevel(root)
    add_win.title("Add Student")
    Label(add_win, text="Enter Roll No:").pack(pady=5)
    entry_rno = Entry(add_win)
    entry_rno.pack(pady=5)
    Label(add_win, text="Enter Name:").pack(pady=5)
    entry_name = Entry(add_win)
    entry_name.pack(pady=5)
    Label(add_win, text="Enter Marks S1:").pack(pady=5)
    entry_s1 = Entry(add_win)
    entry_s1.pack(pady=5)
    Label(add_win, text="Enter Marks S2:").pack(pady=5)
    entry_s2 = Entry(add_win)
    entry_s2.pack(pady=5)
    Label(add_win, text="Enter Marks S3:").pack(pady=5)
    entry_s3 = Entry(add_win)
    entry_s3.pack(pady=5)
    Button(add_win, text="Save", command=save_student).pack(pady=10)
    Button(add_win, text="Back", command=add_win.destroy).pack(pady=5)

# View Students
def view_students():
    view_win = Toplevel(root)
    view_win.title("View Students")
    con = sqlite3.connect("students.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM student")
    records = cursor.fetchall()
    con.close()
    text_area = Text(view_win, width=50, height=20)
    text_area.pack(pady=10)
    for record in records:
        text_area.insert(END, f"Rno: {record[0]}, Name: {record[1]}, S1: {record[2]}, S2: {record[3]}, S3: {record[4]}\n")
    Button(view_win, text="Back", command=view_win.destroy).pack(pady=5)

# Update Student
def update_student():
    def save_update():
        try:
            con = sqlite3.connect("students.db")
            cursor = con.cursor()
            rno = int(entry_rno.get())
            name = entry_name.get()
            s1 = int(entry_s1.get())
            s2 = int(entry_s2.get())
            s3 = int(entry_s3.get())
            cursor.execute("UPDATE student SET name = ?, s1 = ?, s2 = ?, s3 = ? WHERE rno = ?", (name, s1, s2, s3, rno))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Student Updated Successfully!")
            update_win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Could not update student. {e}")

    update_win = Toplevel(root)
    update_win.title("Update Student")
    Label(update_win, text="Enter Roll No:").pack(pady=5)
    entry_rno = Entry(update_win)
    entry_rno.pack(pady=5)
    Label(update_win, text="Enter Name:").pack(pady=5)
    entry_name = Entry(update_win)
    entry_name.pack(pady=5)
    Label(update_win, text="Enter Marks S1:").pack(pady=5)
    entry_s1 = Entry(update_win)
    entry_s1.pack(pady=5)
    Label(update_win, text="Enter Marks S2:").pack(pady=5)
    entry_s2 = Entry(update_win)
    entry_s2.pack(pady=5)
    Label(update_win, text="Enter Marks S3:").pack(pady=5)
    entry_s3 = Entry(update_win)
    entry_s3.pack(pady=5)
    Button(update_win, text="Save", command=save_update).pack(pady=10)
    Button(update_win, text="Back", command=update_win.destroy).pack(pady=5)

# Delete Student
def delete_student():
    def save_delete():
        try:
            con = sqlite3.connect("students.db")
            cursor = con.cursor()
            rno = int(entry_rno.get())
            cursor.execute("DELETE FROM student WHERE rno = ?", (rno,))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Student Deleted Successfully!")
            delete_win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Could not delete student. {e}")

    delete_win = Toplevel(root)
    delete_win.title("Delete Student")
    Label(delete_win, text="Enter Roll No:").pack(pady=5)
    entry_rno = Entry(delete_win)
    entry_rno.pack(pady=5)
    Button(delete_win, text="Delete", command=save_delete).pack(pady=10)
    Button(delete_win, text="Back", command=delete_win.destroy).pack(pady=5)

# Main Menu
def main_menu():
    Button(root, text="Add", command=add_student, width=20).pack(pady=10)
    Button(root, text="View", command=view_students, width=20).pack(pady=10)
    Button(root, text="Update", command=update_student, width=20).pack(pady=10)
    Button(root, text="Delete", command=delete_student, width=20).pack(pady=10)

# Initialize App
init_db()
root = Tk()
root.title("Student Management System")
main_menu()
root.mainloop()



