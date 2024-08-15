import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# 设置支持中文的字体
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False


def plot_excel_files():
    # 获取当前文件夹下所有Excel文件
    excel_files = [f for f in os.listdir() if f.endswith(".xlsx") or f.endswith(".xls")]

    for excel_file in excel_files:
        # 读取Excel文件的Sheet1和Sheet2
        df1 = pd.read_excel(excel_file, sheet_name="Sheet1", header=0)

        # 打印df1的列名
        print(df1.columns)

        # 绘制每日发电量折线图
        plt.figure(figsize=(12, 6))

        # 将日期列转换为 datetime 格式
        df1["日期"] = pd.to_datetime(df1["日期"])

        # 绘制折线图,使用日期列作为 x 轴
        df1["发电量"] = df1["发电量"].replace(",", ".", regex=True)
        plt.plot(df1["日期"], df1["发电量"])
        plt.title(f"逆变器_{excel_file[:-5]}_发电量")
        plt.xlabel("日期")
        plt.ylabel("发电量")

        # 设置 x 轴刻度标签为每个日期
        plt.xticks(df1["日期"], rotation=45)

        plt.gcf().set_size_inches(16, 3)  # 设置图片大小为 1600 x 300 像素
        plt.savefig(
            f"charts/{excel_file[:-5]}_发电量.png", dpi=100
        )  # 设置保存图片的分辨率
        plt.close()


if __name__ == "__main__":
    plot_excel_files()
