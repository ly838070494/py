class Student(object):
    def __init__(self, name):
        self.name = name
    def set_gender(self, gender):
        if gender in ('male', 'female'):
            self.__gender = gender
        else:
            raise ValueError('bad gender')
    def get_gender(self):
        return self.__gender

s = Student('Lisa')
s.set_gender('nv')
print(s.name, s.get_gender())
