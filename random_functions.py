
import random
########### Random funcctions

list = [1, 2, 3, 4]

print(random.choice(list ))
print(random.choice(range(100)))
print(random.choice("hello world"))   # prints any one char
print(random.choice([100,200,300]))


#randrange returns randomly selected element randrange(start, stop, step)

print( random.randrange(100, 1000, 100))  #

print(random.random())  # returns number between 0.0 to 0.99999

random.seed() ; random.seed(10)     ## random seed

print("before shuffle" , list)
random.shuffle(list)     # randomly rearranges the list
print ("after shuffle", list)

print("random.uniform(5, 10) :" , random.uniform(5,10))    #always returns same random number

print (math.pi)