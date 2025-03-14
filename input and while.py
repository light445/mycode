#练习7.4
# pizzas='请输入披萨配料并在输入quit时结束'
# while True:
#     topping=input(pizzas)
#     if topping !='quit':
#         print('我将继续添加')
#     else:
#         break


# prompt='请输入年龄'
# while True:
#     a=input(prompt)
#     if int(a)<18:
#         print('可以进入')
#     else:
#         break

# 7.5
# prompt='\n不到3岁免费，3（含）到12收10美元，年满12岁15美元,请输入年龄'
# prompt+='\n输入quit结束：'
# active=True
# while active:
#     age=input(prompt)
#     if age=='quit':
#         break
#     age=int(age)
#     if age<3:
#         print('免费')
#     elif age<12:
#         print('10美元')
#     else:
#         print('15美元')
# 7.7
# a=1
# while a<5 :
#     print(a)
#     a+=1
#7.8
# sandwich_orders=['火腿三明治','鸡肉三明治','蔬菜三明治']
# finished_sandwich=[]
# while sandwich_orders:
#     print('I made your tuna sandwich.')
#     finished_sandwich=sandwich_orders.pop()
# a='所有三明治'
# print(f'{a}','火腿三明治','鸡肉三明治','蔬菜三明治')
sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)


print("\n")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")









