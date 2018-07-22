x = int(input("Enter a number: "))

div = []

#create a list of numbers that are less than x
interval = range(1, x+1)

#check if each elemnet in interval divides x
for i in interval:
    if x % i == 0:
        div.append(i)
print(div)
