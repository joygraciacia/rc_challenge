#import random package
import random

#some marvel characters
marvel = ['ironman','thor','spiderman','hulk','groot','antman']

#randomly generate character
tag = random.randint(0,len(marvel)-1)

print(marvel[tag])

#initialization
def split(word):
	return [char for char in word]

char_split = split(marvel[tag])

word_length = len(marvel[tag])+4

#start game
message = "Welcome to Avengers hang man. You have "+ str(word_length) +" guesses"

print(message)

output = "_"*len(char_split)

output = split(output)

print(output)

#check if user input is correct
def check(user):
	for j in range(0,len(output)):
		if(char_split[j] == user):
			output[j] = user 
		
	return(output)

#check if user wins
def score():
	hit = 0
	for j in range(0,len(output)):
		if(char_split[j] == output[j]):
			hit = hit + 1
	return(hit)

#play game
for k in range(0,word_length):	
	user = input("Your guess? ")
	print(check(user))
	#if user wins
	if(score()==len(marvel[tag])):
		print("You win!")
		break

#if user loses
if(score()<len(marvel[tag])):
	final_message = "Game Over! The word is "+marvel[tag]
	print(final_message)


