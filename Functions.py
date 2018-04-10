


# Parameter functions is always pass by reference in Python

def fun1( Name ):	
	Name = "Mr." + Name
	return Name

def fun2(Name = "Raghu"):	
	Name = "Mr." + Name
	return Name


print (fun1("Raghu"))
print (fun1(Name="Kiran"))	# Named argument
print (fun2())				#  Default argument

####  Variable length arguments 

def Multiple_Arguments(arg1, *vartuple): 
	"This prints "
	print(arg1)			## First argument

	for x in vartuple:		## Subsequent arguments
		print(x)

	return  x


print ('multiple araguments = ', Multiple_Arguments(10, 20, 30)) 


## Anonymous functions


# not declared using 'def'
# use lamda keyword for anaonymous functions
# can take any number of arguments
# cannot access outside variables. will have local namespace
# syntax:
# lambda [ arg1, [,arg2, arg3..]] : expression

sum = lambda arg1, arg2, arg3 : arg1 + arg2 + arg3		# lambda function with 3 argument
sum2 = lambda : 10					# lambda function without argument

print ("Lambda sum = " , sum(10,20,30))

# Two types of variables.  Global & Local