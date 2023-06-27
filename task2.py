# David Wu
# Task 2 2023-06-27

cOpt = input("Would you like to convert from hours to minutes or minutes to hours? Type in 'h' to convert into hours OR Type in 'm' to convert into minutes")

if cOpt == 'h':
    iNofM = float(input("How many minutes would you like to convert into hours"))
    print(str(iNofM // 60) + " hours")
elif cOpt == 'm':
    iNofH = float(input("How many hours would you like to convert into minutes"))
    print(str(iNofH * 60) + " minutes")
else:
    print("Wrong input, please only enter 'h' or 'm'")