'''
Sample Input

5
Sample Output

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''

solution:

import string
def print_rangoli(size):
    # your code goes here
    alpha = string.ascii_lowercase  #change the input in lowercase
    L = []

    for i in range(n):
        s = "-".join(alpha[i:n])     # in first iteration give output as 'a-b-c-d-e'
        L.append(s[::-1]+s[1:])      #this appends (e-d-c-b-a +-b-c-d-e = e-d-c-b-a-b-c-d-e) in the list L
    width = len(L[0])                #length of largest string=17
    for i in range(n-1, 0, -1):
        print(L[i].center(width, "-"))     #add l[i]=e in the center of 17 that is at 9th place and rest space have -and this goes for all iteration and print half of rangoli   
    for i in range(n):                   
        print(L[i].center(width, "-"))     #rest half rangoli is printed by this
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
