s=input("enter a string:\n")
first_char=s[0]
new_string=first_char +s[1:].replace(first_char,"$")
print(new_string)


