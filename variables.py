
Name="Raghavendra"

print(Name)
print(Name[0])     # prints  R
print(Name[1:3])    # prints charactrs from 1st to 3rd i.e, "ag"
print(Name[3:])    #prints 3rd position till end.  havendra
print(Name * 2)    # prints Raghavendra two times
print ("Mr."+Name)  # string concat

del Name

#### Python Lists ######

list = ["raghu", 123, 2.3]
list2 = [77, "kiran"]

print(list)
print(list[1])
print (list*2)      # ['raghu', 123, 2.3, 'raghu', 123, 2.3]

print(list + list2)  # concat the list

############# Python  Tuples ############
#tuples uses (), list uses []
#tuples separated by commas, 
#tuples cannot be updated(read only).  Lists can be updated

tuple = (100, "raghu", 34.3)

print ("tuple = ", tuple)

############ Python Dictionary   ####
# key value pair
# enclosed in {}
# values can be assigned and accessed using []

print("---------Dictionary----------------")
dict = {}
dict  ["one"] = 1
dict  [2] = "two"
dict  [3.14] = "pi"

print (dict)         #  output-- {'one': 1, 2: 'two', 3.14: 'pi'}
print(dict.keys())
print(dict.values())

#----------------

if "raghu" in tuple:
	print ("raghu is in tuple")
elif "kiran" not in list:
	print ("kiran not in list")

if 1 < 2 : print ("one is < 2")   # Single line conditional statement

print("================")
for var in tuple:
	print (var)

for i in range(1,10):
	for j in range(1,10):
		print (i * j , end =" ")   # end =" " print the string in same line
	print("")

#++++++++++++++++++++++++
print("#++++++++++++++++++++++++")
for letter in 'Python':
	print (letter)