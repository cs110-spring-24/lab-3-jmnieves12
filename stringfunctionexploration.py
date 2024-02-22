# String function exploration:
# class string.Template(template)
# substitute function!
#string = input("Enter any word: ")
#substitute(mapping={string}, /, **kwds)


#In class stuff:

string = "It is a SuNnY DaY. it rained yesterday"

print(string.lower()) #becomes all lowercase
print(string.upper()) #becomes all uppercase
print(string.capitalize()) #only the first word is capitalized
print(string.swapcase()) #all upper case becomes lowercase and vice versa
print(string.title()) # every first letter of each word is capitalized
print(string.partition(" "))
print(string.split(" "))
print(string.strip()) #gets rid of all the whitespace before or after
print("hello".strip())