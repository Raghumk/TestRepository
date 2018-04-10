
#Exception

def KelvinToFahrenheit(Temperature):
	assert (Temperature >= 0),"Colder than absolute zero!"
	return ((Temperature-273)*1.8)+32

### example for Exception clause
#--------------------
#Example 1

try:
	print ( 1/0)
except ZeroDivisionError:
	print ("ZeroDivisionError")
finally: 
	print("Always finally clause is executed")


#--------------------
#Example 2

a = 25
b = 20

try:
	if a > b:
		raise Exception (a)
	else:
		print ("no exception")	

except Exception as e:
	print('Exception', e.args[0])

#--------------------



'''
try:

	print (KelvinToFahrenheit(273))
	print (int(KelvinToFahrenheit(505.78)))
	print (KelvinToFahrenheit(-5))

except IOError:
	print("io error")
else:
		"No error"
finally:
	print("other error")
'''