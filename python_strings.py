
var1 = "Hello World"

print (var1[0])  	# "H"
print (var1[2:3])  	# prints characters from 2nd position to 3rd position. output "l"
print (var1[3:])	# prints all characters from position 3. outpuit "lo World"
print (var1[:4]) 	# prints all characters till the posiotn 4. Output "Hell"

#Escape characters

print ("hello \a")   # \a bell
print ("hello \n world")  # \n new line   \t tab  \r carriage return


## String formating % ##

print ("My name is %s and I am stuydying %d standard"  % ('surabhi', 5))

'''
%c --> character
%s --> string 
%i --> signed decimal integer

'''

a = """  this is a multi line comment
         we can write multple lines using tripple quots
         this is example for the same """

print (a)

a = ''' this is also
          multi linein
          in triple single qotes '''

print (a)



## String functions
str = "This is a text STRing"
print (str.capitalize()) 		# convert first character to upper case and rest to  lower case
print (str.center(50),"a")		# centers to specified number of characters and fills the char
print (str.count("t"))	 		# counts specified pattern. 
print (str.count("t", 11, 15))	 		# counts specified pattern, starting position, end position

print ("position of \"is\" : ", str.find("is"))  	#  finds the string in another string, we can specify position etc.

# isalnum --> check if all  	checks if string has alpha numeric characters
# isalpha ()
# isdigit ()
# islower()
# isnumeric()
# isspace()
# istitle()
# isupper()
# join()
# len()
# ljust() -- left justification, pad with speficie character
# lstrip()

------------------------------ need to continue from page 140

