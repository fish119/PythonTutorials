import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Entry Example")
window.geometry("300x200")

# 创建输入框并pack
nameEntry = tk.Entry(window)  # 创建用户名输入框
nameEntry.pack()

pwdEntry = tk.Entry(window, show="*")  # 创建密码输入框
pwdEntry.pack()


def clickButton():
    """
    当按钮被点击时执行该函数
    :return:
    """
    name = nameEntry.get()
    pwd = pwdEntry.get()
    msg = "用户名：{name}，密码：{pwd}".format(name=name, pwd=pwd)
    messagebox.showinfo(title="Entry Example Message", message=msg)


button = tk.Button(window, text="Login", width=15, height=2, command=clickButton)
button.pack()

window.mainloop()
