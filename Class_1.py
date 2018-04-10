# Object & Class

class Employee:
	'Common base class for keeping employee details'
	empCount = 0

	def __init__(self, name, salary):		# constructor __init__
		self.name = name
		self.salary = salary	
		Employee.empCount  += 1				# Class variable
		self.Projectnames =[]

	def __del__(self):						# destructor
		print(self.name, "deleted")

	def displayCount(self):
		print ("Total number of employees : ", Employee.empCount)

	def displayEmployee(self):
		print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print("__doc__    :        ", Employee.__doc__)
		print("__dict__   :        ", Employee.__dict__)
		print("__name__   :        ", Employee.__name__)
		print("__module__ :        ", Employee.__module__)
		print("__bases__  :        ", Employee.__bases__)

		print(self.name, self.salary)
		

	def addProjects(self, pname):
		self.Projectnames.append(pname)

	def printProjects(self):
		print("Projects handled by ",Raghu, " Are: \n----------------------")
		for x in self.Projectnames: print(x)

#lst.append('C#')
Raghu =  Employee("Raghu", 9999999)

Raghu.displayCount()
Raghu.displayEmployee( )
Raghu.addProjects("Carrier Load")
Raghu.addProjects("CCDB")
Raghu.addProjects('TOS')
Raghu.printProjects()
Raghu.newsal = 3838  				# New attributes can be created  on the fly
print (Raghu.newsal)
print ("------------------")
print (getattr(Raghu, 'name'))
print(getattr(Raghu,'salary'))
print(getattr(Raghu,'newsal'))		# new attribute added above
setattr(Raghu, 'salary', 9393939)
Raghu.displayEmployee( )
delattr(Raghu, 'salary')

# Built in class attribute
'''
__dict__	# dictionary containing the class's namespace
__doc__		# class documentation string or none if undefined
__name__	# Class names
__module__	# Module name in whcih the class is defined. This attribute is __main__ in inactive mode
__bases__

'''

## Example for attributes

