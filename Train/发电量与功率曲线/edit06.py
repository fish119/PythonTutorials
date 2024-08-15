import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# 设置支持中文的字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def plot_power_curve(excel_file):
    # 读取Excel文件的Sheet3
    df = pd.read_excel(excel_file, sheet_name='Sheet3', header=0)

    # 检查并使用有效的列名
    time_col = None
    power_col = None
    for col in df.columns:
        if '时间' in col or 'time' in col.lower():
            time_col = col
        elif '有功功率' in col or 'power' in col.lower():
            power_col = col

    if time_col and power_col:
        # 将时间列转换为datetime格式
        df[time_col] = pd.to_datetime(df[time_col])
        
        # 绘制每小时有功功率曲线图
        plt.figure(figsize=(16, 3))
        plt.plot(df[time_col], df[power_col])
        plt.title(f"逆变器_{excel_file[:-5]}_有功功率")
        plt.xlabel('时间')
        plt.ylabel('有功功率')
        plt.gcf().set_size_inches(16, 3)
        plt.savefig(f"charts/{excel_file[:-5]}_有功功率.png", dpi=100)
        plt.close()
    else:
        print(f"找不到有效的数据列: {excel_file}")

if __name__ == '__main__':
    # 获取当前文件夹下所有Excel文件
    excel_files = [f for f in os.listdir() if f.endswith('.xlsx') or f.endswith('.xls')]

    for excel_file in excel_files:
        plot_power_curve(excel_file)


    # input_file = "07.xlsx"

    # plot_power_curve(input_file)