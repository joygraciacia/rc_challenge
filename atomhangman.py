import random

marvel = ['iron man','thor','spiderman','hulk']

print(marvel[0])

def split(word):
	return [char for char in word]

char_split = split(marvel[0])

print(char_split)

output = "_"*len(char_split)

output = split(output)

print(output)


print(len(output))

user = input("Your guess? ")

print(user)

user_timer = 1

#def check(user):
#	for j in range(0,len(output)):
#		if(char_split[j] == user):
#			output[j] = user 


#check(user)


#print(output)


#print(len(char_split))