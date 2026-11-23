#import random module 
#list 1 of random words
#list 2 of random words
#your new password is f-string 


import random 

phraselist_1= ["Boogie", "Ooogie", "maJor", "paYne"]
phraselist_2 = ["gonna", "gEt", "you", "heres", "Johnny"]
#passphrase is created with a randomly picked string from both lists, and a random integer with a hyphen in between each choice
print(f"Your new password is : {random.choice(phraselist_1)}-{random.choice(phraselist_2)}-{random.randint(0,9)}")