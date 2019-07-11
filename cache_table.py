from time import time, sleep

class Cache:
    def __init__(self, a_dict):
        self.a_dict = a_dict

    def cacheit(a_dict, creation_time):
        if time() > creation_time + 5:
            return 'Value has been cached'
        else :
            return value

my_dict = {}
value = input('Enter a value whitch will be cached after 5 sec : ')
creation_time = time()
my_dict[value] = creation_time

foo = Cache(my_dict)
print(foo.cacheit(my_dict[value]))
sleep(6)
print(foo.cacheit(my_dict[value]))
