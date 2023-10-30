# 2.1Write a program that determines whether a year entered by the user is a leap year or not using ifelif-else statements.
# Python3 implementation to check 
# if the year is a leap year 
# using macros
 
# Macro to check if a year 
# is a leap year

def ISLP(y):

  if((y % 400 == 0) or

     (y % 100 != 0) and

     (y % 4 == 0)): 

    return 1;

  else:

    return 0;
 
# Driver code

if __name__=='__main__':
 

  year = 2020;

  print(ISLP(year));
 

  # This code is contributed by  Pratham76.year = int(input("Enter Year: "))

year = int(input("Enter Year: "))

# Leap Year Check
if year % 4 == 0 and year % 100 != 0:
    print(year, "is a Leap Year")
elif year % 100 == 0:
    print(year, "is not a Leap Year")
elif year % 400 ==0:
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")