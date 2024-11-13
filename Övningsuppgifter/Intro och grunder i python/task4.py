#Uppgift 1: Summera siffror med en forloop
sumList = [1, 2, 3, 4, 5]

sum2 = 0
for number in sumList:
    sum2 += number
print(sum2)

#Uppgift 2: Hitta det största talet med en forloop
maxList = [3, 12, 7, 21, 5]

largest_number = maxList[0]
for num in maxList:
    if num > largest_number:
        largest_number = num

print(largest_number)

#Uppgift 3: Räkna upp till 10 med en whileloop
i = 1
while i <= 10:
    print(i)
    i += 1

#Uppgift 4: Summera siffror som är större än 10 med en whileloop
array = [5, 12, 9, 15, 8]

i = 0
sumOver = 0
while i <= 4:
    if array[i] > 10:
        sumOver += array[i]
    i += 1
print(sumOver)

#Uppgift 5: Multiplicera alla siffror i en lista med en forloop
mList = [2, 3, 4]

mSum = 1
for mNumber in mList:
    mSum *= mNumber
print(mSum)
