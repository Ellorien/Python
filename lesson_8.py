class Student:
    def __init__(self, object):
        self.student = object

    def __getattr__(self, item):
        print('trace:', item)
        return getattr(self.student, item)


class Appreciation:
    def __init__(self):
        self.thanks = 'Спасибо большое! :)'

student = Student(Appreciation())
print(student.thanks)
