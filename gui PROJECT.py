import tkinter as tk
from tkinter import messagebox

students = {}

def add_student():
    roll = roll_entry.get()
    name = name_entry.get()

    if roll == "" or name == "":
        messagebox.showwarning("Input Error", "Please fill all fields")
        return

    students[roll] = {"name": name, "marks": [], "grade": ""}
    messagebox.showinfo("Success", "Student added successfully!")
    roll_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)

def add_marks():
    roll = marks_roll_entry.get()
    if roll not in students:
        messagebox.showerror("Not Found", "Student not found!")
        return

    try:
        m1 = int(sub1_entry.get())
        m2 = int(sub2_entry.get())
        m3 = int(sub3_entry.get())
    except:
        messagebox.showwarning("Input Error", "Please enter valid marks!")
        return

    marks = [m1, m2, m3]
    students[roll]["marks"] = marks
    students[roll]["grade"] = calculate_grade(marks)

    messagebox.showinfo("Success", "Marks added successfully!")

def calculate_grade(marks):
    avg = sum(marks) / 3
    if avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "Fail"

def display_student():
    roll = display_roll_entry.get()
    if roll not in students:
        messagebox.showerror("Not Found", "Student not found!")
        return

    s = students[roll]
    result = f"""
    Name: {s['name']}
    Marks: {s['marks']}
    Grade: {s['grade']}
    """

    messagebox.showinfo("Student Record", result)

root = tk.Tk()
root.title("Student Grade Management System")
root.geometry("400x500")

# ================= Add Student =================
tk.Label(root, text="Add Student", font=("Arial", 14, "bold")).pack()

tk.Label(root, text="Roll No:").pack()
roll_entry = tk.Entry(root)
roll_entry.pack()

tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Button(root, text="Add Student", command=add_student).pack(pady=5)

# ================= Add Marks =================
tk.Label(root, text="\nAdd Marks", font=("Arial", 14, "bold")).pack()

tk.Label(root, text="Roll No:").pack()
marks_roll_entry = tk.Entry(root)
marks_roll_entry.pack()

tk.Label(root, text="Subject 1:").pack()
sub1_entry = tk.Entry(root)
sub1_entry.pack()

tk.Label(root, text="Subject 2:").pack()
sub2_entry = tk.Entry(root)
sub2_entry.pack()

tk.Label(root, text="Subject 3:").pack()
sub3_entry = tk.Entry(root)
sub3_entry.pack()

tk.Button(root, text="Add Marks", command=add_marks).pack(pady=5)

# ================= Display Student =================
tk.Label(root, text="\nDisplay Student", font=("Arial", 14, "bold")).pack()

tk.Label(root, text="Roll No:").pack()
display_roll_entry = tk.Entry(root)
display_roll_entry.pack()

tk.Button(root, text="Show Details", command=display_student).pack(pady=10)

root.mainloop()
