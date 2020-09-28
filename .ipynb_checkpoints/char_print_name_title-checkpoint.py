name = input("Please enter you name here: ")
title = input("Please enter your job title: ")

fullTitle = ""

for char in title:
    fullTitle += char
    print(fullTitle)

fullTitle += " "

for char in name:
    fullTitle += char
    print(fullTitle)
