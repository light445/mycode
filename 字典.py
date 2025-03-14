# yigeren={'first_name':'王','last_name':'小明','age':'12','city':'北京'}
# num='hello'
# print(f"{num}"+yigeren['first_name'])
# print(yigeren['first_name'])
# 创建字典
a={'小明':'1358468751',}
print(a['小明'])
#修改字典
a['小明']='123456'
print(a)
# 创建字典b
b={'小王':'123456','小李':'147852963','小吴':'132465798'}
# 打印小王电话
print(b['小王'])
#修改小王电话
b['小王']='112233'
#打印小王新号码
print(b['小王'])
#删除小王电话
del b['小王']
#打印字典b
print(b)