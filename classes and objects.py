# class Employee:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def description(self):
#         return f"{self.name} is {self.age} old"
    
#     def speak(self,sound):
#         return f"{self.name} makes{sound} sound"
# try:
#     object = Employee('bhargav',23)

#     print(object.name)

#     dog_description = object.description()
#     dog_sound = object.speak('woof')

#     print(dog_description)
#     print(dog_sound)

# except Exception as e:
#     print('error message',e)


# class parent:
#     # hair_colour = 'brown'
#     speaks = ['english']

# class child(parent):
#     #pass
#     def __init__(self):
#         super().__init__()
#         self.speaks.append('telugu')

# childclass = child()
# print(childclass.speaks) 

class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def description(self):
        return f"{self.name} is {self.age} old"
    
class dog(Employee):
    def speak(self,sound='woof'):
        return f"{self.description()} makes sound {sound}"
    
obj = dog('golden retreiver',23)
print(obj.speak())
    
