def run():
    input_str = input("请输入您想访问页面的url：  ").strip()
    package, modules, func = input_str.split("/")
    obj = __import__(package + "." + modules, fromlist=True)  # 注意fromlist参数
    if hasattr(obj, func):
        func = getattr(obj, func)
        func()
    else:
        print("404")


if __name__ == "__main__":
    run()
