formatter = "{} {} {} {}" # this variable takes four brackets to make some
# actions with this variable

print(formatter.format(1, 2, 3, 4)) # print one number in their own bracket
print(formatter.format("one", "two", "three", "four")) # print string in bracket
print(formatter.format(True, False, False, True)) # print Boolean in bracket
# takes the first formatter as variable and fill in brackets
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format( #print all this strings in one line
    "Somebody like",
    "To make mistakes",
    "Somebody don't like it",
    "Can you don't take mistakes"
))
