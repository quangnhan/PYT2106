'''
from server import get_server_data #lay data tu server va hien thi tren man hinh
customers = []

def add_customer(data):
    id, name = data.split(',')
    customers.append({
        "id" : id,
        "name" : name,
    })

f = open('Day8/data.txt', 'r')
for line in f.readlines():
    add_customer(line)

data = get_server_data()

for line in data:
    add_customer(line)

print(customers)
'''

#def giai_thua(n): #ham tinh giai thua
#    if n == 0:
#        return 1
#    return n*giai_thua(n-1)

#print(giai_thua(5))

#bai toan fibonacci
'''def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(15))'''


from abc import ABC, abstractmethod
from server import get_server_data

class Employee:
    count = 0
    BASIC_SALARY = 100
    def __init__(self, id, name, rate) -> None:
        Employee.count = Employee.count + 1
        Employee._id = Employee.count
        self._name = name
        self._rate = rate

    @property
    def name(self):
        return(self._name)

    @property
    def rate(self):
        return(self._rate)

    @name.setter
    def name(self, var):
        self._name = var

    @rate.setter
    def rate(self, var):
        if var > 0:
            self._rate = var
        else:
            print("invalid value!")

    @abstractmethod
    def salary(self):
        pass

    def info(self):
        print(f'Name = {self._name}, ID = {self._id}, Rate = {self._rate}')

class FullTime(Employee):
    def __init__(self, name, rate) -> None:
        super(FullTime, self).__init__(name, rate)

    @abstractmethod
    def salary(self):
        return self.rate * Employee.BASIC_SALARY

class PartTime(Employee):
    def __init__(self, name, rate, days) -> None:
        super(FullTime, self).__init__(name, rate)
        self.days = days

    @property
    def days(self):
        return(self.days)

    @days.setter
    def days(self, var):
        pass

    def salary(self):
        return self._rate * Employee.BASIC_SALARY * self.days

class HourlyEmployee(Employee):
    def __init__(self, id, name, rate, hours) -> None:
        super(Employee, self).__init__(id, name, rate)
        self.hours = hours

    def salary(self):
        return self._rate * Employee.BASIC_SALARY * self.hours

