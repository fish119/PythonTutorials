import tkinter as tk

# window控件是窗口控件，每一个桌面程序都需要至少一个窗口，其他的控件依附于窗口控件
window = tk.Tk()

# 窗口可以通过title方法设置标题
window.title("Hello World")

# 窗口的大小，可以通过geometry方法设置，你可以修改代码里的参数，随意调整窗口的大小
window.geometry("300x200")

# 创建一个标签（Label）控件，用于显示文字
# label控件，是专门用来显示文字的，创建label时，需要指明它的父容器，这里我将label控件的父容器设置为前面创建的window窗口
label = tk.Label(window, text="Hello World!", width=20, height=2, font=("Arial", 16))

# 一定要使用pack方法，这样才能固定到窗口上
label.pack()

# 启动窗口
window.mainloop()
