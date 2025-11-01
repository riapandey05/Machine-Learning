# If a year is divisible by 4 but not by 100: It is a leap year (e.g., 2024).
# If a year is divisible by both 100 and 400: It is a leap year (e.g., 2000).
# If a year is divisible by 100 but not by 400: It is not a leap year (e.g., 1900).
# If a year is not divisible by 4: It is not a leap year (e.g., 2023). 
year = int(input("Enter a year:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"{year} is a leap year")
        else:
            print("not a leap year")
    else:
        print("yes a leap year")
else:
    print(f"{year} is not a leap year")
    
