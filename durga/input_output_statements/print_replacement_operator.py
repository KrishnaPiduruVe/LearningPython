'''
print(object)

print can take any object 

lets say 

l=[10,20,30]

print(l) # [10,20,30]


print with replacement operator :

    {} ===> this is called as replacement operator

    name = 'durga'
    salary = 10000
    gf = 'sunny'

Hello durga, your salary is 10000 and friend sunny is waiting


'''

l = [10, 20, 30]
print(l)

print("#"*30)

name = 'durga'
salary = 10000
gf = 'sunny'

print("Hello {}, your salary is {} and friend {} is waiting".format(name, salary, gf))
print("Hello {0}, your salary is {1} and friend {2} is waiting".format(
    name, salary, gf))
print("Hello {x}, your salary is {y} and friend {z} is waiting".format(
    x=name, y=salary, z=gf))
