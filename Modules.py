

# Modules
# ex: importing
# import module1; module2; ...
# from modulename import name1, name2 ...



Global_V = 1000

#a = dir(math )
#for i in a: 	print(i)

def add_nums(): 
	global Global_V
	Global_v = Global_V + 1
	print (Global_V)


add_nums()
add_nums()


print (Global_V)