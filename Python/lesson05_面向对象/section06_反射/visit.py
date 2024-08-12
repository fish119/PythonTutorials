import commons

def run():
    input_str = input("请输入要访问的对象：")
    if hasattr(commons, input_str):
        func = getattr(commons, input_str)
        func()
    else:
        print("404")

if __name__ == '__main__':
    run()