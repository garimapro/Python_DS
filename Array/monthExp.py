monExp = [2200, 2350, 2600, 2130, 2190]
# 1. In Feb, how many dollars you spent extra compare to January?
extra = monExp[1] - monExp[0]
print(extra)
# 2. Find out your total expense in first quarter (first three months) of the year.
total =0
for i in range(0,3):
    total += monExp[i]
print(total)
# 3. Find out if you spent exactly 2000 dollars in any month
if 2000 in monExp:
    print("yes")
else:
    print("no") 
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
monExp.append(1980)
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
monExp[3] += 200

print(monExp)