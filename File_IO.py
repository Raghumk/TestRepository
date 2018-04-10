
#Reading keyboard input

# Input & Output works in command line

'''
Name = input("Enter Name: ")\
print (Name)

'''

file   = open('File_IO.py')

print ("Name of file : ", file.name)
print("Open/Closed : ", file.closed)
print("Opening mode: ", file.mode)
print ("File contents\n------")

print(file.read())

file.close()


#file functions
#write
#tell() -- tells you current position wihtin file
#rename()
#remove()
#mkdir()
#chdir()
#getcwd()
#rmdir()
#flush() -- flush internal buffer
#fileno()
#isatty() -- returns true if connected to any devices
#next(file) --> returns next line
#read([size[])  -->reads the byts specified in size till EOD
#readline([size]) 
#readlines([sizehint])
#seek()
#truncate([size])
#writelines(sequence)