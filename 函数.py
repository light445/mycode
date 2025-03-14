def display_message():
    print('本章学习函数')
display_message()
# def favorite_book(title):
#     print('One of my favorite_books is Alice in wonderland')

# def ssanjiaoxing(di,gao):
#     a=1/2*di*gao
#     return a
# print(ssanjiaoxing(4,5))
#8.6
# def city_country(city,country):
#     a=f'{city} {country}'
#     return a
# city1=city_country('上海','china')
# city2=city_country('北京','china')
# city3=city_country('深圳','china')
# print(city1)
# def make_album(name,zname,name3):
#     a={'name1':'name','zname':'name2',}
#     if name3:
#         a[name3]=name3
#     return a
# b=make_album('zb','zc')
# print(b)
# def make_album(artist, title, num_songs=0):
#     """创建一个包含专辑信息的字典"""
#     album_dict = {
#         'artist': artist.title(),
#         'title': title.title(),
#
#     }
#     if num_songs:
#         album_dict['num_songs'] = num_songs
#     return album_dict
#
#
# album = make_album('metallica', 'ride the lightning')
# print(album)
#
# album = make_album('beethoven', 'ninth symphony')
# print(album)
#
# album = make_album('willie nelson', 'red-headed stranger')
# print(album)
#
# album = make_album('iron maiden', 'piece of mind', num_songs=8)
# print(album)

# def make_ablum(artist, title, age=None):
#     ablum_dict={'artist':'artist','title':'title'}
#     if age:
#         ablum_dict['age']=age
#     return ablum_dict
# ablum = make_album('willie nelson', 'red-headed stranger')
# a = make_ablum('iron maiden','red-headed stranger')
# print(ablum)
# def build_person(first_name,last_name,age=None):
#     person={'first':first_name,'last':last_name}
#     if age:
#         person['age']=age
#     return person
# while True:
#     print('\nplese tell you name：')
#     print("entre'q'")
#     f_name=input('first name')
#     if f_name=='q':
#         break
#     l_name=input('last name')
#     if l_name=='q':
#         break
# zxc=build_person(f_name,l_name)
# print(f'{zxc}')
# def great_users(names):
#     for name in names:
#         msg = f'{name}'
#         print(msg)
# 8.9
# message=['hi','hello','niaohao']
# def messages(list):
#     for mes in message:
#         a=mes
#         print(a)
# messages(message)
# #8.10
# send=['hi','ok''yes']
# send_messages=[]
# def send_messages(message,send_message):
#     b=send
#     print(b)
#     while send:
#         send_messages=b.append()
# send_messages(message,send_messages)


#创建动物类
# class dongwu:
#     def __init__(self,name,age,height):
#         self.name=name
#         self.age=age
#         self.height=height
# class ren(dongwu):
#     def __init__(self,zhonglei):
#         super().__init__(zhonglei)
#         self.zhonglei=zhonglei
# ren1=ren('bairen')
# print(ren1.zhonglei)






zxcs=['hi','hello','good']
#给hello模块取名字
import hello as h
#导入特定的函数
from hello import jisuan
#给模块中的函数取名
from hello import jisuan as js
jisuan(1,1)
from hello import shou_messages as sm

# def build_profile(first,last,**user_info):
#     '''创建一个字典，其中包含我们知道的有关用户的一切'''
#     user_info['first_name']=first
#     user_info['last_name']=last
#     return user_info
# user_profile = build_profile('li','bai',car='baoma',房子='别墅',职业='doctor')
# print(user_profile)
















