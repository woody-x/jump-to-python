from ErrorException import *

class Bird:
    def fly(self):
        raise NotImplementedError


class Eagle(Bird):
    def fly(self):
        print("very fast")

    def say_name(self, name):
        if name != '독수리':
            raise ErrorException()
        print(name)