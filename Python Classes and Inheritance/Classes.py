# Scopes and Namespaces ExampleS
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
#    do_local()
#    print("After local assignment:", spam)
#    do_nonlocal()
#    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

#Class Objects
print("............................")
print("CLASS OBJECTS")
print("============================")
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
      print("Hello my name is {} and I am {} years old".format(abc.name, abc.age) )
   

p1 = Person("John", 36)
p1.age = 40
p2 = Person("Zeki", 50)
p1.myfunc()
p2.myfunc()




