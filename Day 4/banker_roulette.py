#import random module
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#variable that hold random int as value  from number 0 - 4
num_for_index = random.randint(0,4)
#PRINT friends list with num_for_index as indice
print(friends[num_for_index])

#Here is a simpler way 

print(random.choice(friends))