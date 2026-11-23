#import random module 
#list 1 of random words
#list 2 of random words
#your new password is f-string 


import random 
#added more words to both lists to decrease the chance of brute force
phraselist_1 = ["Boogie", "Ooogie", "maJor", "paYne", "Tryhard", "Eeny", "Snow", "Tasmanian", "martha"]
phraselist_2 = ["gonna", "gEt", "you", "heres", "Johnny", "weeny","white", "Devil","companion"]
#created variables with the random choice and randint function for each phrase for readability purposes
phrase_1 = random.choice(phraselist_1)
phrase_2 = random.choice(phraselist_2)
double_digit = random.randint(10,99)
#passphrase is created with a randomly picked string from both lists, and a random integer with a hyphen in between each choice
print(f"Your new password is: {phrase_1}-{phrase_2}-{double_digit}")