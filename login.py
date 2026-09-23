from tkinter import *
login_page = Tk()
def test():
    print("Hello World!")

login_page.geometry("400x400")
login_page.title("Login Form")

name_lbl = Label(login_page,text="Username",font=("arial",15))
name_lbl.pack(pady=10)

name_ent = Entry(login_page,font=("arial",15))
name_ent.pack(pady=10)

password_lbl = Label(login_page,text="Password",font=("arial",15))
password_lbl.pack(pady=10)

password_ent = Entry(login_page,font=("arial",15))
password_ent.pack(pady=10)

submit_btn = Button(login_page,text="Submit",font=("arial",15),bg="green",fg="white",command=test)
submit_btn.pack(pady=10)

login_page.mainloop()

