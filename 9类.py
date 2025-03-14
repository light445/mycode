#创建动物类
class Animals:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height
        self.shengao=0
    def xixing(self):
        print('eat')
    def name_update(self,aaa):
        #修改属性值
        self.name=aaa
    def dizeng(self,mile):
        #递增属性值
        self.shengao+=mile
    def read_message(self):
        print(f'The car has {self.name}')
cat=Animals('小白','10','160')


#创建一个汽车类
class Car:
    '''一次模拟汽车的简单尝试'''
    def __init__(self,make,model,year):
        '初始化描述汽车属性'
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading =0

    def get_descripyive(self):
        '返回信息'
        long_name=f'{self.make},{self.model},{self.year}'
        return long_name.title()
    def read_odometer(self):
        '打印汽车行驶里程的消息'
        print(f'This car has {self.odometer_reading } miles on it.')
    def update_odometer(self,mileage):
        '''将里程表读数设置为指定值禁止将里程表读数往回调'''
        if mileage >= self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print('You can\'t roll back an odometer_reading')
    def increment_odometer(self,miles):
        '''让里程表读数增加指定的量'''
        self.odometer_reading+=miles
my_new_car =Car('audi','a4',2024)
my_new_car.increment_odometer(100)
my_new_car.read_odometer()

my_new_car.increment_odometer(200)
my_new_car.read_odometer()



