import os, time, random

wordList = {}                   

def wordCount():
    with open("wordsList.txt", "r") as f:
        count = 0
        for words in f.readlines():                                          
            count += 1
        return count

def wordsUpdate():                   #Updates dictionary with words from wordsList.txt
    f = open("wordsList.txt", "r")
    for words in f.readlines():
        keys, meanings = words.rstrip().split(":")
        wordList[keys] = meanings.lstrip()
    f.close()

#adds index and definitions to wordsList.txt
def wordAdd():                      
    with open("wordsList.txt", "a+") as f:
        addWord = input("What word do you want to add? ").capitalize()
        addMeaning = input("What's the definition? ").capitalize()
        
        #double checks user's entry
        print(f"\n{addWord}: {addMeaning}")                             
        dubCheck = input("Are you sure about this entry?\n\ny/n: ")
        if dubCheck[0].lower() == "y":
            count = wordCount() + 1
            f.write(f"\n{count}. {addWord}: {addMeaning}")
            wordCount()

def wordSelectRndm():
    j = random.randint(1, wordCount())
    with open("wordsList.txt", "r") as f:
        for words in f.readlines():
            i, trash = words.split(".")
            if int(i) == j:
                return trash.lstrip()
wordOfDay = wordSelectRndm()

def wordShow():
    with open("wordsList.txt", "r") as f:
        for words in f.readlines():
            print(f"{words}")
    go = input("\nPress Enter to go back to the menu\n")

#Menu
while True:                                                                   
    os.system("cls")
    print("\t\t\tWord of the Day\n")
    print(f"\tToday's word of the day is:\n\n{wordOfDay}")
    
    uChoice = input("Do you want to add a new word or see all the words?  ")

    if uChoice[0].lower() == "a":
        os.system("cls")
        print(wordCount())
        print("\t\tWord of the Day\n")
        wordAdd()

    elif uChoice[0].lower() == "s":
        os.system("cls")
        print("\t\tWord of the Day\n")
        wordShow()
        
    else:
        print("Please enter 'add' or 'show'!!  ")
        time.sleep(3)
        continue