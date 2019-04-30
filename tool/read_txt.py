def read_txt(filename):
    # 打开文件并调用load方法
    with open("../date/" + filename, "r", encoding="utf-8") as f:
        return f.readlines()
if __name__ == '__main__':
    print(read_txt("login.txt"))