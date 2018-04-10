'''
print, functions, while, for, if, type, comments, bitwise operation

'''

print ("Hello Friends")

string="string"
int=833
longint=83939393933
float=93.34

print("-----------")
print(string, int, longint)
print("-----------")

print(type("string"))
print(type(int))
print(type(float))
print(type(38/23.2))     #  Single # is used for commenting
print("Multiply : " , 2*2, "  Power :",  2**2,  "    division:", 4/2)

print ("one") ; print ("two") ; print ("three")  # multiple statements in single line

# function with arguments
def fun_sqr(a):    # Function returning 1 value
	return a*a

def multival(a, b):    #function returning more than 1 value
	return a+b, a-b

a = fun_sqr(3)


print ("function with multiple return values: " , multival(5, 2))

if a == 3:
	print ("a is equal to 3")
else:
	print ("a is not equal to 3")


#bitwise operation
a= 4  # 4=100
print ("4 << 1 = " , a << 1 )  #  prints 8 
print ("4 >> 1 = ",  a >> 1 )  # prints 2


#while loop

i=0
while True:   #  'T'  should be capital letter 
	i = i+1
	print (i)
	if i == 10:
		break

print("outside loop")

for i in range(1,10):
	if i == 5:
		continue
	print (i)

