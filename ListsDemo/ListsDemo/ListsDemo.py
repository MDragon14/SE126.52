# Week 4: Lists Demo.

list1 = ["Sam", "Mary", "Bill", "Adam", "Betty"]
print(list1)
print("")

print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])

num_records = len(list1)

print("\nNumber of Records in List1: ", num_records)
print("")

#Better way to to print/process a full list w/ contents is by using a FOR LOOP
print("")
print("")

for index in range (0, num_records):

    print("Index#", index, "\t", list1[index])

print("")
print("")
#------------------------------------------------------------------------------------------------------------------#
list2 = ["Sam", "18", "32000"]
list3 = ["Mary", "21", "34000"]
list4 = ["Tom", "24", "38000"]

#Step #1: Create Empty Lists (each field should have its own list)
name = []
age = []
salary = []

#Step #2: Add elements to the list (populating the list)
name.append(list2[0])
name.append(list3[0])
name.append(list4[0])
print("")

for index in range (0, 3):
    print(name[index])

print("")
print("\t\t============================== PART 1 DEMO COMPLETE ==============================\n\n")
#=====================================================================================================================
import csv

tot_records = 0

name = []
age = []
salary = []

with open("C:/Users/000859945/Desktop/MDragon SE126.52/ListsDemo.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        tot_records += 1
        name.append(rec[0])
        age.append(int(rec[1]))
        salary.append(float(rec[2]))

for index in range (0, tot_records):
    print("Index: ",index, "\t", name[index], "\t", age[index], "\t$",salary[index])

age_total = 0
for index in range (0, tot_records):
    age_total += age[index]

age_avg = age_total / tot_records
print("\nAverage Age in the File:",age_avg, "years.")

sal_total = 0
for index in range (0, tot_records):
    sal_total += salary[index]

sal_avg = sal_total / tot_records
print("\nAverage Salary in the File: ${:.2f}".format(sal_avg))

print("\nTotal Records Processed: ",tot_records)
print()