'''method 1'''
if __name__ == '__main__':
    n = int(input())
    for i in range (n):
        print(i**2)
 
 '''method 2 (using math)'''
 import math #math header file which contain math related function
if __name__ == '__main__':
    n = int(input())
    for i in range (n):
        print(int(math.pow(i,2))) #The pow() function returns the value of x to the power of y (xy)
