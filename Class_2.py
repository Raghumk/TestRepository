
# derived class
# inheritance

#syntax
'''
class subClass (parentClass1, [parentClass2 ]) :
	'Optional class documentation'
	class_suite

'''


class Parent:	
	parentAttr = 100
	
	def __init__(self):
		print("parent constructor")

	def parentMethod(self):
		print("Calling parent method")

	def setAttr(self, attr):
		Parent.parentAttr = attr

	def getAttr(self):
		print("Parent attribute = ", Parent.parentAttr)

class Child(Parent):		## defining child class
	def __init__(self):
		print("calling child constructor")


	def childMethod(self):
		print("calling child method")



##-- Main program 
c = Child()
c.childMethod()
c.parentMethod()

#--------------- example 2 ----------------

class A :
	a = 10

class B :
	b = 10

class  classSum(A, B):
	sum = 0
	def __init__ (): sum = A.a + B.b; print(sum)

#issubclass(sub, sup)
#isinstance(obj, Class)


#Operator overloading

class Vector:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __str__(self):
		return 'Vector (%d, %d) ' % (self.a, self.b)

	def __add__(self, other):
		return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(1, 2)
v2 = Vector(3, 4)

print (v1) ; print (v2)

v3 = v1 + v2
print (v3)


#Data hiding
# object with double underscore (__) will not be directly visible outside the class
# example

class justCounter:
	__secretCounter = 0

	def count(self) : 
		self.__secretCounter += 1
		print(self.__secretCounter)

counter = justCounter()

counter.count()
counter.count()
#print(counter.__secretCounter)		-- this will give error.

