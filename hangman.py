import random

random.seed(30)

marvel = ['iron man','thor','spiderman','hulk']
index = random.randint(0,len(marvel)-1)

print(index)

def split(word):
    return [char for char in word]

word = split(marvel[0])




