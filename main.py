// this csv will be added to it
l = ["india","china","brazil","kenya","pakistan","bangladesh","hongkong","iran","iraq","isreal"]
import numpy as np
print("----------WELCOME TO THE HANGMAN GAME --------")
print("-----------YOU WILL HVAE TO GUESS THE COUNTRY NAME -----------")
print("-----RULES-----")
print("YOU WILL GET TOTAL OF 5 CHANCES TO GUESS THE LETTER")
print("YOU WILL ")
word = np.random.choice(l,replace = 'True')
word
list1 = []
for i in range(len(word)):
    list1.append('_')
print(list1)
count = 0;
p = len(word)
print("word consist of ",len(word),"letters")
print("GUESS THE LETTER OR GUESS THE WORD")
for i in range(5):
    print("1 for letter \n 2 for word")
    number = int(input("Enter your choice"))
    if number == 1:
        # for i in range(0,5):
            max =5
            l1 = input("Enter the  letter of your guess").lower()
            if l1 in word: 
                count += 1 
                print("You guess the letter right")
                for i in range(len(word)):
                    if word[i] == l1:
                        list1[i] = l1
                # list1[word.index(l1) ] = l1
                print(list1)
            else            : 
                    count = 0
                    print("you guess the worng letter")
            max-=1
            print("You left with chances",max)
    if number == 2:
        l1 = input("Enter the  word of your guess").lower()
        if l1 == word: 
            print("You guess the word right")
            break
        else         : count = 0
    if count == len(word):
        print("You guess the word right")
// this is the hangamn game
