import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Text Example")
window.geometry("300x200")

# 创建Text控件
textInput = tk.Text(window, height=3)
textInput.pack()


# 按钮点击事件
def btnClick():
    """
    按钮点击事件
    :return:
    """
    content = textInput.get("0.0", "end")
    messagebox.showinfo(
        "Text Exampler Message", "输入的内容为：{text}".format(text=content)
    )


button = tk.Button(window, text="Text Submit", width=15, height=2, command=btnClick)
button.pack()

window.mainloop()
