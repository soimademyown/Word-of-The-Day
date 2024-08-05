import os, time, random

wordList = {}

def wordAdd():
    f = open("wordsList.txt", "+a")
    addWord = input("What word do you want to add? ").capitalize()
    addMeaning = input("What's the definition? ").capitalize()
    f.write(f"\n{addWord}: {addMeaning}\n")
    f.close()

def wordCount():
    f = open("wordsList.txt", "r")
    count = 0
    for words in f.readline():                                          #counts number of words
        count += 1
    return count

def wordSelectRndm():
    j = random.randomint(1, 100)
    while i != j:
        for 
        f = open("wordsList.txt", "r")
        
    return selectedWord

def wordShow():
    f = open("wordsList.txt", "r")
    for words in f.readline():
        print(f"{words}\n")
    f.close()

while True:                                                                         #Menu
    print("\t\tWord of the Day\n\n")
    uChoice = input("Do you want to add a new word or see all the words?")

    if uChoice[0].lower() == "a":
        wordAdd()

    elif uChoice[0].lower() == "s":
        wordShow()

    else:
        print("Please enter 'add' or 'show'!")
        continue