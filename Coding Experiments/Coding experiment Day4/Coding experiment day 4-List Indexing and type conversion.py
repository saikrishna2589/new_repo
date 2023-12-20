# Experiment 1- importance of types

a = input('type you value: ')
b = int(a) + 5
c = print(b * 10)
d = print(a + str(5))  # string concate
e = print(a * 5)  # string value repeat 5 times

print(float('10'))
print(int('10'))

# you want to use floats when working with continuous data. say variable such as age ,temperature
# if you are working with number of employees, you work with int.

# Python has implicit declaration of types.
print(type((10.1)))  # type is implicitly assigned to float in this case

print(type(10))

print(type('10.3'))


