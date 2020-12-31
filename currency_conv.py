currencyDict = dict()
with open("currencyData.txt") as fhand:
   # make a currency, value dictionary
    for line in fhand:
        words = line.split('\t')
        currencyDict[words[0]] = words[1]

amount = input("Enter the amount(in INR) you want to convert: ")
print("The available currency convertion options: ")
[print(item) for item in currencyDict.keys()]
currency = input("Enter the currency you want to convert into: ").title()
print(
    f"{amount} INR is equal to {float(amount)*float(currencyDict[currency])}")
