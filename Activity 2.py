dict1 = {"Codingal":2, "is":2, "best": 2, "for":2, "Coding":1}

sum = 0
for i in dict1:
    if dict1[i] == 2:
        sum = sum+1
    
print("The number '2' comes up", sum, " amount of times")

    