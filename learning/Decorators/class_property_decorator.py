
class Employee0:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last +'@email.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_0 = Employee0('John', 'Smith')
print(emp_0.first)
print(emp_0.email)
print(emp_0.fullname())
print('rename first')
emp_0.first = 'Jim'
print(emp_0.first)
print(emp_0.email)
print(emp_0.fullname())

print('##################<Soln: property decorator>################################')
# so that user of class wont have to change code

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')
emp_1.fullname = "Corey Schafer"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
