import matplotlib
import matplotlib.pyplot as plt

date = []
concrete = []
sand = []
stone = []

date1 = "16022022"

# # to calculate the start date & number of days for the report:
# date_start = input("Inout the start date for the 1st report:")
# date_end = input("Input the end date for final report:")
# days = date_start-date_end

# def date_nums(days):
#     for i in range(days):
#         date.append(i)
#     return date


report1 = open('C:/Users/tatwai/Documents/David/Python/Scripts/Exercise/Work done report/workreport-short_'+date1+'.txt')

# function to find materials usage:
def material_usage(material):
    for line in report1:
        line = line.rstrip()
        # print(line)
        wds = line.split()
        # print(wds)

        if len(wds)>1 and wds[0] == material:
            return wds[1]
    # else:    
    #     continue

concrete_usage1 = int(material_usage("Concrete"))
sand_usage1 = int(material_usage('Sand'))
stone_usage1 = int(material_usage('Stone'))

print('Date=',date1,concrete_usage1,sand_usage1,stone_usage1)
# print(type(concrete_usage1))
date.append(date1)
concrete.append(concrete_usage1)
sand.append(sand_usage1)
stone.append(stone_usage1)


date2 = 17
report2 = open('C:/Users/tatwai/Documents/David/Python/Scripts/Exercise/Work done report/workreport-short_17022022.txt')

# function to find materials usage:
def material_usage(material):
    for line in report2:
        line = line.rstrip()
        # print(line)
        wds = line.split()
        # print(wds)

        if len(wds)>1 and wds[0] == material:
            return wds[1]
    # else:    
    #     continue

concrete_usage2 = int(material_usage("Concrete"))
sand_usage2 = int(material_usage('Sand'))
stone_usage2 = int(material_usage('Stone'))

print('Date=',date2,concrete_usage2,sand_usage2,stone_usage2)
date.append(date2)
concrete.append(concrete_usage2)
sand.append(sand_usage2)
stone.append(stone_usage2)


date3 = 18
report3 = open('C:/Users/tatwai/Documents/David/Python/Scripts/Exercise/Work done report/workreport-short_18022022.txt')

# function to find materials usage:
def material_usage(material):
    for line in report3:
        line = line.rstrip()
        # print(line)
        wds = line.split()
        # print(wds)

        if len(wds)>1 and wds[0] == material:
            return wds[1]
    # else:    
    #     continue

concrete_usage3 = int(material_usage("Concrete"))
sand_usage3 = int(material_usage('Sand'))
stone_usage3 = int(material_usage('Stone'))

print('Date=',date3,concrete_usage3,sand_usage3,stone_usage3)
date.append(date3)
concrete.append(concrete_usage3)
sand.append(sand_usage3)
stone.append(stone_usage3)


date4 = 19
report4 = open('C:/Users/tatwai/Documents/David/Python/Scripts/Exercise/Work done report/workreport-short_19022022.txt')

# function to find materials usage:
def material_usage(material):
    for line in report4:
        line = line.rstrip()
        # print(line)
        wds = line.split()
        # print(wds)

        if len(wds)>1 and wds[0] == material:
            return wds[1]
    # else:    
    #     continue

concrete_usage4 = int(material_usage("Concrete"))
sand_usage4 = int(material_usage('Sand'))
stone_usage4 = int(material_usage('Stone'))

print('Date=',date4,concrete_usage4,sand_usage4,stone_usage4)
date.append(date4)
concrete.append(concrete_usage4)
sand.append(sand_usage4)
stone.append(stone_usage4)


date5 = 20
report5 = open('C:/Users/tatwai/Documents/David/Python/Scripts/Exercise/Work done report/workreport-short_20022022.txt')

# function to find materials usage:
def material_usage(material):
    for line in report5:
        line = line.rstrip()
        # print(line)
        wds = line.split()
        # print(wds)

        if len(wds)>1 and wds[0] == material:
            return wds[1]
    # else:    
    #     continue

concrete_usage5 = int(material_usage("Concrete"))
sand_usage5 = int(material_usage('Sand'))
stone_usage5 = int(material_usage('Stone'))

print('Date=',date5,concrete_usage5,sand_usage5,stone_usage5)
date.append(date5)
concrete.append(concrete_usage5)
sand.append(sand_usage5)
stone.append(stone_usage5)


plt.xlabel("date")
# to show concrete usage in a week:
# plt.ylabel("concrete")
# plt.plot(date,concrete)
# plt.show()

# # sand 
plt.ylabel("sand")
plt.plot(date,sand)
plt.show()

# # stone
# plt.ylabel("stone")
# plt.plot(date,stone)
# plt.show()