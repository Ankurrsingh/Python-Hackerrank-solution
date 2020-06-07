''' Method-1 nested loop'''

def is_leap(year):
    leap = False
    
    # Write your logic here
    if(year%4==0):
        leap=True      #if year is evenly divisible by 4 it set value of leap to True
        if(year%100==0):  # checks that value of year is divisible by 100 or not Ex:year=2100
            if(year%400==0):  #if year is evenly divisible by 100 then check for year%400
                leap=True
            else:
                leap=False
    
    
    return leap

year = int(input())



''' Method-2 if-else'''

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
    
    return leap
year = int(input())
