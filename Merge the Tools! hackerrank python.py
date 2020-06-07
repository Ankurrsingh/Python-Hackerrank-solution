def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string), k):
        cstr = string[i:i+k]    #return string of specified length from ith index to i+kth index 
        newstr = ""
        for i in cstr:
            if i not in newstr:
                newstr+=i
        print(newstr)



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
