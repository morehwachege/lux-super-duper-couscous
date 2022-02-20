year = int(input("Please Enter Year: "))
if year % 4 == 0:
    year_lst = list(str(year))
    if year_lst[2:][0] == '0' and year_lst[2:][1] == '0':
        # leap century year check
        if year % 400 == 0:
            print("The year is a leap Century year!!")
        else:
            print("The year is not a leap Century year!! :( ")
    else:
        print("This is a leap year")
else:
    print("This is not leap year!! :( ")