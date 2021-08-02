#empty list
empty=[]
print("This is an empty list: "+ str(empty))

#list of strings
acronyms = ["LOL","IDK","TBH"]
word="tada"
print("This is a list of acronyms: "+ str(acronyms))
print("This is the last item in list: "+acronyms[len(acronyms)-1])

## adding to list
print("\n\n")
acronyms.append("TGIF")
acronyms.append("BFN")
print("After adding to list: "+str(acronyms))

## removing from list
print("\n\n")
acronyms.remove("BFN")
print(acronyms)
print("Now removing the from list: "+acronyms[2])
del acronyms[2]
print("After removing from list: "+str(acronyms))

##if statement
print("\n\n")
if word in acronyms:
    print(word + " is in list\n")
##elif word not in acronyms:
else:
    print(word + " is not in list\n")

#for loopys
for acronym_in_acronyms in acronyms:
    print(acronym_in_acronyms)

#list of numbers
print("\n\n")
numbers=[5,10,15,20]
print("This is a list of numbers: "+ str(numbers)+"\n")