import tkinter as tk

from tkinter import messagebox

window = tk.Tk()
window.title("Button Example")
window.geometry("300x200")


def btn_clicked():
    """
    当按钮被点击时执行该函数
    :return:
    """
    messagebox.showinfo(
        "这里是messagebox的title", "这里是messagebox的内容: 按钮被点击了！"
    )


# 创建一个按钮
btn = tk.Button(window, text="点击我", command=btn_clicked)
btn.pack()  # 将按钮锁定在窗口

window.mainloop() # 启动窗口
