# class Car():
#     name= "gfh"
#     engine= 'b4'
#     wheels= 4
#     fdfgfh= '343fg'
#     fdgfd= '446546$'

#     def drive(self):
#         print (f'{self.name} elfd')
# matiz=Car()
# tesla= Car()
# m2= Car()
# tesla.name='Tedfgfdgdfgfd,glkf'        
# tesla.drive()




# class Car():
#     def __init__(self,name,engine,wheels,weight,price):
#         self.name =  name
#         self.engine =  engine 
#         self.wheels =  wheels
#         self.weight =  weight
#         self.price =  price

# tesla= Car('Tesla','electro','7','3434fdg','2000$')
# matiz= Car('Matiz','electro','7','3434fdg','2000$')
# matiz2= Car('Matiz','electro','7','3434fdg','2000$')

# print(tesla.price)
# print(matiz.name)
# print(matiz2.weight)


# class Cars():
#     def __init__(self,brand,modedl,year,type_of,volume,):
#         self.brand=brand
#         self.model =modedl
#         self.year = year
#         self.odometr = 0
#         self.type_of = type_of  
#         self.volume =  volume  
#         self.is_going  =  False

#     def info_about_car(self):
#             print(self.brand , self.model, self.year)
        
#     def car_is_going(self,km):
#             self.odometr += km 
#             self.is_going = True 
#             return self.odometr, self.is_going 
            
#     def car_not_going(self):
#         self.is_going=False
#         return self.is_going

# mercedec= Cars(brand='Mercedec'  modedl='SSS' year=  '4')
# print(mercedec)





# class Student():
#         def __init__(self,name,age,gpa):
#                 self.__name=name
#                 self.age =age
#                 self.gpa = gpa
#         def name(self): 
#                 print (f'{self.__name,self.age,self.gpa}')

#         def changename(self):
#                 name2 = input()
#                 age2=input()
#                 gpa2=input()
#                 self.age=age2
#                 self.gpa= gpa2
#                 self.__name = name2
                
                

# student1 = Student('Adilet',2007,'100%')
        
# student1.name()
# student1.changename()
# student1.name()


# class Circle():
#         def __init__(self,radius,color):
#                 self.radius=radius
#                 self.color=color


# class Book():
#         def __init__(self, name,pages,author,price):
#                 self.name = name 
#                 self.__pages = pages
#                 self.__author= author
#                 self.__price = price

#         def ring (self):
#                 print(self.__author)
                
#         def info(self):
#                 self.__author="Pushdhsfjdh"
#                 print(self.name, self.__author, self.__pages, self.__price)
# clsa=Book('jjfh' ,'f;lkgfd;lkg','fdkmglkfd','78347398')
# clsa.__author='343'
# clsa.ring()
# clsa.info()

      
               
# class Car():
#         def __init__(self,make,model,year):
#                 self.make=make
#                 self.model= model
#                 self.year=year
#                 self.odometer=0
#                 self.__fuel=70
                
#         def drive (self,km):
#             if self.__fuel>=km/10:
#                self.add_distance(km)
#                self.subtract_fuel(km/10)
#                return  "Let's drive!"
#             else:
#                return 'Need more fuel, please, fill more!'

#         def add_distance(self,fuel):
#                 self.__fuel-= fuel

#         def __str__(self):
#                 return f'{self.year},{self.model},{self.make},{self.__fuel}'
#         def __call__(self, model):
#                 self.model=model

# matiz = Car("gkjfh",'jfd','jhfd')
# matiz('jhgvfdkjghkjfdhkhkdfjkjhfdkgh;kjf')
# print(matiz)

#!dsgfd




# class Changeable:
#      def __init__(self, color):
#           self.color = color
#      def __call__(self, newcolor):
#           self.color = newcolor
#      def __str__(self):
#           return "%s" % self.color
 
# canvas = Changeable("green")
# frame = Changeable("blue")
 
# canvas("red")
# frame("yellow")
 
# print(canvas, frame)






# class A():
#     def __repr__(self):
#         return "you botan"
# a = A()
# print(a)


# class adi:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f'мс {self.name} апра {self.age}'

   

# c = adi('Jellyfish', 5)
# print(str(c))



class Adilet:
        def __init__(self, x, y):
                self.x = x
                self.y = y


def __add__(self, other):
        return Adilet(self.x + other.x, self.y + other.y)