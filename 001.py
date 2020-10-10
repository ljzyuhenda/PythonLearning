# 打印换行
print("hello world")
print('''hello \n
world''')
print(r'''hello \n
world''')

# 字符串
print(ord('A'))
print(chr(65))
print("中文".encode("utf-8"))
print("AB".encode("utf-8"))
# 格式化
print("Hello %s world %.2f" % ("我的", 100.121))

# 集合 list可变，tuple不可变
names = ['中华', '时间', '世界'] 
print(names)
names.append("估计")

ages = (1, 2, 3)



