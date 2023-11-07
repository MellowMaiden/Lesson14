#Lesson 14 void function

#Example 1
def myfunction():
    print("hello")#there is no return

myfunction()
myfunction()
myfunction()

#example 2
def f():
    print("hello")

def g():
    return("hello")

f()#give hello
g()##nothing
print(f())#give hello and none
print(g())#give hello

#example 3
def message(name,age):
    print("hello",name,"you are",age,"years old")

message("srephen",38)
message("bob",19)
message("James",21)

#Example 4
def funny(name):
    name=name.replace("a","4")
    name = name.replace("e", "3")
    name = name.replace("i", "1")
    name = name.replace("o", "0")
    name = name.replace("u", "-")
    print(name)

funny("stephen")

#Example 5
def expand(a,b):
    middle=str(a+b)
    end=str(a*b)
    answer="x**2+"+middle+"x+"+end
    answer=answer.replace("+-","-")
    answer=answer.replace("+1x","+x")
    answer = answer.replace("-1x","-x")
    answer = answer.replace("+0","")
    answer = answer.replace("-0","")
    answer = answer.replace("x**2x","x**2")
    print(answer)

#TESTING
expand(-2,-3)

print("expand(x+a)(x+b)")
a=int(input("a:"))
b=int(input("b:"))
print("answer:")
expand(a,b)