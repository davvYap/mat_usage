import matplotlib
import matplotlib.pyplot as plt

date = []
concrete = []
sand = []
stone = []


# to calculate the start date & number of days for the report:
year=2022
month = int(input("Input report month:"))
date_start = int(input("Input the start date for the 1st report:"))
date_end = int(input("Input the end date for final report:"))
days = date_end-date_start
# print(days)

def date_nums(day):
    for i in range(day+1):
        date.append(date_start+i)
    return date
print("Selected report dates: ")
print(date_nums(days))

# date1 = date[0]
# report1 = open('workreport-short_'+str(date1)+str(month)+str(year)+'.txt','r')
# read1 = report1.readlines()
# print(read1)


# function to find materials usage:
def material_usage(material):
    for line in read:
        line = line.rstrip()
        # print(line)
        wds = line.split()
        # print(wds)

        if len(wds)>1 and wds[0] == material:
            return wds[-2]


for i in range(len(date)):
    print(i,end= " ") 
    report = open('workreport-short_'+str(date[i])+str(month)+str(year)+'.txt','r')
    read = report.readlines()
    concrete_usage = int(material_usage('Concrete'))
    concrete.append(concrete_usage)
    sand_usage = int(material_usage('Sand'))
    sand.append(sand_usage)
    stone_usage = int(material_usage('Stone'))
    stone.append(stone_usage)

print('\nStone usage list:')
print(concrete)
print('Sand usage list:')
print(sand)
print('Stone usage list:')
print(stone)


plt.xlabel("Date")

# to show concrete usage in a week:
plt.ylabel("Concrete usage")
plt.plot(date,concrete)
plt.show()

# # sand 
plt.ylabel("Sand usage")
plt.plot(date,sand)
plt.show()

# # stone
plt.ylabel("Stone usage")
plt.plot(date,stone)
plt.show()