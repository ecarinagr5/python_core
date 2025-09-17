def is_leap(year):
    leap = False
    
    # Write your logic here
    if year > 1900:
       if year % 4 == 0:
          leap = True
       else:
           leap = False
    else:
        print("This number is not valid")
    return leap

year = int(input())