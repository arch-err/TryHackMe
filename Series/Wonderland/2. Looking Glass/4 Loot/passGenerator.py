import random
wordlist = open("/root/passwords/wordlist.txt","r")
words = wordlist.read().splitlines()
wordlist.close()

def genPass(wordCount: int):
    password = ""
    for i in range(wordCount):
        password += random.choice(words)
    return password

print(genPass(4))
