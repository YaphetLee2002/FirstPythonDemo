str1 = "我是字符串数据类型"
# 将字符串类型转换成列表类型
list1 = list(str1)

list1[0] = "它"  # 将列表中的第一个数据修改为它
str1 = "".join(list1)   # 将列表转换成字符串类型
print(str1)