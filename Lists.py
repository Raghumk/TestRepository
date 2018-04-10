
#Python has 6 types of Lists
'''
	1. Lists
	2. Tuples
	3. 

Operations on Lists:
	1. Indexing
	2. Slicing
	3. Adding
	4. Multiplying
	5. Checking for membership

'''

lst1 = [1,2,3]

print (len(lst1))				# 3			-- length

print ( [1,2,3] + [4,5,6])		# [1,2,3,4,5,6]			-- concatanation

print ( ['Hi'] * 4)				# ['Hi','Hi','Hi','Hi']    --- repeatation

print( 3 in [1,2,3])			# True	-- membership 

for x in [1,2,3]:				# Iteration
	print(x)


lst = ['C++', 'Java', 'Python']

print (lst[-2])		#  Java.   Negative, count backward

# other functions
# len( lst)
# max(lst), min(lst), 
# list(seq)				#convert a tupple to a list
 
lst = ['C++', 'Java', 'Python']

lst.append('C#')
print(lst)
print(lst.count("Java")) 		# 1


# pop, insert(), index(), remove(),reverse(),sort(),

