#1800-2025

fw = open("file_operation\\leap_year.txt","w")

for year in range(1800,2027):

    if (year % 100 != 0 and year%4==0) or (year%100==0 and year%400==0):

        fw.write(str(year) + "\n")

print("completed...")

fw.close()