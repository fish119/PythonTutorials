# Tkinter是图形用户界面工具包标准的Python接口，不需要额外安装，是python标准库的一部分
# 它可以运行在大多数unix平台，windows，mac，适合新手入门学习。

# 每一个tkinter程序，至少包含以下两个部分

import tkinter as tk

window = tk.Tk()
window.title("主窗口")
##窗口尺寸
window.geometry("200x200")
##显示出来
window.mainloop()
