
#objects stored in variables
name="john"
members=5

#objects can also be produced by functions
name=input("what is your name?")
#o/p for print(name)-->Sai.'Sai' string will be stored in the name varaible


#converting to another data type
name=float(input("whats your height?"))
#or int(input(x))

#Functions
#Not all functions return a value
x=print("Hello")
#Hello.print function does not return a value to be stored in x variable here.
#unlike the 'input' function


#Custom functions can also return or not return a value
def foo():
    value=10
    return value
x=foo()
x
#o/p=10
#however case 2 doesnt return a value
def foo():
    value=10

x=foo()
x
#here there is no return value specified in the function def. so no o/p is assosiated
#you may get none value


#Return vs Print
def foo1():
    value=10
    return value

def foo2():
    value=10
    print value


x1=foo1()
x1
#o/p=10


x2=foo2()
#o/p=10.
# here x1 will have value 10 assosiated with it but x2 will be nothing
#foo2() will be exeuted and value printed but it wont be assigned to varibale x2


#FUnctions with paremeters/arguments

def foo(number):
    result=number*number
    return result

#with argument name
x=def foo(number=10):
#print(x)-->o/p=10

#Function with multiple parameters/arguments
def foo(number1,number2):
    result=number1*number2
    return result

x=foo(10,20)
x
#o/p=200

#Functions with default parameters/arguments
def foo(number1,number2=2):
    result=number1*number2
    return result
#the default argument can be ommitted
x=foo(10)
#or
x=foo(10,3)
x=30