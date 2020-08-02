
newList = []
digitList = []
#Soru: 40
limit = 1000000
for i in range(1,limit+1):
    newList.append(i)
for digits in str(newList):
    if ((digits == ",") or (digits == " ") or (digits == "]") or (digits == "[")):
        continue
    else:
        digitList.append(digits)
product = (int(digitList[1 -1]) * int(digitList[10 -1]) * int(digitList[100 -1]) * int(digitList[1000 -1]) * int(digitList[10000 -1]) * int(digitList[100000 -1]) * int(digitList[1000000 -1]))
print("Product:",product)

    

