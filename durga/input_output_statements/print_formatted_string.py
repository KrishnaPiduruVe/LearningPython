'''
    print with formatted string :
    =============================

    %i ==> Signed decimal value 
    %d ==> Signed decinal value

    %f ==> float value

    %s ==> string
            any other objects list,set,tuple

    a =10
    print('a value : %i'  %a)

    print("formatted string" %(varialbelist))

'''

a = 10
print('a value : %i' % a)

a = 10
b = 20
c = 30
print('a = %d , b = %d , c =%d' % (a, b, c))

name = 'durga'
marks = [10, 20, 30, 40]

print("Hello %s your's marks list is %s" % (name, marks))

price = 7089.56789
print("price value is {}".format(price))
print("price value is %f" % price)

print("price value is {:.2f}".format(price))
print("price value is %.2f" % price)

print("price value is {:.2f}".format(price))
print("price value is %.2f" % price)
