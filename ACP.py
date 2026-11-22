doc1 = {'Codingal' : 3, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
sum3 = 0
sum2 = 0
sum1 = 0
for i in doc1:
    if doc1[i] == 3:
        sum3 = sum3+1
    elif doc1[i] == 2:
        sum2 = sum2+1
    elif doc1[i] == 1:
        sum1 = sum1+1

print(doc1)
x = int(input("Enter a number between 1 and 3 to check how many occurances there are: "))
if x == 3:
    print(f"{x} occurs {sum3} amount of times.")
elif x == 2:
    print(f"{x} occurs {sum2} amount of times.")
else:
    print(f"{x} occurs {sum1} amount of times.")