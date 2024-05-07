letters = {
    "a" : "f",
    "b" : "g",
    "c" : "h",
    "d" : "i",
    "e" : "j",
    "f" : "k",
    "g" : "l",
    "h" : "m",
    "i" : "n",
    "j" : "o",
    "k" : "p",
    "l" : "q",
    "m" : "r",
    "n" : "s",
    "o" : "t",
    "p" : "u",
    "q" : "v",
    "r" : "w",
    "s" : "x",
    "t" : "y",
    "u" : "z",
    "v" : "a",
    "w" : "b",
    "x" : "c",
    "y" : "d",
    "z" : "e",
}

#input sentence
plain_txt = str(input("Please enter a sentence: "))

#print out sentence to be encrypted
print("The plain sentence is:", plain_txt)

#transform sentence into lowercase
plain_txt = plain_txt.lower() 

#initialize encryp
encryp = " " 

#change input to list & split letters for comparison to dict(letters)
list_letter = list(plain_txt)

#encodes text & charx3=replaces only letters and keeps special characters 
#need for loop thr user input to prevent error
for char in plain_txt:  
    encryp = "".join(letters.get(char, char) for char in list_letter)
#print result     
    print("The encrypted sentence is:", encryp)
    break #stops loop